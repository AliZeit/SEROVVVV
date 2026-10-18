"""Структурные проверки; не заменяют визуальную проверку Writer."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile, ZIP_STORED
from xml.etree import ElementTree as ET
from odf.opendocument import load
from report import build

ROOT = Path(__file__).resolve().parent
NS = {'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
      'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
      'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0'}


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'examples/demo.json').read_text(encoding='utf-8'))
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'report.odt'

    def make(self, data=None):
        return build(data or self.data, ROOT / 'examples', self.path)

    def test_container_and_images(self):
        self.make()
        load(str(self.path))
        with ZipFile(self.path) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(z.namelist()[0], 'mimetype')
            self.assertEqual(z.getinfo('mimetype').compress_type, ZIP_STORED)
            self.assertEqual(z.read('mimetype'), b'application/vnd.oasis.opendocument.text')
            self.assertEqual(len([n for n in z.namelist() if n.startswith('Pictures/')]), 3)
            for n in z.namelist():
                if n.endswith('.xml'):
                    ET.fromstring(z.read(n))
            content = z.read('content.xml').decode()
            self.assertIn('Рисунок 1.3', content)
            self.assertNotIn('{fig:', content)
            self.assertIn('table-of-content-source', content)

    def test_page_styles(self):
        self.make()
        with ZipFile(self.path) as z:
            styles = ET.fromstring(z.read('styles.xml'))
            for p in styles.findall('.//style:page-layout-properties', NS):
                for prop, value in [('margin-left', '3cm'), ('margin-right', '1.5cm'),
                                    ('margin-top', '2cm'), ('margin-bottom', '2cm')]:
                    self.assertEqual(p.get('{'+NS['fo']+'}'+prop), value)
            pages = styles.findall('.//style:master-page', NS)
            title = next(p for p in pages if p.get('{'+NS['style']+'}name') == 'TitlePage')
            main = next(p for p in pages if p.get('{'+NS['style']+'}name') == 'Main')
            self.assertIsNone(title.find('style:footer', NS))
            self.assertIsNotNone(main.find('.//text:page-number', NS))

    def test_missing_image_fails(self):
        self.data['sections'][1]['blocks'][2]['path'] = 'missing.png'
        with self.assertRaises(ValueError):
            self.make()
        self.assertFalse(self.path.exists())

    def test_bad_reference_fails(self):
        self.data['sections'][0]['blocks'][0]['text'] = 'Рисунок {fig:unknown}'
        with self.assertRaises(ValueError):
            self.make()

    def test_duplicate_id_fails(self):
        blocks = self.data['sections'][1]['blocks']
        blocks.append(copy.deepcopy(blocks[2]))
        with self.assertRaises(ValueError):
            self.make()

    def test_numbering_restarts(self):
        section = copy.deepcopy(self.data['sections'][1])
        for b in section['blocks']:
            if b['type'] == 'figure':
                b['id'] += '_copy'
        self.data['sections'].insert(2, section)
        self.make()
        with ZipFile(self.path) as z:
            self.assertIn('Рисунок 2.1', z.read('content.xml').decode())

    def test_table_and_no_toc(self):
        self.data['toc'] = False
        self.data['sections'][1]['blocks'].append({'type': 'table', 'caption': 'Параметры',
                                                   'rows': [['Параметр', 'Значение'], ['ОЗУ', '4 Гбайт']]})
        self.make()
        with ZipFile(self.path) as z:
            content = z.read('content.xml').decode()
            self.assertIn('Таблица 1.1', content)
            self.assertNotIn('table-of-content-source', content)


if __name__ == '__main__':
    unittest.main()
