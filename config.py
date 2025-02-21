from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
import os

import dotenv

dotenv.load_dotenv(dotenv_path="./.env")

BASE_DIR = Path(__file__).parent
WEATHER_BASE_PHOTO_PATH = BASE_DIR / "media" / "img" / "weather_base.jpg"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    api_key: str = os.getenv("API_KEY")
    # add keys for whether utils


settings = Settings()
