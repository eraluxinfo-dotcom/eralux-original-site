# STATUS: FLOATING ICONS READY

Сделано:
- текстовые заглушки TG и VB удалены;
- добавлены локальные SVG-иконки Telegram и Viber;
- hotlink не используется;
- Viber ведёт на https://viber.me/380968074894;
- Telegram отображается как отключённая preview-кнопка, потому что реальная ссылка не предоставлена;
- кнопка «Наверх» использует SVG-стрелку;
- размеры и hover-состояния унифицированы;
- desktop и mobile CSS подготовлены;
- RU / UK / EN пересобраны и проверены;
- live site not changed.

Файлы:
- deploy/prepared_original_site_update/img/icons/telegram.svg
- deploy/prepared_original_site_update/img/icons/viber.svg
- build_eralux_preview.py
- deploy/prepared_original_site_update/css/eralux-update.css
- deploy/prepared_original_site_update/js/eralux-update.js

Примечание:
- Для активации Telegram нужна реальная ссылка пользователя.
- Headless Chrome на узком screenshot не отрисовал fixed-слой, поэтому мобильное положение следует ещё раз визуально проверить в открытом in-app browser.

Живой сайт:
- не изменялся.
