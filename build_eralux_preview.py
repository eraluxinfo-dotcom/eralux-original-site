from pathlib import Path
import colorsys
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

price_content = {
    "ru": {
        "title": "Актуальные цены",
        "subtitle": "Ориентировочная стоимость. Точная цена рассчитывается после замера.",
        "note": "Цены ориентировочные. Финальная стоимость зависит от площади, количества углов, выбранного полотна, освещения и сложности монтажа.",
        "items": [
            ("Теневой потолок", "от 10 у.е./м²", "Чистый контур без видимого декоративного багета."),
            ("Парящий потолок", "от 10 у.е./м²", "Мягкая подсветка по периметру и эффект лёгкости."),
            ("Световые линии", "от 35 у.е./м²", "Геометрия света для современных интерьеров."),
            ("Фотопечать", "от 25 у.е./м²", "Индивидуальное изображение на полотне."),
            ("Apply-потолки", "от 25 у.е./м²", "Сложные декоративные решения и комбинации фактур."),
            ("Звёздное небо", "от 35 у.е./м²", "Атмосферный световой сценарий для комнаты."),
            ("Карнизы", "от 25 у.е.", "Аккуратные решения для штор и ниш."),
        ],
    },
    "uk": {
        "title": "Актуальні ціни",
        "subtitle": "Орієнтовна вартість. Точна ціна розраховується після заміру.",
        "note": "Ціни орієнтовні. Фінальна вартість залежить від площі, кількості кутів, обраного полотна, освітлення та складності монтажу.",
        "items": [
            ("Тіньова стеля", "від 10 у.е./м²", "Чистий контур без видимого декоративного багета."),
            ("Паряща стеля", "від 10 у.е./м²", "М’яке підсвічування по периметру та ефект легкості."),
            ("Світлові лінії", "від 35 у.е./м²", "Геометрія світла для сучасних інтер’єрів."),
            ("Фотодрук", "від 25 у.е./м²", "Індивідуальне зображення на полотні."),
            ("Apply-стелі", "від 25 у.е./м²", "Складні декоративні рішення та комбінації фактур."),
            ("Зоряне небо", "від 35 у.е./м²", "Атмосферний світловий сценарій для кімнати."),
            ("Карнизи", "від 25 у.е.", "Акуратні рішення для штор і ніш."),
        ],
    },
    "en": {
        "title": "Current prices",
        "subtitle": "Estimated pricing. The final price is calculated after measurement.",
        "note": "Prices are approximate. The final cost depends on area, number of corners, selected material, lighting and installation complexity.",
        "items": [
            ("Shadow ceiling", "from 10 USD/m²", "A clean perimeter without a visible decorative trim."),
            ("Floating ceiling", "from 10 USD/m²", "Soft perimeter lighting and a light floating effect."),
            ("Light lines", "from 35 USD/m²", "Light geometry for modern interiors."),
            ("Photo printing", "from 25 USD/m²", "A custom image printed on the ceiling material."),
            ("Apply ceilings", "from 25 USD/m²", "Decorative solutions with combined textures."),
            ("Starry sky", "from 35 USD/m²", "Atmospheric lighting for a room."),
            ("Curtain rails", "from 25 USD", "Neat solutions for curtains and niches."),
        ],
    },
}

