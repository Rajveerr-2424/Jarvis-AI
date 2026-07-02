from typing import List

from brain.providers.gemini import GeminiProvider
from config.settings import settings


class BrainManager:
    def __init__(self):
        provider = getattr(settings, "AI_PROVIDER", "gemini").lower()

        if provider == "gemini":
            self.provider = GeminiProvider()
        else:
            raise ValueError(f"Unsupported AI provider: {provider}")

    def ask(self, messages: List[dict]) -> str:
        return self.provider.ask(messages)