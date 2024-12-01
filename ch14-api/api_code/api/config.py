from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    debug: bool
    api_version: str

    class Config:
        env_file = ".env"
