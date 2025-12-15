from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_string: str


    class Config:
        env_file = ".env"


settings = Settings()
