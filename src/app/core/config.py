from pydantic import BaseSettings


class Settings(BaseSettings):
    # database connection
    HOST: str = "localhost"
    PORT: int = 5432
    USERNAME: str = "myuser"
    PASSWORD: str = "sdfsdf"
    DATABASE: str = "ggolabs"
    SQLALCHEMY_DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'


settings = Settings()