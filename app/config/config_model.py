from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "test_cybellum"
    ROOT_PATH: str = ""
    DEBUG: bool = False
    SECRET_KEY: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    JWT_EXPIRATION_HOURS: int