price_content = {
    "ru": {
        "title": "Актуальные цены",
        "subtitle": "Ориентировочная стоимость. Точная цена рассчитывается после замера.",
        "note": "Цены ориентировочные. Финальная стоимость зависит от площади, количества углов, выбранного полотна, освещения и сложности монтажа.",
        "items": [
            ("Теневой потолок", "от 10 у.е./м²", "Теневой потолок создает тонкий аккуратный зазор между стеной и полотном, поэтому интерьер выглядит современно и собранно. Такая техника хорошо подходит для минималистичных комнат, где не хочется видеть декоративный багет. Контур подчеркивает геометрию помещения и делает переход от стены к потолку визуально легче. В дизайне это решение выглядит спокойно, дорого и очень чисто."),
            ("Парящий потолок", "от 10 у.е./м²", "Парящий потолок строится на специальном профиле с мягкой LED-подсветкой по периметру. Свет отделяет потолок от стен и создает эффект легкости, будто полотно немного поднято в воздух. Такой прием особенно красиво работает вечером, когда основное освещение можно приглушить. В интерьере он добавляет глубину, уют и ощущение современной архитектуры."),
            ("Световые линии", "от 35 у.е./м²", "Световые линии встраиваются в потолок как ровные световые акценты и помогают задать ритм всему помещению. Их можно делать прямыми, геометричными или более сложными под планировку комнаты. Техника требует точной подготовки профиля и аккуратного монтажа, чтобы линии выглядели идеально ровно. В дизайне это один из самых выразительных способов заменить обычную люстру и сделать интерьер современным."),
            ("Фотопечать", "от 25 у.е./м²", "Фотопечать позволяет перенести на потолок изображение, узор или мягкий декоративный мотив. Важно подобрать картинку так, чтобы она не перегружала комнату и сочеталась с мебелью, стенами и светом. Техника хорошо подходит для детских, тематических зон, коммерческих помещений и акцентных интерьеров. При правильном выборе изображение выглядит не случайным декором, а частью общей идеи комнаты."),
            ("Apply-стели", "от 25 у.е./м²", "Apply-стели позволяют сочетать несколько фактур, уровней и декоративных элементов в одном решении. Такая техника подходит, когда хочется сделать потолок более выразительным, но сохранить аккуратность. Комбинация матовых, глянцевых и световых деталей помогает выделить зоны и добавить интерьеру глубину. В дизайне это вариант для тех, кто хочет индивидуальный потолок без ощущения перегруза."),
            ("Звездное небо", "от 35 у.е./м²", "Звездное небо создает мягкий световой сценарий с точками света, которые напоминают ночное небо. Техника может использовать оптоволокно или специальные световые элементы, в зависимости от желаемого эффекта. Такое решение особенно хорошо подходит для спален, детских и зон отдыха. В дизайне оно добавляет атмосферу, спокойствие и ощущение личного пространства."),
            ("Карнизы", "от 25 у.е.", "Скрытые карнизы помогают спрятать крепление штор и оставить линию потолка чистой. Ниша рассчитывается заранее, чтобы ткань красиво выходила из потолка и не спорила с интерьером. Такая техника визуально увеличивает высоту помещения и делает окно более аккуратным. В дизайне это небольшая деталь, которая сильно влияет на ощущение завершенности комнаты."),
        ],
    },
    "uk": {
        "title": "Актуальні ціни",
        "subtitle": "Орієнтовна вартість. Точна ціна розраховується після заміру.",
        "note": "Ціни орієнтовні. Фінальна вартість залежить від площі, кількості кутів, обраного полотна, освітлення та складності монтажу.",
        "items": [
            ("Тіньова стеля", "від 10 у.е./м²", "Тіньова стеля створює тонкий акуратний зазор між стіною та полотном, тому інтер’єр виглядає сучасно й зібрано. Така техніка добре підходить для мінімалістичних кімнат, де не хочеться бачити декоративний багет. Контур підкреслює геометрію приміщення та робить перехід від стіни до стелі візуально легшим. У дизайні це рішення виглядає спокійно, дорого й дуже чисто."),
            ("Паряща стеля", "від 10 у.е./м²", "Паряща стеля будується на спеціальному профілі з м’якою LED-підсвіткою по периметру. Світло відділяє стелю від стін і створює ефект легкості, ніби полотно трохи підняте в повітря. Такий прийом особливо красиво працює ввечері, коли основне освітлення можна приглушити. В інтер’єрі він додає глибину, затишок і відчуття сучасної архітектури."),
            ("Світлові лінії", "від 35 у.е./м²", "Світлові лінії вбудовуються у стелю як рівні світлові акценти й допомагають задати ритм усьому приміщенню. Їх можна робити прямими, геометричними або складнішими під планування кімнати. Техніка потребує точної підготовки профілю та акуратного монтажу, щоб лінії виглядали ідеально рівно. У дизайні це один із найвиразніших способів замінити звичайну люстру й зробити інтер’єр сучасним."),
            ("Фотодрук", "від 25 у.е./м²", "Фотодрук дозволяє перенести на стелю зображення, візерунок або м’який декоративний мотив. Важливо підібрати картинку так, щоб вона не перевантажувала кімнату й поєднувалася з меблями, стінами та світлом. Техніка добре підходить для дитячих, тематичних зон, комерційних приміщень і акцентних інтер’єрів. За правильного вибору зображення виглядає не випадковим декором, а частиною загальної ідеї кімнати."),
            ("Apply-стелі", "від 25 у.е./м²", "Apply-стелі дозволяють поєднувати кілька фактур, рівнів і декоративних елементів в одному рішенні. Така техніка підходить, коли хочеться зробити стелю більш виразною, але зберегти акуратність. Комбінація матових, глянцевих і світлових деталей допомагає виділити зони та додати інтер’єру глибину. У дизайні це варіант для тих, хто хоче індивідуальну стелю без відчуття перевантаження."),
            ("Зоряне небо", "від 35 у.е./м²", "Зоряне небо створює м’який світловий сценарій із точками світла, які нагадують нічне небо. Техніка може використовувати оптоволокно або спеціальні світлові елементи, залежно від бажаного ефекту. Таке рішення особливо добре підходить для спалень, дитячих і зон відпочинку. У дизайні воно додає атмосферу, спокій і відчуття особистого простору."),
            ("Карнизи", "від 25 у.е.", "Приховані карнизи допомагають сховати кріплення штор і залишити лінію стелі чистою. Ніша розраховується заздалегідь, щоб тканина красиво виходила зі стелі й не сперечалася з інтер’єром. Така техніка візуально збільшує висоту приміщення та робить вікно акуратнішим. У дизайні це невелика деталь, яка сильно впливає на відчуття завершеності кімнати."),
        ],
    },
    "en": {
        "title": "Current prices",
        "subtitle": "Estimated pricing. The final price is calculated after measurement.",
        "note": "Prices are approximate. The final cost depends on area, number of corners, selected material, lighting and installation complexity.",
        "items": [
            ("Shadow ceiling", "from 10 USD/m²", "A shadow ceiling creates a thin, clean gap between the wall and the ceiling surface, so the interior feels modern and precise. This technique works especially well in minimalist rooms where visible decorative trim is not wanted. The contour highlights the room geometry and makes the transition from wall to ceiling feel lighter. In design, it looks calm, refined and very clean."),
            ("Floating ceiling", "from 10 USD/m²", "A floating ceiling uses a special profile with soft LED lighting around the perimeter. The glow separates the ceiling from the walls and creates a light suspended effect. This approach looks especially beautiful in the evening when the main light is dimmed. It adds depth, comfort and a sense of modern architecture to the room."),
            ("Light lines", "from 35 USD/m²", "Light lines are built into the ceiling as clean illuminated accents that set the rhythm of the room. They can be straight, geometric or adapted to a more complex layout. The technique requires precise profile preparation and careful installation so every line stays perfectly even. In design, it is one of the strongest ways to replace a standard chandelier and make the interior feel contemporary."),
            ("Photo printing", "from 25 USD/m²", "Photo printing makes it possible to place an image, pattern or soft decorative motif on the ceiling. The key is choosing artwork that supports the room rather than overwhelming it. This technique works well for children’s rooms, themed zones, commercial spaces and accent interiors. When selected carefully, the image feels like part of the full design idea instead of random decoration."),
            ("Apply ceilings", "from 25 USD/m²", "Apply ceilings combine several textures, levels and decorative elements in one ceiling solution. This technique is useful when the ceiling should be more expressive while still staying neat. Matte, glossy and illuminated details can help zone the room and add depth to the interior. In design, it is a good option for a custom ceiling without visual overload."),
            ("Starry sky", "from 35 USD/m²", "A starry sky ceiling creates a soft lighting scenario with points of light that resemble the night sky. The technique can use fiber optics or special lighting elements depending on the desired effect. It is especially suitable for bedrooms, children’s rooms and relaxation areas. In design, it adds atmosphere, calm and a feeling of personal space."),
            ("Curtain rails", "from 25 USD", "Hidden curtain rails conceal the curtain fixing and keep the ceiling line clean. The niche is planned in advance so the fabric appears to come neatly from the ceiling. This technique visually increases the room height and makes the window area look more refined. In design, it is a small detail that strongly affects the feeling of a finished interior."),
        ],
    },
}

