Тут представленны 16 изображения 1.png ..... 32.png

### 1.png
Создал два сата диска, каждый по 10Гиб
### 2.png
откроем лсблк и видем что оба диска детектятся
### 3.png
открываем cfdisk /dev/sda
### 4.png
выбираем тип гпт
### 5.png
что отображает cfdisk после разметки
### 6.png
Делим второй лиск с помощью parted
### 7.png
форматируем диски
### 8.png
создаем директории
### 9.png
смотрим ююид партишинов первого диска
### 10.png
добовляем их в /etc/fstab/
### 11.png
смотрим ююид партишинов второго диска
### 12.png
создаем первый юнит
### 13.png
запускаем юнит
### 14.png
создаем второй юнит
### 15.png
запускаем второй юнит
### 16.png
Перезагружаем систему и смотрим что все разметилось верно

ЛР8
Лабораторная работа: Управление файловыми системами





вот план лабы:
<div style="max-width: 100%; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);"><!-- Титульная страница -->
<div style="text-align: center; margin-bottom: 50px; border-bottom: 2px solid #333; padding-bottom: 30px;">
<h1 style="color: #2c3e50; margin-bottom: 10px;">УПРАВЛЕНИЕ ФАЙЛОВЫМИ СИСТЕМАМИ</h1>
<h2 style="color: #7f8c8d; font-weight: normal;">Методическое пособие по лабораторной работе</h2>
<p style="color: #95a5a6;">Оценка времени выполнения: 90 минут</p>
</div>
<!-- Цели и задачи -->
<div style="margin-bottom: 40px;">
<h2 style="color: #2c3e50; border-left: 4px solid #3498db; padding-left: 15px;">Цели и задачи работы</h2>
<div style="background-color: #ecf0f1; padding: 20px; border-radius: 5px; margin: 15px 0;">
<h3 style="color: #27ae60; margin-top: 0;">Цели:</h3>
<ul style="color: #2c3e50;">
<li>Освоить методы управления файловыми системами в Linux</li>
<li>Изучить инструменты разметки дисков и создания файловых систем</li>
<li>Научиться настраивать автоматическое монтирование файловых систем</li>
</ul>
</div>
<div style="background-color: #ecf0f1; padding: 20px; border-radius: 5px; margin: 15px 0;">
<h3 style="color: #e74c3c; margin-top: 0;">Задачи:</h3>
<ul style="color: #2c3e50;">
<li>Добавить виртуальные диски в систему</li>
<li>Разметить диски с помощью утилит cfdisk и parted</li>
<li>Создать <a class="autolink" title="Файловые системы" href="https://moodle.siriusuniversity.ru/mod/page/view.php?id=7655">файловые системы</a> ext4 и ext2</li>
<li>Настроить автоматическое монтирование через /etc/fstab</li>
<li>Настроить автоматическое монтирование через systemd unit files</li>
<li>Проверить корректность выполненных действий</li>
</ul>
</div>
</div>
<!-- Теоретическая часть -->
<div style="margin-bottom: 40px;">
<h2 style="color: #2c3e50; border-left: 4px solid #3498db; padding-left: 15px;">Теоретическая часть</h2>
<div style="background-color: #fffacd; padding: 15px; border-left: 4px solid #ffd700; margin: 10px 0;">
<h3 style="color: #8b6914; margin-top: 0;">Ключевые понятия:</h3>
<p><strong>Файловая система</strong> - способ организации и хранения данных на носителе информации.</p>
<p><strong>Раздел диска</strong> - логическое разделение дискового пространства на независимые области.</p>
<p><strong>Монтирование</strong> - процесс подключения файловой системы к определенной точке в дереве каталогов.</p>
<p><strong>/etc/fstab</strong> - файл конфигурации, содержащий информацию о файловых системах, монтируемых при загрузке.</p>
<p><strong>Systemd mount units</strong> - альтернативный способ настройки автоматического монтирования через systemd.</p>
</div>
</div>
<!-- Практическая часть -->
<div style="margin-bottom: 40px;">
<h2 style="color: #2c3e50; border-left: 4px solid #3498db; padding-left: 15px;">Практическая часть</h2>
<!-- Шаг 1 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 1: Добавление дисков к виртуальной машине</h3>
<p>Добавьте два новых виртуальных диска к вашей виртуальной машине через интерфейс гипервизора.</p>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-1.png" alt="Добавление дисков к ВМ">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 1: Добавление дисков к ВМ</p>
</div>
<!-- Шаг 2 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 2: Определение имен новых дисков</h3>
<p>После добавления дисков выполните команду <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">lsblk</code> для просмотра доступных блочных устройств:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 1.2em;">root@Fedora-SRV-43:~# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda     8:0    0    80G  0 disk
├─sda1  8:1    0   128M  0 part /boot/efi
├─sda2  8:2    0    1G  0 part /boot
├─sda3  8:3    0  35,9G  0 part /home
├─sda4  8:4    0    35G  0 part /
└─sda5  8:5    0     8G  0 part [SWAP]
sdb     8:16   0    10G  0 disk
sdc     8:32   0    10G  0 disk
zram0  251:0   0   3,8G  0 disk [SWAP]</pre>
<p>На изображении видно, что добавлены два новых диска: <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdb</code> и <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdc</code> по 10ГБ каждый.</p>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-2.png" alt="Результат команды lsblk">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 2: Получение наименования новых дисков</p>
</div>
<!-- Шаг 3 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 3: Разметка диска с помощью cfdisk</h3>
<p>Разметьте диск <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">/dev/sdb</code> с помощью утилиты <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">cfdisk</code>:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo cfdisk /dev/sdb</pre>
<p>Создайте два раздела одинакового размера (по 5ГБ каждый).</p>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px; margin-bottom: 10px;" src="https://nimnull.ru/img/labs/filesystem/file-3.png" alt="Выбор типа диска в cfdisk">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 3: Выбор типа диска</p>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-4.png" alt="Результат разделения диска">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 4: Результат разделения дисков</p>
</div>
<!-- Шаг 4 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 4: Разметка диска с помощью parted</h3>
<p>Разметьте диск <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">/dev/sdc</code> с помощью утилиты <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">parted</code>:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto; font-family: 'Courier New', monospace; font-size: 1.2em;">root@Fedora-SRV-43:~# parted /dev/sdc mktable gpt
root@Fedora-SRV-43:~# parted /dev/sdc mkpart d1 1 5Gb
root@Fedora-SRV-43:~# parted /dev/sdc mkpart d2 5Gb 10Gb
root@Fedora-SRV-43:~# parted /dev/sdc print
Модель: ATA VMware Virtual S (scsi)
Диск /dev/sdc: 10,7GB
Размер сектора (логич./физич.): 512B/512B
Таблица разделов: gpt
Флаги диска:

