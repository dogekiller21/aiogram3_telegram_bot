from aiogram import types
from aiogram.types import KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start(message: types.Message) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text="Помощь"
    )
    menu_builder.add(
        KeyboardButton(text="Отправить контакт", request_contant=True)
    )
    menu_builder.row(
        KeyboardButton(text="Отправить голосование", request_poll=KeyboardButtonPollType(type="quiz"))
    )
    await message.answer("yo", reply_markup=menu_builder.as_markup(resize_keyboard=True))