work_content = {
    "ru": {
        "title": "Примеры наших работ",
        "subtitle": "Ровные фото по категориям: максимум четыре работы в ряду и короткие подписи без перегруза.",
        "details": "Подробнее",
        "price": "Узнать стоимость",
        "viber": "Написать в Viber",
        "close": "Закрыть",
        "meta": ("Локация: Одесса", "Площадь: по замеру", "Фактура: матовая", "Свет: LED / световые линии", "Технология: профиль по задаче"),
        "categories": [
            ("Световые линии", [
                ("Геометрические световые линии", "Чёткая световая геометрия в современном интерьере.", "img/eralux/eralux-signed-light-lines-01.jpg"),
                ("Линии света в гостиной", "Мягкое освещение без визуального шума.", "img/eralux/eralux-signed-light-lines-02.jpg"),
                ("Световой акцент", "Аккуратная работа с направлением света.", "img/eralux/eralux-signed-light-lines-03.jpg"),
                ("Минималистичные линии", "Сдержанный потолок с выразительным контуром.", "img/eralux/eralux-signed-light-lines-04.jpg"),
            ]),
            ("Парящий потолок", [
                ("Парящий контур", "Лёгкая подсветка по периметру комнаты.", "img/eralux/eralux-gallery-led-perimeter-01.jpg"),
                ("LED-подсветка периметра", "Ровный мягкий свет для вечернего сценария.", "img/eralux/eralux-gallery-led-perimeter-02.jpg"),
                ("Периметральная подсветка", "Чистая линия света по краю потолка.", "img/eralux/eralux-internet-perimeter-lighting.jpg"),
                ("Тёплый LED-контур", "Комфортное освещение для жилой зоны.", "img/eralux/eralux-signed-led-perimeter-02.jpg"),
            ]),
            ("Ниша под шторы", [
                ("Скрытая ниша", "Карниз спрятан, линия потолка остаётся чистой.", "img/eralux/eralux-gallery-curtain-niche-01.jpg"),
                ("Ниша вдоль окна", "Аккуратное решение для штор в комнате.", "img/eralux/eralux-gallery-curtain-niche-02.jpg"),
                ("Ниша с ровным контуром", "Сдержанный интерьер без лишних деталей.", "img/eralux/eralux-signed-curtain-niche-01.jpg"),
                ("Чистая зона окна", "Шторы выглядят встроенными в интерьер.", "img/eralux/eralux-signed-curtain-niche-02.jpg"),
            ]),
            ("Теневой потолок", [
                ("Теневой профиль", "Аккуратный контур между стеной и потолком.", "img/eralux/eralux-gallery-shadow-ceiling-01.jpg"),
                ("Матовый потолок", "Спокойная поверхность для современной комнаты.", "img/eralux/eralux-gallery-bedroom-ceiling-01.jpg"),
                ("Потолок в коридоре", "Практичное решение для проходной зоны.", "img/eralux/eralux-gallery-hallway-ceiling-01.jpg"),
                ("Потолок в ванной", "Чистая геометрия для влажного помещения.", "img/eralux/eralux-gallery-bathroom-ceiling-01.jpg"),
            ]),
        ],
    },
    "uk": {
        "title": "Приклади наших робіт",
        "subtitle": "Рівні фото за категоріями: максимум чотири роботи в ряду та короткі підписи без перевантаження.",
        "details": "Детальніше",
        "price": "Дізнатися вартість",
        "viber": "Написати у Viber",
        "close": "Закрити",
        "meta": ("Локація: Одеса", "Площа: за заміром", "Фактура: матова", "Світло: LED / світлові лінії", "Технологія: профіль під задачу"),
        "categories": [
            ("Світлові лінії", [
                ("Геометричні світлові лінії", "Чітка світлова геометрія в сучасному інтер’єрі.", "img/eralux/eralux-signed-light-lines-01.jpg"),
                ("Лінії світла у вітальні", "М’яке освітлення без візуального шуму.", "img/eralux/eralux-signed-light-lines-02.jpg"),
                ("Світловий акцент", "Акуратна робота з напрямком світла.", "img/eralux/eralux-signed-light-lines-03.jpg"),
                ("Мінімалістичні лінії", "Стримана стеля з виразним контуром.", "img/eralux/eralux-signed-light-lines-04.jpg"),
            ]),
            ("Паряща стеля", [
                ("Парящий контур", "Легке підсвічування по периметру кімнати.", "img/eralux/eralux-gallery-led-perimeter-01.jpg"),
                ("LED-підсвічування периметра", "Рівне м’яке світло для вечірнього сценарію.", "img/eralux/eralux-gallery-led-perimeter-02.jpg"),
                ("Периметральне підсвічування", "Чиста лінія світла по краю стелі.", "img/eralux/eralux-internet-perimeter-lighting.jpg"),
                ("Теплий LED-контур", "Комфортне освітлення для житлової зони.", "img/eralux/eralux-signed-led-perimeter-02.jpg"),
            ]),
            ("Ніша під штори", [
                ("Прихована ніша", "Карниз схований, лінія стелі залишається чистою.", "img/eralux/eralux-gallery-curtain-niche-01.jpg"),
                ("Ніша вздовж вікна", "Акуратне рішення для штор у кімнаті.", "img/eralux/eralux-gallery-curtain-niche-02.jpg"),
                ("Ніша з рівним контуром", "Стриманий інтер’єр без зайвих деталей.", "img/eralux/eralux-signed-curtain-niche-01.jpg"),
                ("Чиста зона вікна", "Штори виглядають вбудованими в інтер’єр.", "img/eralux/eralux-signed-curtain-niche-02.jpg"),
            ]),
            ("Тіньова стеля", [
                ("Тіньовий профіль", "Акуратний контур між стіною та стелею.", "img/eralux/eralux-gallery-shadow-ceiling-01.jpg"),
                ("Матова стеля", "Спокійна поверхня для сучасної кімнати.", "img/eralux/eralux-gallery-bedroom-ceiling-01.jpg"),
                ("Стеля в коридорі", "Практичне рішення для прохідної зони.", "img/eralux/eralux-gallery-hallway-ceiling-01.jpg"),
                ("Стеля у ванній", "Чиста геометрія для вологого приміщення.", "img/eralux/eralux-gallery-bathroom-ceiling-01.jpg"),
            ]),
        ],
    },
    "en": {
        "title": "Examples of our work",
        "subtitle": "Clean project photos by category, with short captions and no overloaded metadata in the grid.",
        "details": "Details",
        "price": "Get the price",
        "viber": "Write in Viber",
        "close": "Close",
        "meta": ("Location: Odesa", "Area: measured individually", "Texture: matte", "Lighting: LED / light lines", "Technology: profile selected for the project"),
        "categories": [
            ("Light lines", [
                ("Geometric light lines", "Clear lighting geometry for a modern interior.", "img/eralux/eralux-signed-light-lines-01.jpg"),
                ("Light lines in a living room", "Soft lighting without visual noise.", "img/eralux/eralux-signed-light-lines-02.jpg"),
                ("Lighting accent", "Careful work with light direction.", "img/eralux/eralux-signed-light-lines-03.jpg"),
                ("Minimal light lines", "A restrained ceiling with a clear outline.", "img/eralux/eralux-signed-light-lines-04.jpg"),
            ]),
            ("Floating ceiling", [
                ("Floating contour", "Light perimeter lighting around the room.", "img/eralux/eralux-gallery-led-perimeter-01.jpg"),
                ("LED perimeter lighting", "Even soft light for an evening scenario.", "img/eralux/eralux-gallery-led-perimeter-02.jpg"),
                ("Perimeter LED lighting", "A clean light line along the ceiling edge.", "img/eralux/eralux-internet-perimeter-lighting.jpg"),
                ("Warm LED contour", "Comfortable lighting for a living area.", "img/eralux/eralux-signed-led-perimeter-02.jpg"),
            ]),
            ("Curtain niche", [
                ("Hidden curtain niche", "The rail is hidden and the ceiling line stays clean.", "img/eralux/eralux-gallery-curtain-niche-01.jpg"),
                ("Niche along the window", "A neat curtain solution for the room.", "img/eralux/eralux-gallery-curtain-niche-02.jpg"),
                ("Clean niche contour", "A restrained interior without extra details.", "img/eralux/eralux-signed-curtain-niche-01.jpg"),
                ("Clean window zone", "Curtains look integrated into the interior.", "img/eralux/eralux-signed-curtain-niche-02.jpg"),
            ]),
            ("Shadow ceiling", [
                ("Shadow profile", "A neat contour between the wall and ceiling.", "img/eralux/eralux-gallery-shadow-ceiling-01.jpg"),
                ("Matte ceiling", "A calm surface for a modern room.", "img/eralux/eralux-gallery-bedroom-ceiling-01.jpg"),
                ("Hallway ceiling", "A practical solution for a transit area.", "img/eralux/eralux-gallery-hallway-ceiling-01.jpg"),
                ("Bathroom ceiling", "Clean geometry for a humid room.", "img/eralux/eralux-gallery-bathroom-ceiling-01.jpg"),
            ]),
        ],
    },
}

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
    ("0", "manual", ["001"]),
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
    if number == "001":
        return {
            "base": "#ffffff",
            "shadow": "#e7e9ee",
            "highlight": "#ffffff",
            "finish": "matte",
        }
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

