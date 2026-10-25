Тут представленны 18 изображения 1.png ..... 18.png

### 1.png
1.1.1
### 2.png
1.1.2
### 3.png
проверка файла  с логами через cat var/log/cd.log
### 4.png
1.2
### 5.png
1.3.1
### 6.png
тригерим добавление sda и 1.3.2
### 7.png
2.1
### 8.png
2.2
### 9.png
2.3
### 10.png
Заходим под user1 и lvl-2 
### 11.png
ВИдим что папка польностью доступна
### 12.png
Зайдя по user2 и lvl-1 видем что папка не доступна
### 13.png
Зайдя по user2 и lvl-2 видем что папка доступна
### 14.png
3.1
### 15.png
3.2
### 16.png
3.3
### 17.png
3.4
### 18.png
reboot и проверям получилось ли


ЛР9






вот план лабы:
<div class="box py-3 generalbox boxaligncenter"><div class="no-overflow"><div style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; background-color: #f5f5f5;">
<div style="max-width: 800px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);"><header style="text-align: center; margin-bottom: 30px; border-bottom: 2px solid #3498db; padding-bottom: 15px;">
<h1 style="color: #2c3e50; margin: 0;">Аннотация</h1>
<h2 style="color: #3498db; margin: 10px 0 0 0;">к лабораторной работе "Управление устройствами и модулями ядра"</h2>
</header>
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 5px; margin-bottom: 20px;">
<p style="margin-bottom: 15px;">В этой лабораторной работе вы научитесь управлять оборудованием в Linux на профессиональном уровне. Вы освоите создание правил udev для автоматической реакции на подключение устройств, настроите безопасный доступ к USB-накопителям и получите практические навыки работы с модулями ядра. Эти умения критически важны в повседневной работе системного администратора.</p>
<p style="margin-bottom: 15px;">В реальной IT-инфраструктуре эти знания помогут вам автоматизировать мониторинг подключения устройств, быстро решать проблемы с драйверами, настраивать безопасный доступ к периферийным устройствам и оптимизировать работу серверов. Вы сможете гибко управлять оборудованием без перезагрузки системы и настраивать политики безопасности для разных пользователей.</p>
<p style="margin-bottom: 0;">После выполнения работы вы будете уверенно работать с системой udev, управлять модулями ядра и настраивать разграничение прав доступа к устройствам. Эти навыки станут прочной основой для вашей карьеры в администрировании Linux-систем, DevOps и кибербезопасности.</p>
</div>
<footer style="text-align: center; color: #7f8c8d; font-size: 0.9em; margin-top: 20px; padding-top: 15px; border-top: 1px solid #bdc3c7;">
<p>Лабораторная работа по управлению устройствами и модулями ядра</p>
</footer></div>
</div></div><div class="no-overflow"><div style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; background-color: #f5f5f5;">
<div style="max-width: 1200px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);"><header style="text-align: center; margin-bottom: 40px; border-bottom: 2px solid #3498db; padding-bottom: 20px;">
<h1 style="color: #2c3e50; margin: 0;">Лабораторная работа</h1>
<h2 style="color: #3498db; margin: 10px 0 0 0;">Управление устройствами и модулями ядра</h2>
<p style="color: #7f8c8d; font-style: italic;">Оценка времени выполнения: 60 минут</p>
</header>
<section style="margin-bottom: 40px;">
<h3 style="color: #2c3e50; border-left: 4px solid #3498db; padding-left: 10px;">Цели работы:</h3>
<ul style="padding-left: 20px;">
<li>Освоить создание правил udev для автоматизации действий при подключении устройств</li>
<li>Изучить регистрацию новых подключаемых устройств с разграничением прав доступа</li>
<li>Научиться управлять модулями ядра: загрузкой, выгрузкой и настройкой автозагрузки</li>
</ul>
</section>
<section style="margin-bottom: 40px;">
<h3 style="color: #2c3e50; border-left: 4px solid #e74c3c; padding-left: 10px;">Часть 1: Создание правил udev</h3>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #e74c3c; margin-top: 0;">Шаг 1: Создание сценария для логирования</h4>
<p>Создайте сценарий <code style="font-family: 'Courier New', monospace; background-color: #ecf0f1; padding: 2px 5px; border-radius: 3px;">/usr/bin/cd_log.sh</code>:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">#!/bin/bash
/bin/echo "At $(/bin/date) CD $1 $2 was inserted or ejected" &gt;&gt; /var/log/cd.log</pre>
<p>Сделайте сценарий исполняемым и проверьте его работу:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo chmod +x /usr/bin/cd_log.sh
sudo cd_log.sh</pre>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #e74c3c; margin-top: 0;">Шаг 2: Создание правила udev</h4>
<p>Создайте файл правила <code style="font-family: 'Courier New', monospace; background-color: #ecf0f1; padding: 2px 5px; border-radius: 3px;">/etc/udev/rules.d/99_CD_LOG.rules</code>:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">KERNEL=="sr0", RUN+="/usr/bin/cd_log.sh $env{ID_FS_LABEL} $env{ID_FS_UUID}"</pre>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #e74c3c; margin-top: 0;">Шаг 3: Применение правил и проверка</h4>
<p>Перезагрузите правила udev и протестируйте их:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo udevadm control --reload
udevadm test $(udevadm info /dev/sr0 | grep DEVPATH | awk -F '=' '{print $2}')</pre>
<p>Для проверки работоспособности:</p>
<ol>
<li>Вставьте/эмулируйте компакт-диск</li>
<li>Проверьте содержимое лог-файла:</li>
</ol>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo tail -f /var/log/cd.log</pre>
</div>
</section>
<section style="margin-bottom: 40px;">
<h3 style="color: #2c3e50; border-left: 4px solid #f39c12; padding-left: 10px;">Часть 2: Регистрация нового подключаемого устройства</h3>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #f39c12; margin-top: 0;">Шаг 1: Создание пользователей с разными уровнями доступа</h4>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo useradd -m -s /bin/bash user1
sudo pdpl-user -l 0:3 user1
sudo passwd user1