Номер  Начало  Конец  Размер  Файловая система  Имя  Флаги
1      1049kB  5000MB 4999MB                   d1
2      5000MB  10,0GB 5001MB                   d2</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-5.png" alt="Разметка диска с помощью parted">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 5: Разметка диска с помощью parted</p>
</div>
<!-- Шаг 5 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 5: Создание файловых систем</h3>
<p>Создайте <a class="autolink" title="Файловые системы" href="https://moodle.siriusuniversity.ru/mod/page/view.php?id=7655">файловые системы</a> на разделах:</p>
<ul>
<li>На первых разделах (<code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdb1</code>, <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdc1</code>) - ext4</li>
<li>На вторых разделах (<code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdb2</code>, <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdc2</code>) - ext2</li>
</ul>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo mkfs.ext4 /dev/sdb1
sudo mkfs.ext4 /dev/sdc1
sudo mkfs.ext2 /dev/sdb2
sudo mkfs.ext2 /dev/sdc2</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-6.png" alt="Форматирование дисков">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 6: Форматирование дисков</p>
</div>
<!-- Шаг 6 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 6: Создание точек монтирования</h3>
<p>Создайте директории для точек монтирования:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">mkdir -p /opt/data/{storage,cache,export,log}</pre>
<p>Проверьте создание директорий:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">ls -l /opt/data</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-7.png" alt="Создание точек монтирования">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 7: Создание точек монтирования</p>
</div>
<!-- Шаг 7 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 7: Настройка автоматического монтирования через /etc/fstab</h3>
<p>Для диска <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdb</code> используем файл <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">/etc/fstab</code>.</p>
<p>Сначала определим UUID разделов:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo blkid | grep sdb</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-8.png" alt="Определение UUID диска sdb">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 8: Результат команды sudo blkid | grep sdb</p>
<p>Добавьте строки в файл <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">/etc/fstab</code>:</p>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-9.png" alt="Файл /etc/fstab">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 9: Файл /etc/fstab</p>
<div style="background-color: #e8f4f8; padding: 15px; border-radius: 5px; margin: 10px 0;">
<h4 style="color: #2980b9; margin-top: 0;">Пояснение параметров fstab:</h4>
<ul>
<li><strong>device</strong> - накопитель (путь или UUID)</li>
<li><strong>dir</strong> - каталог для монтирования</li>
<li><strong>type</strong> - тип файловой системы</li>
<li><strong>options</strong> - опции монтирования</li>
<li><strong>dump</strong> - создание резервной копии (0-нет, 1-да)</li>
<li><strong>fsck</strong> - проверка ФС при загрузке (0-нет, 1-высокий приоритет, 2-низкий приоритет)</li>
</ul>
</div>
</div>
<!-- Шаг 8 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 8: Настройка автоматического монтирования через systemd</h3>
<p>Для диска <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdc</code> используем юниты systemd типа mount.</p>
<p>Определим UUID разделов:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo blkid | grep sdc</pre>
<p>Создайте юнит для <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdc1</code>:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo systemctl --force --full edit opt-data-export.mount</pre>
<p>Содержимое юнита:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">[Unit]
Description=mount /opt/data/export

