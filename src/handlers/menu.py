from aiogram import types, Dispatcher, F

async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🛍 Каталог", "📞 Связаться")
    await message.answer("Добро пожаловать в Not Encrypted!", reply_markup=keyboard)

# Вот это — обработчик на кнопку "Каталог"
async def show_catalog(message: types.Message):
    await message.answer("Здесь будет каталог товаров.")

# Это — на кнопку "Связаться"
async def show_contacts(message: types.Message):
    await message.answer("📞 Вы можете связаться с нами через Telegram: @your_contact")

def register(dp: Dispatcher):
    dp.message.register(cmd_start, F.command.in_({"start", "menu"}))
    dp.message.register(show_catalog, F.text == "🛍 Каталог")
    dp.message.register(show_contacts, F.text == "📞 Связаться")
