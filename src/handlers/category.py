from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data.startswith("category_"))
async def handle_category_callback(callback: CallbackQuery):
    category = callback.data.replace("category_", "")

    messages = {
        "sites": "Вы выбрали: Сайты",
        "bots": "Вы выбрали: Боты",
        "parsing": "Вы выбрали: Парсинг",
        "automation": "Вы выбрали: Автоматизация",
        "AI": "Вы выбрали: Искусственный интеллект",
    }

    text = messages.get(category, "❓ Неизвестная категория")
    await callback.message.answer(text)
    await callback.answer()
