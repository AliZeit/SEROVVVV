Привет, сделай из этого отчет по лабороторной по примеру: [Пример лабы 1](../Gentoo.odt)
[Пример лабы 2](<../Лаба 2.odt>)
[Пример лабы 3](<../Лаба 3.odt>)
[Шаблон накиданный по госту](../Шаблон_отчета_IT_Сириус.ott) + [учебный ПУД с инфой](../ИС_темы_0709252_Ист.docx)
[Главный пример, отсюда можно взять титульник](../Отчет_ЛР1_Установка_ROSA_Linux.odt)

Тут представленны 21 изображения 1.png ..... 21.png

### 1.png
Открыл настройки граба, заменил ro на rw и добавил необходимое в строку
### 2.png
Сменил пароль пользователя gefest, проверил, что пароль успешно сменился
### 3.png
Поставил пароль на граб, под пользователем gefest, проверив, что он успешно установился
### 4.png
Изменил параметры граба на GRUB_TIMEOUT=10 и добавил GRUB_TIMEOUT_STYLE=countdown
### 5.png
Сделал update-grub , дабы изменения подтянулись
### 6.png
Мы видим что обновление прошло и видем отсчет от 10 до 1 перед Бутом в систему
### 7.png
Создаем daemon(или как то так)
### 8.png
Параметры нового деамона 
### 9.png
Перезапускаем все деамоны и проверяем статус новосозданного
### 10.png
Включаем деамон





ЛР7
Лабораторная работа: Процесс загрузки и выключения системы





