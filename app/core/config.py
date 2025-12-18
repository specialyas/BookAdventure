# Store database settings and configuration values

# Import BaseSettings, which loads and validates environment variables
from pydantic_settings import BaseSettings


# Define a settings class for application configuration
class Settings(BaseSettings):
    # Database connection string used by SQLAlchemy
    sqlalchemy_string: str


    # Configuration for how settings are loaded
    class Config:
        # Load environment variables from a .env file
        env_file = ".env"


# Create a settings instance
# This reads values from environment variables and the .env file
settings = Settings()