palette_group_labels = {
    "ru": [
        ("light", "Светлые и белые"),
        ("blue", "Голубые и синие"),
        ("green", "Зелёные"),
        ("dark", "Серые и графитовые"),
        ("neutral", "Бежевые и нейтральные"),
        ("red", "Красные и бордовые"),
        ("violet", "Розовые и фиолетовые"),
        ("yellow", "Жёлтые и тёплые"),
    ],
    "uk": [
        ("light", "Світлі та білі"),
        ("blue", "Блакитні та сині"),
        ("green", "Зелені"),
        ("dark", "Сірі та графітові"),
        ("neutral", "Бежеві та нейтральні"),
        ("red", "Червоні та бордові"),
        ("violet", "Рожеві та фіолетові"),
        ("yellow", "Жовті та теплі"),
    ],
    "en": [
        ("light", "Light and white"),
        ("blue", "Blue shades"),
        ("green", "Green shades"),
        ("dark", "Gray and graphite"),
        ("neutral", "Beige and neutral"),
        ("red", "Red and burgundy"),
        ("violet", "Pink and violet"),
        ("yellow", "Yellow and warm"),
    ],
}


def palette_rgb(item: dict[str, str]) -> tuple[int, int, int]:
    value = item["base"].lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def palette_group(item: dict[str, str]) -> str:
    rgb = palette_rgb(item)
    hue, saturation, value = colorsys.rgb_to_hsv(*(channel / 255 for channel in rgb))
    hue *= 360
    if saturation < 0.18:
        return "light" if value >= 0.62 else "dark"
    if 20 <= hue < 40 and saturation < 0.5:
        return "neutral"
    if 20 <= hue < 75:
        return "yellow"
    if 75 <= hue < 175:
        return "green"
    if 175 <= hue < 255:
        return "blue"
    if hue < 20 or hue >= 345:
        return "red"
    if hue >= 255:
        return "violet"
    return "neutral"


def palette_brightness(item: dict[str, str]) -> float:
    red, green, blue = palette_rgb(item)
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue

