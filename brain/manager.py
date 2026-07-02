from brain.providers.gemini import GeminiProvider
from brain.providers.ollama import OllamaProvider
from config.settings import settings


class BrainManager:
    def __init__(self):
        provider = settings.AI_PROVIDER.lower()

        if provider == "gemini":
            self.provider = GeminiProvider()

        elif provider == "ollama":
            self.provider = OllamaProvider()

        else:
            raise ValueError(
                f"Unsupported AI provider: {provider}"
            )

    def ask(self, messages):
        return self.provider.ask(messages)