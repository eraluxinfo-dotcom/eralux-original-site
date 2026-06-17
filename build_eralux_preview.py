from pathlib import Path
import json
import re
from html import escape
from PIL import Image, ImageStat

root = Path(r"E:\ERALUX\original-site")
deploy = root / "deploy" / "prepared_original_site_update"
base_html = (root / "backup" / "files_public_2026-06-17_10-31" / "index.html").read_text(encoding="utf-8")
i18n = {
    lang: json.loads((Path(r"E:\ERALUX\site\i18n") / f"{lang}.json").read_text(encoding="utf-8"))
    for lang in ["ru", "uk", "en"]
}

T = {
    "ru": {
        "hero_over": "Монтаж за 1 день | Гарантия 12 лет",
        "hero_title": '<b>Натяжные потолки</b><br>в Одессе и области<br class="hidden-sm"> от 7 у.е./м²',
        "hero_intro": 'Бесплатный замер и аккуратный монтаж<br class="hidden-sm"> для квартиры, дома и бизнеса',
        "phone": "Введите ваш телефон",
        "calc": "Рассчитать стоимость",
        "viber": "Написать в Viber",
        "top": "Наверх",
        "gallery_title": "Каталог работ и решений ERALUX",
        "price_title": "Актуальные цены",
        "details": "Локация: Одесса<br>Площадь: по замеру<br>Фактура: матовая",
        "title": "Натяжные потолки в Одессе и Одесской области | ERALUX",
        "desc": "Натяжные потолки в Одессе и области. Бесплатный замер, монтаж за 1 день, гарантия 12 лет, от 7 у.е./м².",
        "prices": [
            "Теневой потолок от 10 у.е./м²",
            "Парящий потолок от 10 у.е./м²",
            "Световые линии от 35 у.е./м²",
            "Фотопечать от 25 у.е./м²",
            "Apply-потолки от 25 у.е./м²",
            "Звёздное небо от 35 у.е./м²",
            "Карнизы от 25 у.е.",
        ],
        "filters": [
            "Все работы",
            "Световые линии",
            "Теневые потолки",
            "Парящие потолки",
            "Ниша под шторы",
            "Периметральная LED-подсветка",
            "Спальня",
            "Ванная",
            "Коридор",
        ],
        "cards": [
            ("light-lines led", "Геометрические световые линии", "Современное решение для чистого и выразительного интерьера. Световые линии подчёркивают геометрию потолка и помогают создать мягкое, комфортное освещение.", "img/eralux/projects/eralux-project-01.jpg"),
            ("shadow", "Теневой потолок", "Теневой профиль формирует аккуратный контур и визуально отделяет потолок от стен.", "img/eralux/old/old-works-14.jpg"),
            ("floating led", "Парящий потолок с LED-подсветкой", "Мягкая подсветка по периметру делает комнату легче и добавляет глубину интерьеру.", "img/eralux/projects/eralux-project-02.jpg"),
            ("curtain", "Ниша под шторы", "Скрытая ниша помогает спрятать карниз и сохранить чистую линию потолка.", "img/eralux/projects/eralux-project-03.jpg"),
            ("bedroom", "Спальня с матовым потолком", "Матовая фактура и спокойный свет подходит для уютной спальни.", "img/eralux/projects/eralux-project-04.jpg"),
            ("bathroom", "Потолок в ванной", "Практичное решение для влажных помещений с аккуратной геометрией.", "img/eralux/projects/eralux-project-05.jpg"),
        ],
    },
    "uk": {
        "hero_over": "Монтаж за 1 день | Гарантія 12 років",
        "hero_title": '<b>Натяжні стелі</b><br>в Одесі та області<br class="hidden-sm"> від 7 у.е./м²',
        "hero_intro": 'Безкоштовний замір і акуратний монтаж<br class="hidden-sm"> для квартири, будинку та бізнесу',
        "phone": "Введіть ваш телефон",
        "calc": "Розрахувати вартість",
        "viber": "Написати у Viber",
        "top": "Нагору",
        "gallery_title": "Каталог робіт і рішень ERALUX",
        "price_title": "Актуальні ціни",
        "details": "Локація: Одеса<br>Площа: за заміром<br>Фактура: матова",
        "title": "Натяжні стелі в Одесі та області | ERALUX",
        "desc": "Натяжні стелі в Одесі та області. Безкоштовний замір, монтаж за 1 день, гарантія 12 років, від 7 у.е./м².",
        "prices": [
            "Тіньова стеля від 10 у.е./м²",
            "Паряща стеля від 10 у.е./м²",
            "Світлові лінії від 35 у.е./м²",
            "Фотодрук від 25 у.е./м²",
            "Apply-стелі від 25 у.е./м²",
            "Зоряне небо від 35 у.е./м²",
            "Карнизи від 25 у.е.",
        ],
        "filters": [
            "Усі роботи",
            "Світлові лінії",
            "Тіньові стелі",
            "Парящі стелі",
            "Ніша під штори",
            "Периметральне LED-підсвічування",
            "Спальня",
            "Ванна",
            "Коридор",
        ],
        "cards": [
            ("light-lines led", "Геометричні світлові лінії", "Сучасне рішення для чистого та виразного інтер’єру. Світлові лінії підкреслюють геометрію стелі та допомагають створити м’яке комфортне освітлення.", "img/eralux/projects/eralux-project-01.jpg"),
            ("shadow", "Тіньова стеля", "Тіньовий профіль формує акуратний контур і візуально відділяє стелю від стін.", "img/eralux/old/old-works-14.jpg"),
            ("floating led", "Паряща стеля з LED-підсвічуванням", "М’яке підсвічування по периметру робить кімнату легшою та додає інтер’єру глибини.", "img/eralux/projects/eralux-project-02.jpg"),
            ("curtain", "Ніша під штори", "Прихована ніша допомагає сховати карниз і зберегти чисту лінію стелі.", "img/eralux/projects/eralux-project-03.jpg"),
            ("bedroom", "Спальня з матовою стелею", "Матова фактура та спокійне світло пасують для затишної спальні.", "img/eralux/projects/eralux-project-04.jpg"),
            ("bathroom", "Стеля у ванній", "Практичне рішення для вологих приміщень з акуратною геометрією.", "img/eralux/projects/eralux-project-05.jpg"),
        ],
    },
    "en": {
        "hero_over": "Installation in 1 day | 12-year warranty",
        "hero_title": '<b>Stretch ceilings</b><br>in Odesa and Odesa region<br class="hidden-sm"> from 7 USD/m²',
        "hero_intro": 'Free measurement and neat installation<br class="hidden-sm"> for apartments, homes and businesses',
        "phone": "Enter your phone",
        "calc": "Calculate the price",
        "viber": "Write in Viber",
        "top": "Back to top",
        "gallery_title": "ERALUX project gallery",
        "price_title": "Current prices",
        "details": "Location: Odesa<br>Area: measured individually<br>Texture: matte",
        "title": "Stretch ceilings in Odesa and Odesa region | ERALUX",
        "desc": "Stretch ceilings in Odesa and Odesa region. Free measurement, installation in 1 day, 12-year warranty, from 7 USD/m².",
        "prices": [
            "Shadow ceiling from 10 USD/m²",
            "Floating ceiling from 10 USD/m²",
            "Light lines from 35 USD/m²",
            "Photo printing from 25 USD/m²",
            "Apply ceilings from 25 USD/m²",
            "Starry sky from 35 USD/m²",
            "Curtain rails from 25 USD",
        ],
        "filters": [
            "All projects",
            "Light lines",
            "Shadow ceilings",
            "Floating ceilings",
            "Curtain niche",
            "Perimeter LED lighting",
            "Bedroom",
            "Bathroom",
            "Hallway",
        ],
        "cards": [
            ("light-lines led", "Geometric light lines", "A modern solution for a clean and expressive interior. Light lines highlight the ceiling geometry and create soft, comfortable lighting.", "img/eralux/projects/eralux-project-01.jpg"),
            ("shadow", "Shadow ceiling", "A shadow profile creates a clean outline and visually separates the ceiling from the walls.", "img/eralux/old/old-works-14.jpg"),
            ("floating led", "Floating ceiling with LED lighting", "Soft perimeter lighting makes the room feel lighter and adds depth to the interior.", "img/eralux/projects/eralux-project-02.jpg"),
            ("curtain", "Curtain niche", "A hidden curtain niche keeps the rail discreet and preserves a clean ceiling line.", "img/eralux/projects/eralux-project-03.jpg"),
            ("bedroom", "Bedroom with matte ceiling", "Matte texture and calm lighting works well for a comfortable bedroom.", "img/eralux/projects/eralux-project-04.jpg"),
            ("bathroom", "Bathroom ceiling", "A practical ceiling solution for humid rooms with neat geometry.", "img/eralux/projects/eralux-project-05.jpg"),
        ],
    },
}

