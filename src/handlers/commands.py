from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.category import get_category_keyboard

router = Router()

category_keyboard = get_category_keyboard()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(
        f"Добро пожаловать, {message.from_user.full_name}!\nВыберите категорию:",
        reply_markup=category_keyboard
    )


@router.message(Command("menu"))
async def menu_handler(message: Message):
    await message.answer("Вот меню:", reply_markup=get_category_keyboard())
