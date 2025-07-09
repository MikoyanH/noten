from aiogram.types import CallbackQuery
from aiogram import Router, F

@dp.callback_query(F.data.startswith("category_"))
async def category_chosen_handler(callback: CallbackQuery):
    category = callback.data[len("category_"):]  # получаем id категории, например 'shops'
    await callback.answer(f"Вы выбрали категорию: {category}")
    # Тут можно добавить логику для каждой категории, например, запускать разные сцены
