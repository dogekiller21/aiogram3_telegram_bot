from datetime import datetime

from sqlalchemy import BigInteger, DateTime, func
from sqlalchemy.orm import Mapped, declarative_mixin, mapped_column


@declarative_mixin
class IdMixin:
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)


@declarative_mixin
class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        onupdate=datetime.now,
    )
