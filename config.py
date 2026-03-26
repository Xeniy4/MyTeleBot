
from pydantic_settings import BaseSettings, SettingsConfigDict

class StandConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    bot_token: str