filter_keys = ["all", "light-lines", "shadow", "floating", "curtain", "led", "bedroom", "bathroom", "hallway"]

palette_meta = {
    "ru": ("Палитра потолков", "Компактный каталог оттенков по номерам", "Цвет и оттенок могут отличаться в зависимости от освещения и настроек экрана. Точный выбор делается по реальным образцам при замере."),
    "uk": ("Палітра стель", "Компактний каталог відтінків за номерами", "Колір і відтінок можуть відрізнятися залежно від освітлення та налаштувань екрана. Точний вибір робиться за реальними зразками під час заміру."),
    "en": ("Ceiling palette", "Compact catalog of shades by number", "Color shades may vary depending on lighting and screen settings. The final choice is made using physical samples during measurement."),
}

palette_descriptions = {
    "ru": [
        "Чистый интерьер.",
        "Мягкая атмосфера.",
        "Современные комнаты.",
        "Акцентное решение.",
        "LED-подсветка.",
        "Спальня и гостиная.",
    ],
    "uk": [
        "Чистий інтер’єр.",
        "М’яка атмосфера.",
        "Сучасні кімнати.",
        "Акцентне рішення.",
        "LED-підсвічування.",
        "Спальня та вітальня.",
    ],
    "en": [
        "Clean interiors.",
        "Soft atmosphere.",
        "Modern rooms.",
        "Accent solution.",
        "LED lighting.",
        "Bedroom and living room.",
    ],
}

