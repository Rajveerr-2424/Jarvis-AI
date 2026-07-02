from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    MODEL: str = "gemini-2.5-flash"

    USER_NAME: str = "Sir"
    ASSISTANT_NAME: str = "Jarvis"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()