import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import commands, category  # импортируем наши роутеры

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


dp.include_router(commands.router)
dp.include_router(category.router)

async def main():
    print("🚀 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




