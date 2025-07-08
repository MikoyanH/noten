import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Импортируем регистрацию меню
from handlers.menu import register as register_menu

# Регистрируем меню-хендлеры
register_menu(dp)

@dp.message()
async def echo_all(message: types.Message):
    print(f"Получено сообщение от {message.from_user.id}: {message.text}")
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("🚀 Бот запущен...")
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
