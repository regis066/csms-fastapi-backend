# app/core/config.py

from pydantic_settings import BaseSettings  # Updated import for Pydantic v2


class Settings(BaseSettings):
    DATABASE_URL: str  # This will read the DATABASE_URL from the .env file
    SECRET_KEY: str  # Read SECRET_KEY from .env

    class Config:
        env_file = ".env"  # Ensure it loads from the .env file


# Instantiate settings
settings = Settings()
