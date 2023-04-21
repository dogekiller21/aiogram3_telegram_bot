import asyncio
import logging
from builtins import SystemExit

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from bot.commands import register_user_commands

from bot.commands.bot_commands import bot_commands

from bot.db import create_async_engine, get_session_maker
from bot.middlewares.user_middleware import UserMiddleware
from bot.config import get_settings

settings = get_settings()


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for command in bot_commands:
        commands_for_bot.append(BotCommand(command=command[0], description=command[1]))
    dp = Dispatcher()
    dp.message.middleware(UserMiddleware())
    dp.callback_query.middleware(UserMiddleware())

    bot = Bot(settings.BOT_TOKEN)
    await bot.set_my_commands(commands_for_bot)
    register_user_commands(dp)
    async_engine = create_async_engine(url=settings.DB_URL)
    await dp.start_polling(bot, session_maker=get_session_maker(engine=async_engine))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
        exit()
