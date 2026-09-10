from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


project_root = Path(__file__).parents[3]

class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        env_file=Path.joinpath(project_root, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
        )

    #GROQ_API_KEY: str


settings = Settings()