palette_sources = [
    ("1", "img/colors/1.jpg", ["420", "753", "739", "733", "717", "713", "721", "707", "507", "666", "644", "624", "652", "628", "608"]),
    ("2", "img/colors/2.jpg", ["235", "231", "227", "229", "225", "233", "162", "160", "156", "140", "120", "114", "104", "100", "604", "205", "201", "110", "333", "319", "313", "317", "311", "309", "305", "303"]),
    ("3", "img/colors/3.jpg", ["82", "94", "95"]),
    ("4", "img/colors/4.jpg", ["303", "501", "307", "507", "511", "404", "504", "602", "652", "305", "313", "347", "110"]),
    ("5", "img/colors/5.jpg", ["303", "501", "225", "402", "114", "162", "347"]),
    ("6", "img/colors/6.jpg", ["347", "478", "476", "866", "466", "462", "444", "442", "416", "402", "412", "400", "404", "501", "307", "577", "490", "571", "555", "547", "573", "525", "545", "410", "424", "408", "406", "511", "519", "515"]),
]


def clamp_channel(value: float) -> int:
    return max(0, min(255, int(round(value))))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def adjust_rgb(rgb: tuple[int, int, int], factor: float, offset: int = 0) -> tuple[int, int, int]:
    return tuple(clamp_channel(channel * factor + offset) for channel in rgb)


