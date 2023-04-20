from aiogram import types
from aiogram.filters import CommandObject

from bot.commands.bot_commands import bot_commands


async def help_command(message: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    text=f"{cmd[0]} - {cmd[1]}\n\n"
                         f"{cmd[2]}"
                )
        else:
            return await message.answer("Команда не найдена")
    await help_func(message=message)


async def help_func(message: types.Message):
    await message.answer(
        "Справка по командам в боте\n"
        "Чтобы получить информацию о команде, используй /help <команда>"
    )