from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Pydantic will look for POSTGRES_USER env var automatically
    postgres_db: str
    postgres_user: str
    postgres_password: str

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

CONFIG = Settings()