вот план лабы:
<div class="no-overflow" id="yui_3_18_1_1_1792327920741_347"><div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 100%; margin: 0 auto; padding: 20px; background-color: #f9f9f9; font-size: 1.3em;" id="yui_3_18_1_1_1792327920741_346">
<div style="background: white; border-radius: 10px; padding: 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); max-width: 1200px; margin: 0 auto;" id="yui_3_18_1_1_1792327920741_345"><header style="text-align: center; margin-bottom: 30px; border-bottom: 2px solid #4a6ea9; padding-bottom: 15px;">
<h1 style="color: #2c3e50; margin: 0; font-size: 1.6em;">🔧 Лабораторная работа</h1>
<h2 style="color: #4a6ea9; margin: 10px 0 0 0; font-size: 1.6em;">Процесс загрузки и выключения системы</h2>
</header>
<section style="margin-bottom: 30px;">
<h3 style="color: #4a6ea9; border-left: 4px solid #4a6ea9; padding-left: 10px; font-size: 1.6em;">📋 Теоретическая справка</h3>
<div style="background: #f0f7ff; padding: 20px; border-radius: 5px;">
<h4 style="margin-top: 0; font-size: 1.6em;">Процесс загрузки Linux</h4>
<p>Процесс загрузки Linux состоит из нескольких этапов:</p>
<ol>
<li><strong>BIOS/UEFI</strong> - инициализация оборудования и поиск загрузчика</li>
<li><strong>GRUB</strong> - загрузчик, позволяющий выбрать ядро и передать параметры</li>
<li><strong>Ядро Linux</strong> - инициализация системы, монтирование корневой файловой системы</li>
<li><strong>systemd</strong> - инициализация пользовательского пространства и служб</li>
</ol>
<h4 style="font-size: 1.6em;">GRUB (Grand Unified Bootloader)</h4>
<p>GRUB - это многостадийный загрузчик, который позволяет:</p>
<ul>
<li>Выбирать операционную систему для загрузки</li>
<li>Передавать параметры ядру при загрузке</li>
<li>Работать с различными файловыми системами</li>
<li>Защищать доступ к настройкам загрузки паролем</li>
</ul>
<h4 style="font-size: 1.6em;">Systemd и юниты</h4>
<p>Systemd - это система инициализации и менеджер служб в современных дистрибутивах Linux. Юниты (units) - это конфигурационные файлы, описывающие:</p>
<ul>
<li>Службы (services)</li>
<li>Точки монтирования (mounts)</li>
<li>Сокеты (sockets)</li>
<li>И другие системные ресурсы</li>
</ul>
</div>
</section>
<section style="margin-bottom: 30px;" id="yui_3_18_1_1_1792327920741_353">
<h3 style="color: #4a6ea9; border-left: 4px solid #4a6ea9; padding-left: 10px; font-size: 1.6em;">📋 Описание практического задания</h3>
<div style="background: #f0f7ff; padding: 15px; border-radius: 5px;" id="yui_3_18_1_1_1792327920741_352">
<ul style="list-style-type: none; padding: 0;" id="yui_3_18_1_1_1792327920741_351">
<li style="margin-bottom: 10px; padding-left: 25px; position: relative;"><span style="position: absolute; left: 0;">⚙️</span> Настройка параметров, передаваемых ядру при загрузке</li>
<li style="margin-bottom: 10px; padding-left: 25px; position: relative;" id="yui_3_18_1_1_1792327920741_350"><span style="position: absolute; left: 0;">🔑</span> Смена паролей и проверка корректности смены</li>
<li style="margin-bottom: 10px; padding-left: 25px; position: relative;"><span style="position: absolute; left: 0;">🛠️</span> Создание сервисной службы</li>
</ul>
</div>
</section>
<section style="margin-bottom: 30px;">
<h3 style="color: #4a6ea9; border-left: 4px solid #4a6ea9; padding-left: 10px; font-size: 1.6em;">🚀 Настройка параметров, смена паролей и проверка корректности его смены</h3>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">1. Настройка параметров загрузки через GRUB</h4>
<p><strong>Теоретическая часть:</strong> Параметры ядра передаются в командной строке и влияют на поведение системы при загрузке. Ключевые параметры включают режим монтирования корневой файловой системы и указание программы, запускаемой с PID=1.</p>
<p>Используя редактор пунктов меню GRUB, настройте параметры, передаваемые ядру при загрузке Astra Linux:</p>
<ul>
<li>Примонтируйте в корневой каталог устройство в режиме <strong>Чтение/Запись</strong></li>
<li>Укажите полный путь к программе <code style="font-family: 'Courier New', monospace;">/bin/bash</code>, выполняемой с PID=1</li>
</ul>
<div style="background: #f8f8f8; padding: 10px; border-radius: 5px; margin: 10px 0;">
<p><strong>Процедура:</strong> Во время загрузки системы при появлении окна меню GRUB нажмите «e», на запрос ввода имени пользователя введите имя администратора системы, при запросе пароля введите пароль GRUB.</p>
</div>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-1.png" alt="Настройка GRUB">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 1. Настройка параметров загрузки в GRUB</p>
</div>
</div>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">2. Смена пароля пользователя</h4>
<p><strong>Теоретическая часть:</strong> Утилита <code style="font-family: 'Courier New', monospace;">passwd</code> используется для изменения паролей пользователей. Она обновляет хэш пароля в файле <code style="font-family: 'Courier New', monospace;">/etc/shadow</code>, обеспечивая безопасное хранение учетных данных.</p>
<p>Смените пароль у пользователя системы, используя утилиту <code style="font-family: 'Courier New', monospace;">passwd</code> (см. рис. 2):</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-2.png" alt="Смена пароля">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 2. Смена пароля пользователя с помощью утилиты passwd</p>
</div>
</div>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">3. Проверка смены пароля</h4>
<p>Проверьте корректность смены пароля: перезагрузите машину и войдите с новым паролем в графическом интерфейсе (для выхода из консоли bash нажмите <code style="font-family: 'Courier New', monospace;">Ctrl+Alt+Del</code>).</p>
</div>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">4. Смена пароля GRUB</h4>
<p><strong>Теоретическая часть:</strong> Защита GRUB паролем предотвращает несанкционированный доступ к параметрам загрузки, что особенно важно для систем с повышенными требованиями безопасности.</p>
<p>Для смены пароля GRUB воспользуйтесь командой <code style="font-family: 'Courier New', monospace;">grub-set-password</code>.</p>
<p>Пересоберите GRUB с помощью <code style="font-family: 'Courier New', monospace;">update-grub</code>. Дополнительные сведения можно получить в <code style="font-family: 'Courier New', monospace;">info grub</code> (см. рис. 3).</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-3.png" alt="Смена пароля GRUB">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 3. Смена пароля GRUB и обновление конфигурации</p>
</div>
</div>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">5. Проверка смены пароля GRUB</h4>
<p>Проверьте корректность смены пароля: перезагрузите машину и войдите с новым паролем в редактор команд GRUB.</p>
</div>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">6. Настройка GRUB-таймаута</h4>
<p><strong>Теоретическая часть:</strong> Таймаут GRUB определяет время ожидания перед автоматической загрузкой системы по умолчанию. Настройка таймаута важна для автоматизации процесса загрузки и повышения безопасности.</p>
<p>Поменяйте GRUB-таймаут на 10 сек с обратным отсчетом времени и без показа меню.</p>
<p>Задание выполните с помощью внесения изменений в файл <code style="font-family: 'Courier New', monospace;">/etc/default/grub</code>, параметры описаны в <code style="font-family: 'Courier New', monospace;">info grub → * Configuration::</code> (см. рис. 4).</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-4.png" alt="Настройка таймаута GRUB">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 4. Настройка параметров таймаута в файле /etc/default/grub</p>
</div>
</div>
<div style="background: #fff9e6; border: 1px solid #e6db55; border-radius: 5px; padding: 15px; margin-bottom: 20px;">
<h4 style="color: #8a6d3b; margin-top: 0; font-size: 1.6em;">⚠️ Важно!</h4>
<p>Не забудьте выполнить команду: <code style="font-family: 'Courier New', monospace;">sudo update-grub</code> (см. рис. 5)</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-5.png" alt="Команда update-grub">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 5. Выполнение команды update-grub для применения изменений</p>
</div>
<p>Перезагрузите систему. Вместо меню grub должен отображаться счётчик секунд (см. рис. 6):</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-6.png" alt="Счётчик GRUB">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 6. Отображение счетчика времени загрузки GRUB</p>
</div>
</div>
</section>
<section style="margin-bottom: 30px;">
<h3 style="color: #4a6ea9; border-left: 4px solid #4a6ea9; padding-left: 10px; font-size: 1.6em;">🛠️ Создание unit</h3>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">1. Создание unit типа service</h4>
<p><strong>Теоретическая часть:</strong> Systemd юниты позволяют автоматизировать запуск и управление системными службами. Юнит типа service описывает как управлять конкретной службой, включая команды запуска, остановки и условия зависимости.</p>
<p>Создайте unit (типа service) для включения маршрутизации в ядре (переменная <code style="font-family: 'Courier New', monospace;">net.ipv4.ip_forward</code>).</p>
<div style="background: #f0f7ff; padding: 15px; border-radius: 5px; margin: 15px 0;">
<h5 style="margin-top: 0; font-size: 1.6em;">Порядок выполнения:</h5>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>1. Создание юнита:</strong></p>
<p>Создайте юнит с именем <code style="font-family: 'Courier New', monospace;">ip_forward.service</code> (см. рис. 7):</p>
<div style="background: #f5f5f5; padding: 10px; border-radius: 3px; font-family: 'Courier New', monospace;">sudo systemctl --force --full edit ip_forward.service</div>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-7.png" alt="Создание юнита">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 7. Создание юнита службы systemd</p>
</div>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>2. Настройка секции [Unit]:</strong></p>
<p>В секции <code style="font-family: 'Courier New', monospace;">[Unit]</code> параметру <code style="font-family: 'Courier New', monospace;">Description</code> присвойте краткое описание:</p>
<div style="background: #f5f5f5; padding: 10px; border-radius: 3px; font-family: 'Courier New', monospace;">Description=Turn on/off internal routing</div>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>3. Настройка секции [Service]:</strong></p>
<p><strong>Теоретическая часть:</strong> Секция [Service] определяет поведение службы. Тип <code style="font-family: 'Courier New', monospace;">oneshot</code> используется для служб, которые выполняют одну операцию и завершаются, а параметр <code style="font-family: 'Courier New', monospace;">RemainAfterExit</code> указывает, что служба считается активной даже после завершения основного процесса.</p>
<ul>
<li>Тип службы: <code style="font-family: 'Courier New', monospace;">Type=oneshot</code></li>
<li>Параметр для сохранения состояния после выполнения: <code style="font-family: 'Courier New', monospace;">RemainAfterExit=yes</code></li>
<li>Команда запуска: <code style="font-family: 'Courier New', monospace;">ExecStart=/usr/sbin/sysctl net.ipv4.ip_forward=1</code></li>
<li>Команда остановки: <code style="font-family: 'Courier New', monospace;">ExecStop=/usr/sbin/sysctl net.ipv4.ip_forward=0</code></li>
</ul>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>4. Настройка секции [Install]:</strong></p>
<p>Задайте многопользовательский режим без графического интерфейса:</p>
<div style="background: #f5f5f5; padding: 10px; border-radius: 3px; font-family: 'Courier New', monospace;">WantedBy=multi-user.target</div>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>5. Сохранение юнита:</strong></p>
<p>Сохраните юнит с параметрами по умолчанию (см. рис. 8):</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-8.png" alt="Сохранение юнита">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 8. Сохранение конфигурации юнита</p>
</div>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>6. Перезагрузка конфигурации:</strong></p>
<p>Перечитайте конфигурационный файл службы:</p>
<div style="background: #f5f5f5; padding: 10px; border-radius: 3px; font-family: 'Courier New', monospace;">sudo systemctl daemon-reload</div>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>7. Запуск и проверка службы:</strong></p>
<p>Запустите созданную службу и проверьте корректность работы (см. рис. 9):</p>
<div style="text-align: center; margin: 20px 0;"><img style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 5px;" src="https://nimnull.ru/img/labs/OnOffAstra/astra-9.png" alt="Проверка службы">
<p style="margin-top: 8px; font-style: italic; color: #666;">Рисунок 9. Проверка состояния созданной службы</p>
</div>
</div>
<div style="background: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
<p><strong>8. Добавление в автозагрузку:</strong></p>
<p>Добавьте службу в автозагрузку:</p>
<div style="background: #f5f5f5; padding: 10px; border-radius: 3px; font-family: 'Courier New', monospace;">sudo systemctl enable ip_forward.service</div>
</div>
</div>
</div>
<div style="background: #fff; border: 1px solid #e1e1e1; border-radius: 5px; padding: 20px;">
<h4 style="color: #2c3e50; margin-top: 0; font-size: 1.6em;">2. Проверка работы службы</h4>
<p>Проверьте корректность работы службы <code style="font-family: 'Courier New', monospace;">ip_forward.service</code> после перезагрузки ОС.</p>
</div>
</section>
<footer style="text-align: center; margin-top: 30px; padding-top: 15px; border-top: 1px solid #e1e1e1; color: #777; font-size: 0.9em;">
<p>Лабораторная работа: "Процесс загрузки и выключения системы"</p>
</footer></div>
</div></div>

Use SKILL.md to do this 

Отдай мне файл .odt 
Пиши в обезличенном формате, вроде того что *открылась консоль*





