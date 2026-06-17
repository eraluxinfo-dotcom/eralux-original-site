STATUS: ORIGINAL SITE STRUCTURE AUDITED

Дата: 2026-06-17

Живой сайт:
- https://eralux.od.ua/
- Не изменялся.
- Ничего не публиковалось.

Backup:
- Создана публичная локальная копия доступных файлов: E:\ERALUX\original-site\backup\files_2026-06-17_10-55
- Это не FTP-полный backup, а копия из ранее скачанного публичного mirror.
- FTP backup и database export не выполнены, потому что в рабочей папке нет приватных FTP/hosting/phpMyAdmin доступов.
- База данных не найдена в публичной структуре. Если хостинг даст phpMyAdmin/панель, экспорт нужно сделать отдельно.

CMS / движок:
- По публичной структуре сайт выглядит как статический HTML-лендинг.
- Признаки Joomla не обнаружены в публичной проверке:
  - /administrator/ возвращал 404
  - /configuration.php возвращал 404
  - /components/ возвращал 404
  - /modules/ возвращал 404
  - /plugins/ возвращал 404
  - /templates/ возвращал 404
- Признаки WordPress также не обнаружены:
  - /wp-admin/ возвращал 404
  - /wp-content/ возвращал 404

Структура:
- Главная страница: index.html
- CSS: css/app.css, css/ion.rangeSlider.min.css, css/swiper-bundle.min.css, css/jquery.fancybox.min.css
- JS: js/script.js, js/jquery-3.6.0.min.js, js/ion.rangeSlider.min.js, js/swiper-bundle.min.js, js/jquery.fancybox.min.js, js/jquery.maskedinput.min.js
- Изображения: img/
- Каталог потолков: img/katalog/
- Галерея работ: img/works/ и img/works1/
- Палитра: img/colors/1.jpg ... img/colors/6.jpg

Блоки:
- Главный hero находится в index.html в блоке .hero.
- Каталог находится в блоке .new_catalog.
- Примеры работ находятся в блоке .new_portfolio и .new_portfolio1.
- Палитра находится в блоке .new_colors.
- Форма/калькулятор находятся в index.html и используют существующие JS/CSS библиотеки.

Языки:
- Оригинальный сайт публично выглядит одноязычным.
- Безопасный preview-вариант добавляет отдельные папки:
  - /
  - /ru/
  - /uk/
  - /en/
- Для публикации можно добавить /uk/ и /en/ как отдельные статические папки без замены оригинального сайта.
- Редиректы на живом сайте не делать без отдельного подтверждения.

Риск:
- До публикации нужен настоящий FTP/hosting backup и проверка того, что на сервере нет скрытых обработчиков форм или backend-файлов, не видимых из публичного mirror.
