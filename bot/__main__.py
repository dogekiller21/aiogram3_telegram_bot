import asyncio
import logging
import os
from builtins import SystemExit

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from sqlalchemy import URL

from bot.commands import register_user_commands

from bot.commands.bot_commands import bot_commands


from bot.db import Base, create_async_engine, get_session_maker, proceed_schemas


async def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = []
    for command in bot_commands:
        commands_for_bot.append(BotCommand(command=command[0], description=command[1]))
    dp = Dispatcher()
    bot = Bot(token=os.getenv("token"))
    await bot.set_my_commands(commands_for_bot)
    register_user_commands(dp)

    pg_url = URL.create(
        drivername="postgresql+asyncpg",
        username=os.getenv("db_user"),
        password=os.getenv("db_password"),
        database=os.getenv("db_name"),
        port=os.getenv("db_port"),
        host=os.getenv("db_host")
    )

    async_engine = create_async_engine(url=pg_url)
    await proceed_schemas(engine=async_engine, metadata=Base.metadata)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
        exit()
