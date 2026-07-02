from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GEMINI_API_KEY: str

    MODEL: str = "gemini-2.5-flash"

    AI_PROVIDER: str = "gemini"

    USER_NAME: str = "Rajveerr"

    ASSISTANT_NAME: str = "Jarvis"

    TEMPERATURE: float = 0.7

    MAX_OUTPUT_TOKENS: int = 2048

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()