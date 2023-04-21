import os
from functools import lru_cache
from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator

USE_CACHED_SETTINGS = os.getenv("USE_CACHED_SETTINGS", "True").lower == "true"


class BotSettings(BaseSettings):
    BOT_TOKEN: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_PORT: str

    DB_URL: PostgresDsn | None = None

    @validator("DB_URL", pre=True)
    def assemble_db_url(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
            port=f"{values.get('POSTGRES_PORT') or ''}",
        )


def _get_settings(env_file: str | None = ".env"):
    if env_file is not None and os.path.isfile(env_file):
        return BotSettings(_env_file=env_file, _env_file_encoding="utf-8")
    return BotSettings()


@lru_cache
def get_cached_settings():
    return _get_settings()


def get_settings() -> BotSettings:
    if USE_CACHED_SETTINGS:
        return get_cached_settings()
    else:
        return _get_settings()
