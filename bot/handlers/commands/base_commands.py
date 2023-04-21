import logging

from aiogram import types
from aiogram.filters import CommandObject
from aiogram.types import KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlalchemy.ext.asyncio import AsyncSession

from bot.handlers.commands.commands_list import bot_commands

logger = logging.getLogger(__name__)


async def start(message: types.Message, session: AsyncSession) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(text="Помощь")
    menu_builder.add(KeyboardButton(text="Отправить контакт", request_contant=True))
    menu_builder.row(
        KeyboardButton(
            text="Отправить голосование",
            request_poll=KeyboardButtonPollType(type="quiz"),
        )
    )
    await message.answer(
        "yo", reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )


async def help_command(message: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(text=f"{cmd[0]} - {cmd[1]}\n\n" f"{cmd[2]}")
        else:
            return await message.answer("Команда не найдена")
    await help_func(message=message)


async def help_func(message: types.Message):
    await message.answer(
        "Справка по командам в боте\n"
        "Чтобы получить информацию о команде, используй /help <команда>"
    )