benefits_content = {
    "ru": {
        "title": "Что вы получаете с ERALUX",
        "subtitle": "Аккуратный монтаж, понятный расчёт и современные решения для потолка",
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
        "title": "Що ви отримуєте з ERALUX",
        "subtitle": "Акуратний монтаж, зрозумілий розрахунок і сучасні рішення для стелі",
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
        "title": "What you get with ERALUX",
        "subtitle": "Careful installation, clear pricing and modern ceiling solutions",
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

cta_content = {
    "ru": {
        "title": "Запишитесь на замер сегодня",
        "text": "Оставьте контактные данные — специалист ERALUX перезвонит, уточнит детали и поможет подобрать потолок под ваш интерьер.",
        "name": "Ваше имя",
        "phone": "Введите ваш номер*",
        "button": "Заказать замер",
        "viber": "Написать в Viber",
        "telegram": "Написать в Telegram",
        "call": "Позвонить",
        "benefits": ["Бесплатный замер по Одессе и области", "Подбор фактуры, цвета и подсветки", "Понятный расчёт до начала работ", "Аккуратный монтаж и гарантия"],
    },
    "uk": {
        "title": "Запишіться на замір сьогодні",
        "text": "Залиште контактні дані — спеціаліст ERALUX передзвонить, уточнить деталі та допоможе підібрати стелю під ваш інтер’єр.",
        "name": "Ваше ім’я",
        "phone": "Введіть ваш номер*",
        "button": "Замовити замір",
        "viber": "Написати у Viber",
        "telegram": "Написати у Telegram",
        "call": "Зателефонувати",
        "benefits": ["Безкоштовний замір по Одесі та області", "Підбір фактури, кольору та підсвічування", "Зрозумілий розрахунок до початку робіт", "Акуратний монтаж і гарантія"],
    },
    "en": {
        "title": "Request a measurement today",
        "text": "Leave your contact details and an ERALUX specialist will call back, clarify the project and help select a ceiling for your interior.",
        "name": "Your name",
        "phone": "Enter your phone*",
        "button": "Request a measurement",
        "viber": "Write in Viber",
        "telegram": "Write in Telegram",
        "call": "Call us",
        "benefits": ["Free measurement in Odesa and the region", "Material, color and lighting selection", "Clear estimate before installation", "Careful installation and warranty"],
    },
}

benefits_content = {
    "ru": {
        "title": "Что вы получаете с ERALUX",
        "subtitle": "Аккуратный монтаж, понятный расчет и современные решения для потолка",
        "items": [
            ("shield", "12 лет гарантии", "Мы используем проверенные материалы и отвечаем за качество монтажа. Потолок сохраняет форму, цвет и аккуратный внешний вид при нормальной эксплуатации. Все узлы крепления подбираются под помещение, чтобы конструкция служила спокойно и надежно. Гарантия дает уверенность, что результат останется красивым не только в день установки."),
            ("ruler", "Бесплатный замер", "Мастер приезжает на объект и внимательно оценивает геометрию помещения. На замере уточняются углы, ниши, светильники, карнизы и будущая подсветка. После этого вы получаете понятный расчет без лишних сюрпризов. Такой подход помогает выбрать решение, которое подходит и по виду, и по бюджету."),
            ("tools", "Монтаж за 1 день", "Большинство стандартных потолков мы устанавливаем в течение одного рабочего дня. Команда заранее готовит материалы и план работ, чтобы монтаж проходил быстро и спокойно. Мы бережно относимся к стенам, мебели и уже готовому ремонту. В результате комната быстро получает чистый, ровный и завершенный вид."),
            ("sparkle", "Аккуратная работа", "Для нас важны ровные линии, чистые стыки и внимательное отношение к деталям. Мы работаем без лишнего шума и стараемся оставлять после себя порядок. Каждый участок потолка проверяется визуально, чтобы поверхность выглядела цельно. Именно аккуратность делает интерьер дороже и приятнее в ежедневном использовании."),
            ("lamp", "Современные решения", "ERALUX помогает сделать потолок частью дизайна, а не просто ровной поверхностью. Световые линии, теневой профиль, ниши под шторы и LED-подсветка создают нужную атмосферу в комнате. Мы подбираем решение под стиль интерьера, высоту помещения и сценарии освещения. Такой потолок выглядит современно днем и особенно эффектно вечером."),
            ("pin", "Одесса и область", "Мы работаем по Одессе и выезжаем на объекты в Одесской области. Мастер заранее согласует удобное время и приезжает с учетом особенностей объекта. Можно заказать замер для квартиры, дома, офиса или коммерческого помещения. Локальная работа помогает быстрее решать вопросы и держать связь на каждом этапе."),
        ],
    },
    "uk": {
        "title": "Що ви отримуєте з ERALUX",
        "subtitle": "Акуратний монтаж, зрозумілий розрахунок і сучасні рішення для стелі",
        "items": [
            ("shield", "12 років гарантії", "Ми використовуємо перевірені матеріали та відповідаємо за якість монтажу. Стеля зберігає форму, колір і акуратний вигляд за нормальної експлуатації. Усі вузли кріплення підбираються під конкретне приміщення, щоб конструкція служила спокійно й надійно. Гарантія дає впевненість, що результат залишиться красивим не лише в день встановлення."),
            ("ruler", "Безкоштовний замір", "Майстер приїжджає на об’єкт і уважно оцінює геометрію приміщення. Під час заміру уточнюються кути, ніші, світильники, карнизи та майбутня підсвітка. Після цього ви отримуєте зрозумілий розрахунок без зайвих сюрпризів. Такий підхід допомагає вибрати рішення, яке підходить і за виглядом, і за бюджетом."),
            ("tools", "Монтаж за 1 день", "Більшість стандартних стель ми встановлюємо протягом одного робочого дня. Команда заздалегідь готує матеріали та план робіт, щоб монтаж проходив швидко й спокійно. Ми бережно ставимося до стін, меблів і вже готового ремонту. У результаті кімната швидко отримує чистий, рівний і завершений вигляд."),
            ("sparkle", "Акуратна робота", "Для нас важливі рівні лінії, чисті стики та уважне ставлення до деталей. Ми працюємо без зайвого шуму й стараємося залишати після себе порядок. Кожна ділянка стелі перевіряється візуально, щоб поверхня виглядала цілісно. Саме акуратність робить інтер’єр дорожчим і приємнішим у щоденному використанні."),
            ("lamp", "Сучасні рішення", "ERALUX допомагає зробити стелю частиною дизайну, а не просто рівною поверхнею. Світлові лінії, тіньовий профіль, ніші під штори та LED-підсвічування створюють потрібну атмосферу в кімнаті. Ми підбираємо рішення під стиль інтер’єру, висоту приміщення та сценарії освітлення. Така стеля виглядає сучасно вдень і особливо ефектно ввечері."),
            ("pin", "Одеса та область", "Ми працюємо по Одесі та виїжджаємо на об’єкти в Одеській області. Майстер заздалегідь погоджує зручний час і приїжджає з урахуванням особливостей об’єкта. Можна замовити замір для квартири, будинку, офісу або комерційного приміщення. Локальна робота допомагає швидше вирішувати питання й тримати зв’язок на кожному етапі."),
        ],
    },
    "en": {
        "title": "What you get with ERALUX",
        "subtitle": "Careful installation, clear pricing and modern ceiling solutions",
        "items": [
            ("shield", "12-year warranty", "We use proven materials and stand behind the installation quality. The ceiling keeps its shape, color and clean appearance under normal use. Every fixing point is selected for the room, so the system feels stable and reliable. The warranty gives you confidence that the result will stay beautiful long after installation day."),
            ("ruler", "Free measurement", "A specialist visits the site and carefully checks the room geometry. Corners, niches, lighting points, curtain tracks and LED details are clarified during the visit. After that you receive a clear estimate without unpleasant surprises. This helps choose a solution that fits both the interior and the budget."),
            ("tools", "Installation in 1 day", "Most standard ceilings are installed within one working day. The team prepares materials and the work plan in advance, so the process stays fast and calm. We treat walls, furniture and finished renovation with care. As a result, the room quickly gets a clean, even and finished look."),
            ("sparkle", "Neat work", "Clean lines, accurate joints and attention to detail are central to our work. We install carefully and try to leave the space tidy after the job. Every part of the ceiling is visually checked so the surface feels complete. This level of care makes the interior look more refined in everyday use."),
            ("lamp", "Modern solutions", "ERALUX helps turn the ceiling into part of the design, not just a flat surface. Light lines, shadow profiles, curtain niches and LED lighting create the right atmosphere in the room. We match the solution to the interior style, ceiling height and lighting scenarios. The result looks modern during the day and especially expressive in the evening."),
            ("pin", "Odesa region", "We work across Odesa and travel to projects throughout the Odesa region. A specialist agrees on a convenient time and arrives prepared for the site conditions. Measurements are available for apartments, houses, offices and commercial spaces. Local service helps us answer faster and stay connected at every stage."),
        ],
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
    data = work_content[lang]
    categories = []
    for category, projects in data["categories"]:
        cards = []
        for title, description, image in projects[:4]:
            metadata = " | ".join(data["meta"])
            cards.append(
                f'<button class="work-photo-card" type="button" data-work-image="/{image}" '
                f'data-work-title="{escape(title, quote=True)}" data-work-description="{escape(description, quote=True)}" '
                f'data-work-meta="{escape(metadata, quote=True)}">'
                f'<span class="work-photo-card__media"><img src="/{image}" alt="{escape(title, quote=True)}" loading="lazy">'
                f'<span class="work-photo-card__overlay">{data["details"]}</span></span>'
                f'<span class="work-photo-card__body"><strong>{title}</strong><small>{description}</small></span>'
                '</button>'
            )
        categories.append(
            f'<section class="work-category"><h3>{category}</h3><div class="work-grid">{"".join(cards)}</div></section>'
        )
    return (
        '<section class="eralux-work-gallery eralux-section" id="gallery"><div class="eralux-container">'
        f'<div class="eralux-section-head"><h2>{data["title"]}</h2><p>{data["subtitle"]}</p></div>'
        f'{"".join(categories)}</div></section>'
        '<div class="work-modal" aria-hidden="true"><div class="work-modal__backdrop" data-work-close></div>'
        '<div class="work-modal__dialog" role="dialog" aria-modal="true">'
        f'<button class="work-modal__close" type="button" data-work-close aria-label="{data["close"]}">×</button>'
        '<img class="work-modal__image" src="" alt=""><div class="work-modal__body"><h3></h3><p class="work-modal__description"></p><p class="work-modal__meta"></p>'
        f'<div class="work-modal__actions"><a href="#callback">{data["price"]}</a><a href="https://viber.me/380968074894">{data["viber"]}</a></div>'
        '</div></div></div>'
    )


def prices(lang: str) -> str:
    data = price_content[lang]
    cards = "".join(
        f'<button class="price-card" type="button" data-expand-card aria-expanded="false"><h3>{title}</h3><strong class="price-value">{value}</strong><p>{hint}</p></button>'
        for title, value, hint in data["items"]
    )
    return (
        '<section class="prices-section eralux-section" id="prices"><div class="eralux-container">'
        f'<div class="eralux-section-head"><h2>{data["title"]}</h2><p>{data["subtitle"]}</p></div>'
        f'<div class="price-grid">{cards}</div><p class="price-note">{data["note"]}</p>'
        '</div></section>'
    )


def palette(lang: str) -> str:
    title, subtitle, disclaimer = palette_meta[lang]
    cards_by_group = {group_key: [] for group_key, _ in palette_group_labels[lang]}
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
        card_html = (
            f'<article class="eralux-palette-card palette-card--{finish}" style="{style}" '
            f'data-palette-number="№ {number}" data-palette-description="{escape(description, quote=True)}" '
            f'data-palette-base="{base}" data-palette-shadow="{shadow}" data-palette-highlight="{highlight}" data-palette-finish="{finish}" data-palette-finish-label="{finish_label}">'
            '<button class="palette-swatch palette-strip" type="button" aria-label="palette sample">'
            '<span class="palette-swatch-surface"></span>'
            f'<span class="palette-strip__number">№ {number}</span>'
            "</button>"
            '<div class="palette-card-body">'
            f'<span class="palette-number">№ {number}</span>'
            f'<span class="palette-description">{description}</span>'
            "</div>"
            "</article>"
        )
        cards_by_group[palette_group(item)].append((palette_brightness(item), card_html))
    groups = []
    for group_key, group_title in palette_group_labels[lang]:
        group_cards = cards_by_group[group_key]
        if not group_cards:
            continue
        group_cards.sort(key=lambda card: card[0], reverse=True)
        groups.append(
            f'<section class="palette-group palette-family" data-palette-group="{group_key}">'
            f'<h3 class="palette-group__title">{group_title}</h3>'
            f'<div class="palette-group__grid palette-strip-grid">{"".join(card[1] for card in group_cards)}</div>'
            '</section>'
        )
    return (
        '<section class="eralux-palette wrapper section" id="palette">'
        f'<div class="eralux-palette__head"><h2 class="title-dec">{title}</h2><p>{subtitle}</p></div>'
        f'<div class="eralux-palette__groups">{"".join(groups)}</div>'
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
            '<button class="benefit-card" type="button" data-expand-card aria-expanded="false">'
            f'<span class="benefit-card__icon"><svg viewBox="0 0 24 24" aria-hidden="true">{icon_paths[icon]}</svg></span>'
            f"<h3>{title}</h3><p>{text}</p>"
            "</button>"
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
    data = cta_content[lang]
    benefits = "".join(
        f'<li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 12l2 2 4-5"/><circle cx="12" cy="12" r="9"/></svg>{item}</li>'
        for item in data["benefits"]
    )
    return (
        '<section class="eralux-cta" id="callback">'
        '<div class="container eralux-cta__content">'
        f'<div class="eralux-cta__copy"><h2>{data["title"]}</h2><p>{data["text"]}</p><ul>{benefits}</ul></div>'
        '<div class="eralux-cta__panel">'
        f'<form class="form js-less eralux-cta__form" action="/api/lead" method="POST" data-lead-form data-lang="{lang}">'
        f'<input class="input form__input form__input_horiz" type="text" name="name" required placeholder="{data["name"]}">'
        f'<input class="input form__input form__input_horiz" type="tel" name="phone" required placeholder="{data["phone"]}">'
        '<input type="text" name="website" tabindex="-1" autocomplete="off" class="lead-trap" aria-hidden="true">'
        f'<button class="button form__button btn-4">{data["button"]}</button>'
        '<p class="lead-form-status" aria-live="polite"></p>'
        '</form>'
        '<div class="eralux-cta__actions">'
        f'<a class="cta-action cta-action--viber" href="https://viber.me/380968074894">{data["viber"]}</a>'
        f'<a class="cta-action cta-action--telegram" href="tg://resolve?phone=380968074894">{data["telegram"]}</a>'
        f'<a class="cta-action cta-action--phone" href="tel:+380968074894">{data["call"]}</a>'
        '</div></div></div></section>'
    )


def page(lang: str) -> str:
    s = base_html
    d = T[lang]
    path = f"{lang}/"
    s = re.sub(r'<html lang="[^"]+"', f'<html lang="{lang}"', s, count=1)
    s = re.sub(r"<title>.*?</title>", f"<title>{d['title']}</title>", s, count=1, flags=re.S)
    s = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="{d["desc"]}">',
        s,
        count=1,
        flags=re.S,
    )
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "ERALUX",
        "url": f"https://eralux.od.ua/{path}",
        "image": "https://eralux.od.ua/img/eralux/eralux-hero-ceiling.jpg",
        "email": "eralux.info@gmail.com",
        "telephone": ["+380968074894", "+380635703594"],
        "areaServed": ["Odesa", "Odesa region"],
        "priceRange": "$$",
        "description": d["desc"],
    }
    seo = (
        '<link rel="stylesheet" href="/css/app.css?v2">\n'
        '    <link rel="stylesheet" href="/css/eralux-update.css?v=align-text-1">\n'
        f'    <link rel="canonical" href="https://eralux.od.ua/{path}">\n'
        '    <link rel="alternate" hreflang="ru-UA" href="https://eralux.od.ua/ru/">\n'
        '    <link rel="alternate" hreflang="uk-UA" href="https://eralux.od.ua/uk/">\n'
        '    <link rel="alternate" hreflang="en" href="https://eralux.od.ua/en/">\n'
        '    <link rel="alternate" hreflang="x-default" href="https://eralux.od.ua/uk/">\n'
        f'    <meta property="og:type" content="website">\n'
        f'    <meta property="og:site_name" content="ERALUX">\n'
        f'    <meta property="og:title" content="{escape(d["title"], quote=True)}">\n'
        f'    <meta property="og:description" content="{escape(d["desc"], quote=True)}">\n'
        f'    <meta property="og:url" content="https://eralux.od.ua/{path}">\n'
        '    <meta property="og:image" content="https://eralux.od.ua/img/eralux/eralux-hero-ceiling.jpg">\n'
        '    <meta name="google-site-verification" content="PLqSUexgDnCr7iKdnOhkQnnTcrPpUOend03cLJQK1lA">\n'
        f'    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
    )
    s = s.replace('<link rel="stylesheet" href="css/app.css?v2">', seo)
    s = re.sub(r'(href|src|data-src)="(css|js|img)/', r'\1="/\2/', s)
    replacements = [
        (r'<p class="hero__overtitle">.*?</p>', f'<p class="hero__overtitle">{d["hero_over"]}</p>'),
        (r'<h1 class="hero__title">.*?</h1>', f'<h1 class="hero__title">{d["hero_title"]}</h1>'),
        (r'<p class="hero__intro">.*?</p>', f'<p class="hero__intro">{d["hero_intro"]}</p>'),
        (r'placeholder="[^"]+" class="inputN', f'placeholder="{d["phone"]}" class="inputN'),
        (r'<button type="submit" class="buttonN buttonN-red btn-pulse">.*?</button>', f'<button type="submit" class="buttonN buttonN-red btn-pulse">{i18n[lang]["orderMeasure"]}</button><p class="lead-form-status" aria-live="polite"></p>'),
        (r'<p class="calc__total"><span>195</span>.*?</p>', f'<p class="calc__total"><span>7</span> {"USD/m²" if lang == "en" else "у.е./м²"}</p>'),
        (r'<a href="#" class="calc__callback buttonN buttonN-red btn-4 to-form">.*?</a>', f'<a href="#callback" class="calc__callback buttonN buttonN-red btn-4 to-form">{d["calc"]}</a>'),
    ]
    for pattern, value in replacements:
        s = re.sub(pattern, value, s, count=1, flags=re.S)
    calc_labels = {
        "uk": {
            "Калькулятор": "Калькулятор",
            "Расчёт стоимости натяжного потолка.": "Розрахунок вартості натяжної стелі.",
            "Для точного расчёта необходим замер!": "Для точного розрахунку потрібен замір!",
            "Площадь помещения": "Площа приміщення",
            "Периметр помещения": "Периметр приміщення",
            "Количество светильников": "Кількість світильників",
            "Цена с установкой": "Ціна з установкою",
        },
        "en": {
            "Калькулятор": "Calculator",
            "Расчёт стоимости натяжного потолка.": "Stretch ceiling cost estimate.",
            "Для точного расчёта необходим замер!": "A site measurement is required for an exact price!",
            "Площадь помещения": "Room area",
            "Периметр помещения": "Room perimeter",
            "Количество светильников": "Number of spotlights",
            "Цена с установкой": "Price with installation",
        },
    }
    if lang in calc_labels:
        for source, target in calc_labels[lang].items():
            s = s.replace(source, target)
        if lang == "en":
            s = s.replace("(м<sup>2</sup>)", "(m<sup>2</sup>)")
            s = s.replace("(м)</p>", "(m)</p>")
    s = s.replace(
        '<form class="formN hero__form js-less">',
        f'<form class="formN hero__form js-less" action="/api/lead" method="POST" data-lead-form data-lang="{lang}">'
        '<input type="text" name="website" tabindex="-1" autocomplete="off" class="lead-trap" aria-hidden="true">',
        1,
    )
    logo_alt = {
        "ru": "Логотип ERALUX",
        "uk": "Логотип ERALUX",
        "en": "ERALUX logo",
    }[lang]
    s = re.sub(
        r'<div class="eralux-logo">.*?</div>',
        '<div class="eralux-logo">'
        '<picture>'
        '<source media="(max-width: 640px)" srcset="/img/logo/eralux-logo-original-280.png">'
        f'<img class="hero-logo-image" src="/img/logo/eralux-logo-original-420.png" alt="{logo_alt}">'
        '</picture>'
        '</div>',
        s,
        count=1,
        flags=re.S,
    )
    price_section = prices(lang)
    start = s.find('<div class="portfolio portfolioN portfolio_main portfolio_ceilings new_catalog">')
    nxt = s.find('<div class="portfolio portfolioN portfolio_main portfolio_ceilings new_colors">', start)
    if start != -1 and nxt != -1:
        s = (
            s[:start]
            + f'{gallery(lang)}\n\t\t{price_section}\n\t\t'
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
    pref_start = s.find('<div class="other section wrapper new-pref">')
    pref_end = s.find('<div class="seo-block seo-block_main">', pref_start)
    if pref_start != -1 and pref_end != -1:
        s = s[:pref_start] + benefits(lang) + "\n\t\t" + s[pref_end:]
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
        f'<a class="{"is-active" if lang == "uk" else ""}" href="/uk/">UA</a>'
        f'<a class="{"is-active" if lang == "ru" else ""}" href="/">RU</a>'
        f'<a class="{"is-active" if lang == "en" else ""}" href="/en/">EN</a>'
        "</nav>"
    )
    s = s.replace(
        "</div>\n\t\t</div>\n\t</div>\n\n\t<div class=\"main\">",
        switch + "</div>\n\t\t</div>\n\t</div>\n\n\t<div class=\"main\">",
        1,
    )
    favicon_links = (
        '<link rel="icon" href="/favicon.ico?v=eralux-1" sizes="any">\n'
        '    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=eralux-1">\n'
        '    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png?v=eralux-1">\n'
        '    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=eralux-1">\n'
        '    <link rel="manifest" href="/site.webmanifest">\n'
        '    <meta name="theme-color" content="#151922">'
    )
    s = s.replace('<link rel="icon" href="/favicon.ico" type="image/x-icon">', favicon_links)
    s = s.replace(
        '<img class="logo__icon" src="/img/logo1.png" alt="логотип Твой Стиль">',
        '<img class="logo__icon" src="/img/logo/eralux-logo-original-280.png" alt="ERALUX">',
    )
    floating = (
        '<div class="eralux-floating floating-actions">'
        f'<button class="eralux-floating__btn floating-action floating-action--top eralux-floating__top" type="button" aria-label="{d["top"]}">'
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5l7 7-1.4 1.4L13 8.8V20h-2V8.8l-4.6 4.6L5 12l7-7z" fill="currentColor"/></svg>'
        '</button>'
        '<a class="eralux-floating__btn floating-action floating-action--telegram" href="tg://resolve?phone=380968074894" aria-label="Telegram">'
        '<img src="/img/icons/telegram.png" alt="" aria-hidden="true"></a>'
        f'<a class="eralux-floating__btn floating-action floating-action--viber" href="https://viber.me/380968074894" target="_blank" rel="noopener" aria-label="{d["viber"]}">'
        '<img src="/img/icons/viber.png" alt="" aria-hidden="true"></a>'
        '<a class="eralux-floating__btn floating-action floating-action--phone" href="tel:+380968074894" aria-label="Phone">'
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8c1.8 3.5 3.1 4.8 6.6 6.6l2.2-2.2c.3-.3.7-.4 1.1-.2 1.2.4 2.4.6 3.7.6.5 0 .8.3.8.8V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.6c.5 0 .8.3.8.8 0 1.3.2 2.5.6 3.7.1.4.1.8-.2 1.1l-2.2 2.2Z" fill="currentColor"/></svg>'
        '</a></div>\n'
        '<script src="/js/eralux-update.js?v=expand-cards-1"></script>\n'
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
