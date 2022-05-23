from pydantic import BaseSettings


class LocalSettings(BaseSettings):
    # database connection
    HOST: str = "localhost"
    PORT: int = 5432
    USERNAME: str = "myuser"
    PASSWORD: str = "sdfsdf"
    DATABASE: str = "ggolabs"
    API_V1_PREFIX: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'


settings = LocalSettings()
