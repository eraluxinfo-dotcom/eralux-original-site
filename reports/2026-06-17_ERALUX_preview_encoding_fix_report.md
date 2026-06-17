STATUS: PREVIEW ENCODING FIXED

Дата проверки: 2026-06-17

Живой сайт не изменялся. Ничего на https://eralux.od.ua/ не публиковалось.

Проверено:
- http://127.0.0.1:4177/uk/
- http://127.0.0.1:4177/ru/
- http://127.0.0.1:4177/en/
- HTML charset UTF-8
- no ????
- no mojibake
- title нормальный
- украинский текст нормальный
- русский текст нормальный
- английский текст нормальный

Что исправлено:
- Генератор preview перенесён в рабочую папку E:\ERALUX\original-site\build_eralux_preview.py.
- В build_eralux_preview.py все чтения и записи выполняются с encoding="utf-8".
- Кириллица больше не передаётся в генератор через PowerShell-строки.
- В build_eralux_preview.py добавлена встроенная проверка generated HTML на UTF-8 charset, запрещённые broken-последовательности и обязательные фразы для RU/UK/EN.
- Добавлена отдельная preview-страница /ru/ вместе с корневой русской версией.
- Исправлен ACCESS_NOTE.md внутри deploy-пакета, который ранее был повреждён PowerShell-кодировкой.

Автоматическая проверка:
- build_eralux_preview.py выполнен успешно.
- Независимый UTF-8 scan проверил 23 текстовых файла.
- Запрещённые broken-последовательности не найдены.
- Все generated HTML страницы содержат <meta charset="utf-8">.

Браузерная проверка:
- UK: найдены Натяжні стелі, Безкоштовний замір, Гарантія 12 років, Написати у Viber, Тіньова стеля, Світлові лінії.
- RU: найдены Натяжные потолки, Бесплатный замер, Гарантия 12 лет, Написать в Viber, Теневой потолок, Световые линии.
- EN: найдены Stretch ceilings, Free measurement, 12-year warranty, Write in Viber.
- Broken-последовательности в видимом тексте браузера не найдены.

Скриншоты:
- E:\ERALUX\original-site\screenshots\uk-home-fixed.png
- E:\ERALUX\original-site\screenshots\ru-home-fixed.png
- E:\ERALUX\original-site\screenshots\en-home-fixed.png

Файлы изменены:
- E:\ERALUX\original-site\build_eralux_preview.py
- E:\ERALUX\original-site\deploy\prepared_original_site_update\index.html
- E:\ERALUX\original-site\deploy\prepared_original_site_update\ru\index.html
- E:\ERALUX\original-site\deploy\prepared_original_site_update\uk\index.html
- E:\ERALUX\original-site\deploy\prepared_original_site_update\en\index.html
- E:\ERALUX\original-site\deploy\prepared_original_site_update\ACCESS_NOTE.md
- E:\ERALUX\original-site\reports\2026-06-17_ERALUX_preview_encoding_fix_report.md

Git:
- E:\ERALUX\original-site не является Git-репозиторием.
- E:\ERALUX не является Git-репозиторием.
- Commit и push не выполнены, потому что Git не подключён.

Важно:
- Живой сайт не публиковать без отдельного подтверждения пользователя.
- Ничего на eralux.od.ua не менять без отдельного подтверждения.
