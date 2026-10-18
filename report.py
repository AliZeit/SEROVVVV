#!/usr/bin/env python3
"""Генератор ODT по СТАНДАРТУ 01-2023 Университета «Сириус».
Python 3.10+. Данные и пути к изображениям задаются в JSON; код не исполняется.
"""
import argparse
import json
import re
from pathlib import Path

from PIL import Image as PILImage
from odf.opendocument import OpenDocumentText
from odf import style, text, draw, table
from odf.teletype import addTextToElement


def validate(data, base):
    if not isinstance(data, dict):
        raise ValueError('Корень JSON должен быть объектом')
    for key in ('title', 'discipline', 'student', 'group', 'teacher', 'year'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'Обязательная непустая строка: {key}')
    if not isinstance(data.get('sections'), list) or not data['sections']:
        raise ValueError('Нужен непустой массив sections')
    ids = set()
    for section in data['sections']:
        if not isinstance(section.get('title'), str) or not section['title'].strip():
            raise ValueError('У раздела отсутствует title')
        for block in section.get('blocks', []):
            kind = block.get('type')
            if kind not in ('paragraph', 'heading', 'figure', 'table'):
                raise ValueError(f'Неизвестный тип блока: {kind}')
            if kind in ('paragraph', 'heading') and not isinstance(block.get('text'), str):
                raise ValueError(f'У блока {kind} отсутствует text')
            if kind in ('figure', 'table'):
                if not isinstance(block.get('caption'), str) or not block['caption'].strip():
                    raise ValueError('Нужна непустая подпись caption')
            if kind == 'figure':
                ident = block.get('id')
                if not isinstance(ident, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', ident) or ident in ids:
                    raise ValueError(f'Некорректный или повторный id рисунка: {ident}')
                if not section.get('numbered', False):
                    raise ValueError('Рисунки помещайте в нумеруемый раздел')
                ids.add(ident)
                path = (base / block['path']).resolve()
                if not path.is_file():
                    raise ValueError(f'Изображение не найдено: {path}')
                with PILImage.open(path) as im:
                    if im.format not in ('PNG', 'JPEG'):
                        raise ValueError('Поддерживаются изображения PNG и JPEG')
                    im.verify()
            if kind == 'table':
                if not section.get('numbered', False):
                    raise ValueError('Таблицы помещайте в нумеруемый раздел')
                rows = block.get('rows')
                if not rows or not isinstance(rows, list) or not isinstance(rows[0], list) or not rows[0]:
                    raise ValueError('Таблица должна содержать непустые rows')
                if any(not isinstance(r, list) or len(r) != len(rows[0]) or any(not isinstance(c, str) for c in r) for r in rows):
                    raise ValueError('Строки таблицы должны иметь одинаковое число текстовых ячеек')
    for section in data['sections']:
        for block in section.get('blocks', []):
            if block['type'] == 'paragraph':
                for ident in re.findall(r'\{fig:([^}]+)\}', block['text']):
                    if ident not in ids:
                        raise ValueError(f'Ссылка на неизвестный рисунок: {ident}')


def build(data, base, destination):
    validate(data, base)
    doc = OpenDocumentText()
    font = style.FontFace(name='Times New Roman', fontfamily='Times New Roman')
    doc.fontfacedecls.addElement(font)

    def ps(name, parent=None, props=None, tp=None, **attrs):
        s = style.Style(name=name, family='paragraph', **attrs)
        if parent:
            s.setAttribute('parentstylename', parent)
        if props:
            s.addElement(style.ParagraphProperties(**props))
        if tp:
            s.addElement(style.TextProperties(**tp))
        doc.styles.addElement(s)
        return s

    ps('Body', props=dict(textalign='justify', textindent='1.25cm', lineheight='150%',
                          margintop='0cm', marginbottom='0cm', orphans=2, widows=2),
       tp=dict(fontname='Times New Roman', fontsize='14pt', color='#000000', language='ru', country='RU'))
    ps('Center', 'Body', dict(textalign='center', textindent='0cm'))
    ps('TitleFirst', 'Center', dict(lineheight='100%'), masterpagename='TitlePage')
    ps('TitleLine', 'Center', dict(lineheight='100%', marginbottom='0.15cm'))
    ps('TitleTopic', 'Center', dict(margintop='1.8cm', marginbottom='0.7cm'), dict(fontweight='bold'))
    ps('Sign', 'Body', dict(marginleft='7cm', textindent='0cm', textalign='left', lineheight='100%', marginbottom='0.18cm'))
    ps('City', 'Center', dict(margintop='1.6cm', lineheight='100%'))
    ps('Major', 'Center', dict(breakbefore='page', margintop='0cm', marginbottom='21pt', keepwithnext='always'), dict(fontweight='bold'), masterpagename='Main')
    ps('Minor', 'Center', dict(margintop='21pt', marginbottom='21pt', keepwithnext='always'), dict(fontweight='bold'))
    ps('Figure', 'Center', dict(lineheight='100%', margintop='0.3cm', keepwithnext='always'))
    ps('Caption', 'Center', dict(lineheight='100%', marginbottom='0.5cm', keeptogether='always'))
    ps('TableCaption', 'Body', dict(textindent='0cm', textalign='left', lineheight='100%', keepwithnext='always'))
    ps('Cell', 'Body', dict(textindent='0cm', textalign='left', lineheight='100%'))
    ps('Footer', 'Center', dict(lineheight='100%'))
    ps('TOC', 'Body', dict(textindent='0cm', textalign='left'))

    for name in ('TitleLayout', 'MainLayout'):
        layout = style.PageLayout(name=name)
        layout.addElement(style.PageLayoutProperties(pagewidth='21cm', pageheight='29.7cm',
            printorientation='portrait', marginleft='3cm', marginright='1.5cm',
            margintop='2cm', marginbottom='2cm', numformat='1'))
        if name == 'MainLayout':
            fs = style.FooterStyle()
            fs.addElement(style.HeaderFooterProperties(minheight='0.5cm', margintop='0.5cm'))
            layout.addElement(fs)
        doc.automaticstyles.addElement(layout)
    titlepage = style.MasterPage(name='TitlePage', pagelayoutname='TitleLayout', nextstylename='Main')
    mainpage = style.MasterPage(name='Main', pagelayoutname='MainLayout')
    footer = style.Footer()
    p = text.P(stylename='Footer')
    p.addElement(text.PageNumber(selectpage='current'))
    footer.addElement(p)
    mainpage.addElement(footer)
    doc.masterstyles.addElement(titlepage)
    doc.masterstyles.addElement(mainpage)

    def para(value='', sty='Body', parent=None):
        p = text.P(stylename=sty)
        addTextToElement(p, value)
        (parent if parent is not None else doc.text).addElement(p)
        return p

    para('Автономная некоммерческая образовательная организация высшего образования', 'TitleFirst')
    para('«НАУЧНО-ТЕХНОЛОГИЧЕСКИЙ УНИВЕРСИТЕТ «СИРИУС»', 'TitleLine')
    para(data.get('department', 'Структурное подразделение колледж'), 'TitleLine')
    para(data.get('program', '[Код и наименование направления]'), 'TitleLine')
    para(data['title'].upper(), 'TitleTopic')
    para('Отчет по лабораторной работе' + (' № ' + str(data['lab_number']) if data.get('lab_number') else ''), 'TitleLine')
    para('по дисциплине «' + data['discipline'] + '»', 'TitleLine')
    para('', 'TitleLine')
    if data.get('draft', True):
        para('ШАБЛОН / ЧЕРНОВИК — НЕ ДЛЯ СДАЧИ', 'TitleLine')
    para('', 'TitleLine')
    for line in [f'Студент группы {data["group"]}', f'____________ {data["student"]}',
                 data.get('date', '«___» __________ 20__ г.'), '', 'Руководитель',
                 data.get('teacher_position', '[Должность руководителя]'),
                 'Работа выполнена на оценку «_____»', f'____________ {data["teacher"]}',
                 '«___» __________ 20__ г.']:
        para(line, 'Sign')
    para('Федеральная территория «Сириус» ' + data['year'], 'City')

    if data.get('toc', True):
        toc = text.TableOfContent(name='Contents', protected='false', stylename='Major')
        source = text.TableOfContentSource(outlinelevel=2, useoutlinelevel='true')
        title = text.IndexTitleTemplate(stylename='Major')
        title.addText('Оглавление')
        source.addElement(title)
        for level in (1, 2):
            entry = text.TableOfContentEntryTemplate(outlinelevel=level, stylename='TOC')
            entry.addElement(text.IndexEntryText())
            entry.addElement(text.IndexEntryTabStop(type='right', position='16.5cm', leaderchar='.'))
            entry.addElement(text.IndexEntryPageNumber())
            source.addElement(entry)
        toc.addElement(source)
        body = text.IndexBody()
        para('Оглавление', 'Major', body)
        para('Обновите оглавление в LibreOffice: Сервис → Обновить → Обновить всё.', 'Body', body)
        toc.addElement(body)
        doc.text.addElement(toc)

    refs, section_number = {}, 0
    for section in data['sections']:
        if section.get('numbered', False):
            section_number += 1
        n = 0
        for b in section.get('blocks', []):
            if b['type'] == 'figure':
                n += 1
                refs[b['id']] = f'{section_number}.{n}'

    section_number = 0
    for section in data['sections']:
        label = section['title']
        if section.get('numbered', False):
            section_number += 1
            label = f'{section_number} {label.upper()}'
        doc.text.addElement(text.H(outlinelevel=1, stylename='Major', text=label))
        subsection = table_number = 0
        for b in section.get('blocks', []):
            kind = b['type']
            if kind == 'paragraph':
                para(re.sub(r'\{fig:([^}]+)\}', lambda m: refs[m[1]], b['text']))
            elif kind == 'heading':
                subsection += 1
                prefix = f'{section_number}.{subsection} ' if section.get('numbered', False) else ''
                doc.text.addElement(text.H(outlinelevel=2, stylename='Minor', text=prefix + b['text']))
            elif kind == 'figure':
                path = (base / b['path']).resolve()
                with PILImage.open(path) as im:
                    w, h = im.size
                # Сохраняем пропорции; высокие снимки не выталкивают подпись за лист.
                width = min(16.5, 17 * w / h)
                height = width * h / w
                p = para('', 'Figure')
                frame = draw.Frame(name=b['id'], anchortype='as-char', width=f'{width:.3f}cm', height=f'{height:.3f}cm')
                href = doc.addPicture(str(path))
                frame.addElement(draw.Image(href=href, type='simple', show='embed', actuate='onLoad'))
                p.addElement(frame)
                para(f'Рисунок {refs[b["id"]]} — {b["caption"]}', 'Caption')
            elif kind == 'table':
                table_number += 1
                para(f'Таблица {section_number}.{table_number} — {b["caption"]}', 'TableCaption')
                t = table.Table(name=f'Table{section_number}_{table_number}')
                cs = style.Style(name=f'Cell{section_number}_{table_number}', family='table-cell')
                cs.addElement(style.TableCellProperties(border='0.5pt solid #000000', padding='0.12cm'))
                doc.automaticstyles.addElement(cs)
                for row in b['rows']:
                    tr = table.TableRow()
                    for value in row:
                        cell = table.TableCell(valuetype='string', stylename=cs)
                        para(value, 'Cell', cell)
                        tr.addElement(cell)
                    t.addElement(tr)
                doc.text.addElement(t)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(destination), addsuffix=False)
    return destination


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('data', type=Path, help='JSON с содержимым отчета')
    ap.add_argument('-o', '--output', type=Path, required=True, help='Выходной файл .odt')
    args = ap.parse_args()
    if args.output.suffix.lower() != '.odt':
        ap.error('Выходной файл должен иметь расширение .odt')
    try:
        data = json.loads(args.data.read_text(encoding='utf-8'))
        result = build(data, args.data.resolve().parent, args.output)
    except (ValueError, KeyError, OSError, TypeError) as exc:
        ap.exit(2, f'Ошибка входных данных: {exc}\n')
    print(f'Создано: {result}')
    print('Перед сдачей обновите оглавление и проверьте переносы в LibreOffice Writer.')


if __name__ == '__main__':
    main()