def swatch_color(number: str) -> dict[str, str]:
    path = root / "processed-images" / "palette-swatches" / f"palette-{number}.jpg"
    if not path.exists():
        return {
            "base": "#c8c3b8",
            "shadow": "#8f887c",
            "highlight": "#f8f4eb",
            "finish": "matte",
        }
    with Image.open(path) as image:
        image = image.convert("RGB").resize((1, 1), Image.Resampling.LANCZOS)
        rgb = tuple(int(v) for v in ImageStat.Stat(image).mean[:3])
    maximum = max(rgb)
    minimum = min(rgb)
    saturation = 0 if maximum == 0 else (maximum - minimum) / maximum
    brightness = sum(rgb) / 3
    finish = "glossy" if saturation > 0.22 or brightness < 120 else "matte"
    return {
        "base": rgb_to_hex(rgb),
        "shadow": rgb_to_hex(adjust_rgb(rgb, 0.68)),
        "highlight": rgb_to_hex(adjust_rgb(rgb, 0.55, 112)),
        "finish": finish,
    }


palette_cards = []
seen_palette_numbers = set()
for source_number, source_image, visible_numbers in palette_sources:
    for visible_number in visible_numbers:
        if visible_number in seen_palette_numbers:
            continue
        seen_palette_numbers.add(visible_number)
        palette_cards.append(
            {
                "number": visible_number,
                "image": f"img/eralux/palette-swatches/palette-{visible_number}.jpg",
                "source": source_image,
                "source_number": source_number,
                **swatch_color(visible_number),
            }
        )

benefits_content = {
    "ru": {
        "title": "Наши преимущества",
        "subtitle": "Работаем аккуратно, быстро и с гарантией 12 лет",
        "items": [
            ("shield", "12 лет гарантии", "Качественные материалы и ответственность за монтаж."),
            ("ruler", "Бесплатный замер", "Мастер приедет, сделает точные замеры и подготовит расчёт."),
            ("tools", "Монтаж за 1 день", "Большинство стандартных потолков устанавливаем в течение одного дня."),
            ("sparkle", "Аккуратная работа", "Работаем чисто, внимательно к деталям и без лишнего беспорядка."),
            ("lamp", "Современные решения", "Световые линии, теневой профиль, ниши под шторы и LED-подсветка."),
            ("pin", "Одесса и область", "Выезжаем на объекты по Одессе и Одесской области."),
        ],
    },
    "uk": {
        "title": "Наші переваги",
        "subtitle": "Працюємо акуратно, швидко та з гарантією 12 років",
        "items": [
            ("shield", "12 років гарантії", "Якісні матеріали та відповідальність за монтаж."),
            ("ruler", "Безкоштовний замір", "Майстер приїде, зробить точні виміри та підготує розрахунок."),
            ("tools", "Монтаж за 1 день", "Більшість стандартних стель встановлюємо протягом одного дня."),
            ("sparkle", "Акуратна робота", "Працюємо чисто, уважно до деталей і без зайвого безладу."),
            ("lamp", "Сучасні рішення", "Світлові лінії, тіньовий профіль, ніші під штори та LED-підсвічування."),
            ("pin", "Одеса та область", "Виїжджаємо на об’єкти по Одесі та Одеській області."),
        ],
    },
    "en": {
        "title": "Our advantages",
        "subtitle": "Careful work, fast installation and a 12-year warranty",
        "items": [
            ("shield", "12-year warranty", "Quality materials and responsibility for the installation."),
            ("ruler", "Free measurement", "A specialist visits, takes accurate measurements and prepares an estimate."),
            ("tools", "Installation in 1 day", "Most standard ceilings are installed within one working day."),
            ("sparkle", "Neat work", "Clean installation, attention to detail and no unnecessary mess."),
            ("lamp", "Modern solutions", "Light lines, shadow profiles, curtain niches and LED lighting."),
            ("pin", "Odesa region", "We work across Odesa and the Odesa region."),
        ],
    },
}

