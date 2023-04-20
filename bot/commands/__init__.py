__all__ = ["register_user_commands", "bot_commands"]


from aiogram import Router
from aiogram.filters import CommandStart, Command, Text

from bot.commands.help import help_command, help_func
from bot.commands.settings import settings_command
from bot.commands.start import start


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=["help"]))
    router.message.register(help_func, Text(text="Помощь"))
    router.message.register(settings_command, Command(commands=["settings"]))
