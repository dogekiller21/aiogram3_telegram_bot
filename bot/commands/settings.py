from aiogram import types
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def settings_command(message: types.Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Яндекс",
        url="https://yandex.ru/"
    )
    await message.answer("Настройки", reply_markup=keyboard.as_markup())