about_content = {
    "ru": {
        "title": "ERALUX для современных интерьеров",
        "text": "Подбираем натяжной потолок под планировку, свет и стиль помещения. Работаем с матовыми фактурами, световыми линиями, теневым профилем, нишами под шторы и LED-подсветкой.",
        "cta_title": "Запишитесь на замер",
        "cta_text": "Оставьте телефон, и мастер уточнит детали проекта.",
        "name": "Ваше имя",
        "phone": "Введите ваш номер*",
        "button": "Заказать замер",
    },
    "uk": {
        "title": "ERALUX для сучасних інтер’єрів",
        "text": "Підбираємо натяжну стелю під планування, світло та стиль приміщення. Працюємо з матовими фактурами, світловими лініями, тіньовим профілем, нішами під штори та LED-підсвічуванням.",
        "cta_title": "Запишіться на замір",
        "cta_text": "Залиште телефон, і майстер уточнить деталі проєкту.",
        "name": "Ваше ім’я",
        "phone": "Введіть ваш номер*",
        "button": "Замовити замір",
    },
    "en": {
        "title": "ERALUX for modern interiors",
        "text": "We match stretch ceilings to the room layout, lighting and interior style. Matte textures, light lines, shadow profiles, curtain niches and LED lighting are available.",
        "cta_title": "Request a measurement",
        "cta_text": "Leave your phone number and a specialist will clarify the project details.",
        "name": "Your name",
        "phone": "Enter your phone*",
        "button": "Request a measurement",
    },
}

icon_paths = {
    "shield": '<path d="M12 3l7 3v5c0 4.4-2.8 8.4-7 10-4.2-1.6-7-5.6-7-10V6l7-3z"/><path d="M9 12l2 2 4-5"/>',
    "ruler": '<path d="M4 17L17 4l3 3L7 20l-3-3z"/><path d="M14 7l3 3"/><path d="M11 10l2 2"/><path d="M8 13l3 3"/>',
    "tools": '<path d="M14.7 6.3a4 4 0 0 0-5 5L4 17l3 3 5.7-5.7a4 4 0 0 0 5-5l-2.9 2.9-3-3 2.9-2.9z"/>',
    "sparkle": '<path d="M12 3l1.4 4.4L18 9l-4.6 1.6L12 15l-1.4-4.4L6 9l4.6-1.6L12 3z"/><path d="M19 14l.8 2.2L22 17l-2.2.8L19 20l-.8-2.2L16 17l2.2-.8L19 14z"/>',
    "lamp": '<path d="M8 2h8l2 9H6l2-9z"/><path d="M12 11v8"/><path d="M9 22h6"/><path d="M10 19h4"/>',
    "pin": '<path d="M12 21s7-5.2 7-12a7 7 0 0 0-14 0c0 6.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
}


def gallery(lang: str) -> str:
    d = T[lang]
    buttons = "".join(
        f'<button type="button" data-filter="{key}" class="{"is-active" if key == "all" else ""}">{label}</button>'
        for key, label in zip(filter_keys, d["filters"])
    )
    cards = []
    for cat, title, desc, img in d["cards"]:
        cards.append(
            f'<a href="/{img}" data-fancybox class="case b-card portfolio__item portfolio__item_slide swiper-slide" data-cat="{cat}">'
            f'<img data-src="/{img}" alt="{title}" class="case__img lazyloaded" src="/{img}">'
            f'<p class="card-title case__title">{title}</p><hr class="line line_small case__line">'
            f'<div class="case__totals"><p class="case__info text">{d["details"]}</p></div>'
            f'<div class="case__overlay"><h3>{title}</h3><p>{desc}</p>'
            f'<div class="case__overlay-actions"><a href="#callback">{i18n[lang]["learnPrice"]}</a>'
            f'<a href="https://viber.me/380968074894">{d["viber"]}</a></div></div></a>'
        )
    return (
        f'<div class="portfolio__filters">{buttons}</div>'
        '<div class="portfolio__wrapper"><div class="portfolio__content swiper-container">'
        f'<div class="portfolio__slider swiper-wrapper">{"".join(cards)}</div></div></div>'
    )