[Mount]
What=UUID="ff9a04d0-6b14-4B60-ab40-4e378009236e"
Where=/opt/data/export
Type=ext4
Options=defaults

[Install]
WantedBy=multi-user.target</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-10.png" alt="Юнит для sdc1">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 10: Содержимое юнита для sdc1</p>
<p>Сохраните файл как: <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">/lib/systemd/system/opt-data-export.mount</code></p>
<p>Активируйте юнит:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo systemctl start opt-data-export.mount
sudo systemctl enable opt-data-export.mount</pre>
<p>Аналогично создайте юнит для <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">sdc2</code>:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">[Unit]
Description=mount /opt/data/log

[Mount]
What=UUID="57745698-2b8c-4273-b876-8b893c6b732a"
Where=/opt/data/log
Type=ext2
Options=defaults

[Install]
WantedBy=multi-user.target</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-11.png" alt="Юнит для sdc2">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 11: Содержимое юнита sdc2</p>
<p>Сохраните как: <code style="background-color: #f8f9fa; padding: 2px 5px; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 1.2em;">/lib/systemd/system/opt-data-log.mount</code></p>
<p>Активируйте юнит:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">sudo systemctl start opt-data-log.mount
sudo systemctl enable opt-data-log.mount</pre>
</div>
<!-- Шаг 9 -->
<div style="background-color: white; border: 1px solid #ddd; padding: 20px; margin: 15px 0; border-radius: 5px;">
<h3 style="color: #2980b9; margin-top: 0;">Шаг 9: Проверка результатов</h3>
<p>Перезагрузите систему и проверьте корректность автоматического монтирования:</p>
<pre style="background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace; font-size: 1.2em;">lsblk -f</pre>
<img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/filesystem/file-12.png" alt="Результат автомонтирования">
<p style="text-align: center; font-style: italic; margin-top: 10px;">Рисунок 12: Результат автомонтирования после перезагрузки</p>
<div style="background-color: #d4edda; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p style="color: #155724; margin: 0;">✅ Все <a class="autolink" title="Файловые системы" href="https://moodle.siriusuniversity.ru/mod/page/view.php?id=7655">файловые системы</a> должны быть автоматически смонтированы в соответствующие каталоги после перезагрузки.</p>
</div>
</div>
</div>
<!-- Контрольные вопросы -->
<div style="margin-bottom: 40px;">
<h2 style="color: #2c3e50; border-left: 4px solid #3498db; padding-left: 15px;">Контрольные вопросы</h2>
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin: 15px 0;">
<ol>
<li>В чем разница между файловыми системами ext2, ext3 и ext4?</li>
<li>Какие преимущества и недостатки использования UUID вместо имен устройств в /etc/fstab?</li>
<li>Что произойдет, если в /etc/fstab указать неверный UUID файловой системы?</li>
<li>В чем разница между параметрами fsck 0, 1 и 2 в /etc/fstab?</li>
<li>Какие альтернативные способы монтирования файловых систем существуют кроме /etc/fstab?</li>
<li>Что такое журналирование в файловых системах и зачем оно нужно?</li>
<li>Как посмотреть список смонтированных файловых систем в Linux?</li>
<li>В чем разница между командами mount и systemctl start name.mount?</li>
<li>Как принудительно размонтировать файловую систему, если она занята?</li>
</ol>
</div>
</div>
<!-- Заключение -->
<div style="background-color: #e8f4f8; padding: 25px; border-radius: 8px; margin: 30px 0;">
<h2 style="color: #2c3e50; margin-top: 0;">Заключение</h2>
<p>В ходе лабораторной работы были успешно выполнены все поставленные задачи:</p>
<ul>
<li>Освоены методы разметки дисков с помощью утилит <strong>cfdisk</strong> и <strong>parted</strong></li>
<li>Созданы файловые систем <strong>ext4</strong> и <strong>ext2</strong></li>
<li>Настроено автоматическое монтирование двумя способами: через <strong>/etc/fstab</strong> и <strong>systemd mount units</strong></li>
<li>Проверена корректность работы после перезагрузки системы</li>
</ul>
<p>Полученные навыки являются фундаментальными для администрирования Linux-систем и управления хранилищами данных.</p>
</div>
<!-- Подвал -->
<div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd; color: #7f8c8d;">
<p>Методическое пособие по лабораторной работе "Управление файловыми системами"</p>
</div>
</div>

Use SKILL.md to do this 

Отдай мне файл .odt 
Пиши в обезличенном формате, вроде того что *открылась консоль*





