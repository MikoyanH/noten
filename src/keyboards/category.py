from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

categories = [
    ("Сайты", "category_sites"),
    ("Боты", "category_bots"),
    ("Парсинг", "category_parsing"),
    ("Автоматизация", "category_automation"),
    ("Искусственный интеллект", "category_AI"),
]

def get_category_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for name, data in categories:
        builder.button(text=name, callback_data=data)

    # ВАЖНО: adjust раскладывает кнопки по строкам
    return builder.adjust(2).as_markup()
