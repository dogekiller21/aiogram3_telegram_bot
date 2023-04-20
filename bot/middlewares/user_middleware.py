from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.db import User


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        session_maker: sessionmaker = data.get("session_maker")
        async with session_maker() as session:
            session: AsyncSession
            async with session.begin():
                # Check if user exist
                q = select(User).where(User.telegram_id == event.from_user.id)
                user: User = (await session.execute(q)).scalars().first()
                if user is None:
                    # Add user if not exist
                    user = User(telegram_id=event.from_user.id, username=event.from_user.username)
                    session.add(user)
                    await session.commit()
                else:
                    # Update user's username if it has changed
                    if user.username != event.from_user.username:
                        user.username = event.from_user.username
                        session.add(user)
                        await session.commit()
                # Add user to 'data' to use it handlers
                data["current_user"] = user
        return await handler(event, data)
