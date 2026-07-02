from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AI_PROVIDER: str = "ollama"

    GEMINI_API_KEY: str = ""

    GEMINI_MODEL: str = "gemini-2.5-flash"

    OLLAMA_HOST: str = "http://localhost:11434"

    OLLAMA_MODEL: str = "qwen2.5:3b"

    USER_NAME: str = "Rajveerr"

    ASSISTANT_NAME: str = "Jarvis"

    TEMPERATURE: float = 0.7

    MAX_OUTPUT_TOKENS: int = 2048

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()