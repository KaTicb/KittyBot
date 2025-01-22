from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).parent
WEATHER_BASE_PHOTO_PATH = BASE_DIR / "media" / "img" / "weather_base.jpg"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    api_key: str
    # add keys for whether utils


settings = Settings()