def palette(lang: str) -> str:
    title, subtitle, disclaimer = palette_meta[lang]
    cards = []
    descriptions = palette_descriptions[lang]
    measure_label = {"ru": "Заказать замер", "uk": "Замовити замір", "en": "Request a measurement"}[lang]
    close_label = {"ru": "Закрыть", "uk": "Закрити", "en": "Close"}[lang]
    for index, item in enumerate(palette_cards):
        number = item["number"]
        description = descriptions[index % len(descriptions)]
        base = item["base"]
        shadow = item["shadow"]
        highlight = item["highlight"]
        finish = item["finish"]
        finish_label = {"ru": "глянец" if finish == "glossy" else "мат", "uk": "глянець" if finish == "glossy" else "мат", "en": "glossy" if finish == "glossy" else "matte"}[lang]
        style = f"--swatch-base:{base};--swatch-shadow:{shadow};--swatch-highlight:{highlight};"
        cards.append(
            f'<article class="eralux-palette-card palette-card--{finish}" style="{style}" '
            f'data-palette-number="№ {number}" data-palette-description="{escape(description, quote=True)}" '
            f'data-palette-base="{base}" data-palette-shadow="{shadow}" data-palette-highlight="{highlight}" data-palette-finish="{finish}" data-palette-finish-label="{finish_label}">'
            '<button class="palette-swatch" type="button" aria-label="palette sample">'
            '<span class="palette-swatch-surface"></span>'
            f'<span class="palette-finish-badge">{finish_label}</span>'
            "</button>"
            '<div class="palette-card-body">'
            f'<span class="palette-number">№ {number}</span>'
            f'<span class="palette-description">{description}</span>'
            "</div>"
            "</article>"
        )
    return (
        '<section class="eralux-palette wrapper section" id="palette">'
        f'<div class="eralux-palette__head"><h2 class="title-dec">{title}</h2><p>{subtitle}</p></div>'
        f'<div class="eralux-palette__grid">{"".join(cards)}</div>'
        f'<p class="eralux-palette__note">{disclaimer}</p>'
        f'<div class="eralux-palette__actions"><a href="#callback">{measure_label}</a><a href="https://viber.me/380968074894">Viber</a></div>'
        '<div class="palette-modal" aria-hidden="true">'
        '<div class="palette-modal__backdrop" data-palette-close></div>'
        '<div class="palette-modal__dialog" role="dialog" aria-modal="true">'
        f'<button class="palette-modal__close" type="button" data-palette-close aria-label="{close_label}">×</button>'
        '<div class="palette-modal__swatch"><span class="palette-swatch-surface"></span><span class="palette-finish-badge"></span></div>'
        '<div class="palette-modal__body"><strong class="palette-modal__number"></strong><p class="palette-modal__description"></p>'
        f'<div class="palette-modal__actions"><a href="#callback">{measure_label}</a><a href="https://viber.me/380968074894">Viber</a></div></div>'
        '</div></div>'
        "</section>"
    )


def benefits(lang: str) -> str:
    data = benefits_content[lang]
    cards = []
    for icon, title, text in data["items"]:
        cards.append(
            '<article class="benefit-card">'
            f'<span class="benefit-card__icon"><svg viewBox="0 0 24 24" aria-hidden="true">{icon_paths[icon]}</svg></span>'
            f"<h3>{title}</h3><p>{text}</p>"
            "</article>"
        )
    return (
        '<section class="benefits-section wrapper section" id="benefits">'
        f'<div class="benefits-section__head"><h2 class="title-dec">{data["title"]}</h2><p>{data["subtitle"]}</p></div>'
        f'<div class="benefits-grid">{"".join(cards)}</div>'
        "</section>"
    )


def about(lang: str) -> str:
    data = about_content[lang]
    return (
        '<section class="eralux-about wrapper section">'
        f'<div><h2 class="title-dec">{data["title"]}</h2><p>{data["text"]}</p></div>'
        "</section>"
    )


def cta(lang: str) -> str:
    data = about_content[lang]
    return (
        '<section class="eralux-cta">'
        '<div class="container eralux-cta__content">'
        f'<div><h2>{data["cta_title"]}</h2><p>{data["cta_text"]}</p></div>'
        '<form class="form js-less eralux-cta__form" action="javascript:void(0);" method="POST">'
        f'<input class="input form__input form__input_horiz" type="text" name="name" required placeholder="{data["name"]}">'
        f'<input class="input form__input form__input_horiz" type="tel" name="phone" required placeholder="{data["phone"]}">'
        f'<button class="button form__button btn-4">{data["button"]}</button>'
        "</form></div></section>"
    )