sudo useradd -m -s /bin/bash user2
sudo pdpl-user -l 0:2 user2
sudo passwd user2</pre>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #f39c12; margin-top: 0;">Шаг 2: Подготовка USB-накопителя</h4>
<p>Создайте файловую систему и настройте права доступа:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo mkfs.ext4 /dev/sdc
sudo mount /dev/sdc /media
sudo pdpl-file 2 /media
sudo chown user1 /media</pre>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #f39c12; margin-top: 0;">Шаг 3: Настройка разграничения доступа</h4>
<p>Используйте утилиту для настройки политик безопасности:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo astra-systemsettings</pre>
<p>В открывшемся интерфейсе настройте доступ только для user1 на 2-м уровне конфиденциальности.</p>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #f39c12; margin-top: 0;">Шаг 4: Проверка работы разграничения доступа</h4>
<p>Проверьте доступность накопителя под разными учетными записями:</p>
<ol>
<li>Войдите как user1 на 2-м уровне конфиденциальности</li>
<li>Попробуйте создать/изменить файл на накопителе</li>
<li>Войдите как user2 на разных уровнях конфиденциальности</li>
<li>Попробуйте получить доступ к накопителю</li>
</ol>
</div>
</section>
<section style="margin-bottom: 40px;">
<h3 style="color: #2c3e50; border-left: 4px solid #27ae60; padding-left: 10px;">Часть 3: Управление модулями ядра</h3>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #27ae60; margin-top: 0;">Шаг 1: Поиск модулей семейства raw</h4>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo cat /lib/modules/$(uname -r)/modules.dep | grep raw.ko</pre>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #27ae60; margin-top: 0;">Шаг 2: Проверка загруженных модулей</h4>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo lsmod | grep _raw</pre>
<p>Для ядра 6.1.90-1 ищем модуль: <code style="font-family: 'Courier New', monospace; background-color: #ecf0f1; padding: 2px 5px; border-radius: 3px;">serio_raw</code></p>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #27ae60; margin-top: 0;">Шаг 3: Ручная загрузка и выгрузка модуля</h4>
<p>Загрузите модуль:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo modprobe serio_raw
sudo lsmod | grep serio_raw</pre>
<p>Выгрузите модуль:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo modprobe -r serio_raw
sudo lsmod | grep serio_raw</pre>
</div>
<div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h4 style="color: #27ae60; margin-top: 0;">Шаг 4: Настройка автозагрузки модуля</h4>
<p>Отредактируйте файл <code style="font-family: 'Courier New', monospace; background-color: #ecf0f1; padding: 2px 5px; border-radius: 3px;">/etc/modules</code>:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;"># /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.

serio_raw</pre>
<p>Перезагрузите систему и проверьте загрузку модуля:</p>
<pre style="font-family: 'Courier New', monospace; background-color: #2c3e50; color: white; padding: 15px; border-radius: 5px; overflow-x: auto;">sudo reboot
sudo lsmod | grep serio_raw</pre>
</div>
</section>
<section style="background-color: #e8f4fd; padding: 20px; border-radius: 5px; border-left: 4px solid #3498db;">
<h3 style="color: #2c3e50; margin-top: 0;">Контрольные вопросы:</h3>
<ol>
<li>Каково назначение демона udev в Linux?</li>
<li>Как происходит обработка событий при подключении устройств?</li>
<li>Какие способы управления модулями ядра вы узнали?</li>
<li>Как настроить автоматическую загрузку модуля при старте системы?</li>
<li>Какие инструменты используются для разграничения доступа к устройствам?</li>
</ol>
</section>
<footer style="margin-top: 40px; text-align: center; color: #7f8c8d; font-size: 0.9em; border-top: 1px solid #bdc3c7; padding-top: 20px;">
<p>Лабораторная работа по управлению устройствами и модулями ядра</p>
</footer></div>
</div></div></div>

Use SKILL.md to do this 

Отдай мне файл .odt 
Пиши в обезличенном формате, вроде того что *открылась консоль*





