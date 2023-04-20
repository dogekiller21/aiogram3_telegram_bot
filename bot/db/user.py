from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

from bot.db.base import Base
from bot.db.mixins import IdMixin, TimestampMixin


class User(IdMixin, TimestampMixin, Base):

    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(32), unique=False, nullable=True)

    def __str__(self) -> str:
        return f"<User({self.user_id}, {self.username})>"