def page(lang: str) -> str:
    s = base_html
    d = T[lang]
    path = "" if lang == "ru" else f"{lang}/"
    s = re.sub(r'<html lang="[^"]+"', f'<html lang="{lang}"', s, count=1)
    s = re.sub(r"<title>.*?</title>", f"<title>{d['title']}</title>", s, count=1, flags=re.S)
    s = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{d["desc"]}">',
        s,
        count=1,
        flags=re.S,
    )
    seo = (
        '<link rel="stylesheet" href="/css/app.css?v2">\n'
        '    <link rel="stylesheet" href="/css/eralux-update.css">\n'
        f'    <link rel="canonical" href="https://eralux.od.ua/{path}">\n'
        '    <link rel="alternate" hreflang="ru-UA" href="https://eralux.od.ua/">\n'
        '    <link rel="alternate" hreflang="uk-UA" href="https://eralux.od.ua/uk/">\n'
        '    <link rel="alternate" hreflang="en" href="https://eralux.od.ua/en/">'
    )
    s = s.replace('<link rel="stylesheet" href="css/app.css?v2">', seo)
    s = re.sub(r'(href|src|data-src)="(css|js|img)/', r'\1="/\2/', s)
    replacements = [
        (r'<p class="hero__overtitle">.*?</p>', f'<p class="hero__overtitle">{d["hero_over"]}</p>'),
        (r'<h1 class="hero__title">.*?</h1>', f'<h1 class="hero__title">{d["hero_title"]}</h1>'),
        (r'<p class="hero__intro">.*?</p>', f'<p class="hero__intro">{d["hero_intro"]}</p>'),
        (r'placeholder="[^"]+" class="inputN', f'placeholder="{d["phone"]}" class="inputN'),
        (r'<button type="submit" class="buttonN buttonN-red btn-pulse">.*?</button>', f'<button type="submit" class="buttonN buttonN-red btn-pulse">{i18n[lang]["orderMeasure"]}</button>'),
        (r'<p class="calc__total"><span>195</span>.*?</p>', f'<p class="calc__total"><span>7</span> {"USD/m²" if lang == "en" else "у.е./м²"}</p>'),
        (r'<a href="#" class="calc__callback buttonN buttonN-red btn-4 to-form">.*?</a>', f'<a href="#callback" class="calc__callback buttonN buttonN-red btn-4 to-form">{d["calc"]}</a>'),
    ]
    for pattern, value in replacements:
        s = re.sub(pattern, value, s, count=1, flags=re.S)
    price_section = f'<section class="wrapper section"><h2 class="title-dec">{d["price_title"]}</h2><p>{"<br>".join(d["prices"])}</p></section>'
    start = s.find('<div class="portfolio portfolioN portfolio_main portfolio_ceilings new_catalog">')
    nxt = s.find('<div class="portfolio portfolioN portfolio_main portfolio_ceilings new_portfolio"', start)
    if start != -1 and nxt != -1:
        s = (
            s[:start]
            + f'<div class="portfolio portfolioN portfolio_main portfolio_ceilings new_catalog"><h2 class="title-dec">{d["gallery_title"]}</h2>{gallery(lang)}</div>\n\t\t{price_section}\n\t\t'
            + s[nxt:]
        )
    palette_start = s.find('<div class="portfolio portfolioN portfolio_main portfolio_ceilings new_colors">')
    palette_end = s.find('<div class="other', palette_start)
    if palette_start != -1 and palette_end != -1:
        s = s[:palette_start] + palette(lang) + "\n\t\t" + s[palette_end:]
    benefits_start = s.find('<h2 class="title-dec" style="text-align: center; margin-top: 50px;">')
    benefits_end = s.find('<div class="seo-block seo-block_main">', benefits_start)
    if benefits_start != -1 and benefits_end != -1:
        s = s[:benefits_start] + benefits(lang) + "\n\t\t" + s[benefits_end:]
    seo_start = s.find('<div class="seo-block seo-block_main">')
    footer_offer_start = s.find('<div class="footer-offer">', seo_start)
    if seo_start != -1 and footer_offer_start != -1:
        s = s[:seo_start] + about(lang) + "\n\t\t" + s[footer_offer_start:]
    footer_offer_start = s.find('<div class="footer-offer">')
    footer_start = s.find("<footer", footer_offer_start)
    if footer_offer_start != -1 and footer_start != -1:
        s = s[:footer_offer_start] + cta(lang) + "\n\t\t" + s[footer_start:]
    switch = (
        '<nav class="lang-switcher" aria-label="Language">'
        f'<a class="{"is-active" if lang == "ru" else ""}" href="/">RU</a>'
        f'<a class="{"is-active" if lang == "uk" else ""}" href="/uk/">UA</a>'
        f'<a class="{"is-active" if lang == "en" else ""}" href="/en/">EN</a>'
        "</nav>"
    )
    s = s.replace(
        "</div>\n\t\t</div>\n\t</div>\n\n\t<div class=\"main\">",
        switch + "</div>\n\t\t</div>\n\t</div>\n\n\t<div class=\"main\">",
        1,
    )
    floating = (
        f'<div class="eralux-floating"><a class="eralux-floating__btn eralux-floating__btn_tg" href="#" aria-label="Telegram" data-disabled="true">TG</a>'
        f'<a class="eralux-floating__btn eralux-floating__btn_viber" href="https://viber.me/380968074894" aria-label="{d["viber"]}">VB</a>'
        f'<button class="eralux-floating__btn eralux-floating__top" type="button" aria-label="{d["top"]}">↑</button></div>\n'
        '<script src="/js/eralux-update.js?v=rendered-swatch-1"></script>\n'
    )
    return s.replace("</body>", floating + "</body>")


