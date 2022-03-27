from pathlib import Path
from pydantic import BaseSettings
import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.load_dotenv(BASE_DIR / 'api.env')


class Settings(BaseSettings):
    KAKAO_API_KEY: str = ''

    class Config:
        env_file = BASE_DIR / 'api.env'


settings = Settings()
