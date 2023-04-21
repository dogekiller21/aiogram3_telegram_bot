__all__ = ["register_user_commands", "bot_commands"]


from aiogram import Router
from aiogram.filters import CommandStart, Command, Text

from bot.handlers.commands.settings_commands import settings_command
from bot.handlers.commands.base_commands import start, help_command, help_func
from bot.handlers.commands.commands_list import bot_commands


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_func, Text(text="Помощь"))
    router.message.register(settings_command, Command(commands=["settings"]))