for lang in ["ru", "uk", "en"]:
    destinations = [deploy / lang / "index.html"]
    if lang == "ru":
        destinations.append(deploy / "index.html")
    for dest in destinations:
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(page(lang), encoding="utf-8")

generated_pages = {
    "ru": deploy / "ru" / "index.html",
    "root": deploy / "index.html",
    "uk": deploy / "uk" / "index.html",
    "en": deploy / "en" / "index.html",
}

forbidden_sequences = [
    "?" * 4,
    bytes.fromhex("d0a0d19c").decode("utf-8"),
    bytes.fromhex("d0a0d19f").decode("utf-8"),
    bytes.fromhex("d0a0c2b0").decode("utf-8"),
    bytes.fromhex("c390").decode("utf-8"),
    bytes.fromhex("c391").decode("utf-8"),
    "\ufffd",
]
required_phrases = {
    "ru": [
        "Натяжные потолки",
        "Бесплатный замер",
        "Гарантия 12 лет",
        "Написать в Viber",
        "Теневой потолок",
        "Световые линии",
    ],
    "uk": [
        "Натяжні стелі",
        "Безкоштовний замір",
        "Гарантія 12 років",
        "Написати у Viber",
        "Тіньова стеля",
        "Світлові лінії",
    ],
    "en": [
        "Stretch ceilings",
        "Free measurement",
        "12-year warranty",
        "Write in Viber",
    ],
}

errors = []
for lang, page_path in generated_pages.items():
    html = page_path.read_text(encoding="utf-8")
    lowered = html.lower()
    if '<meta charset="utf-8">' not in lowered:
        errors.append(f"{page_path}: missing <meta charset=\"utf-8\">")
    for bad in forbidden_sequences:
        if bad in html:
            line_no = html[: html.find(bad)].count("\n") + 1
            errors.append(f"{page_path}:{line_no}: forbidden sequence {bad!r}")
    phrase_lang = "ru" if lang == "root" else lang
    for phrase in required_phrases[phrase_lang]:
        if phrase not in html:
            errors.append(f"{page_path}: missing required phrase {phrase!r}")

if errors:
    raise SystemExit("Preview encoding validation failed:\n" + "\n".join(errors))

for lang, page_path in generated_pages.items():
    title = re.search(r"<title>(.*?)</title>", page_path.read_text(encoding="utf-8"), re.S)
    print(lang, "OK", title.group(1) if title else "NO TITLE")
