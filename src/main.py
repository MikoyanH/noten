import asyncio
import os
import logging
# from dotenv import load_dotenv  # ← не забудь импорт
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import commands, category  # ← роутеры


# Загрузка переменных окружения ДО использования
# env_name = os.getenv("ENV")
# dotenv_path = f".env.{env_name}" if env_name else ".env"  # если переменной ENV нет — грузим .env

# load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")


# Теперь можно безопасно создать Bot и Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Подключаем роутеры
dp.include_router(commands.router)
dp.include_router(category.router)

# Запуск
async def main():
    logging.basicConfig(level=logging.INFO)
    print(f"🚀 [{env_name}] Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
