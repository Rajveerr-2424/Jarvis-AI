from brain.providers.gemini import GeminiProvider
from brain.providers.ollama import OllamaProvider
from config.settings import settings
from core.logger import jarvis_logger


class BrainManager:
    def __init__(self):
        self.providers = {
            "ollama": OllamaProvider(),
            "gemini": GeminiProvider(),
        }

        self.mode = settings.AI_PROVIDER.lower()

        # Runtime state
        self.current_provider = "None"
        self.current_model = "None"

    def ask(self, messages):
        if self.mode == "ollama":
            self.current_provider = "Ollama"
            self.current_model = settings.OLLAMA_MODEL

            return self.providers["ollama"].ask(messages)

        if self.mode == "gemini":
            self.current_provider = "Gemini"
            self.current_model = settings.GEMINI_MODEL

            return self.providers["gemini"].ask(messages)

        if self.mode == "auto":
            return self._auto(messages)

        raise ValueError(
            f"Unsupported provider mode: {self.mode}"
        )

    def _auto(self, messages):
        # -------------------------------
        # Primary Provider : Ollama
        # -------------------------------
        try:
            self.current_provider = "Ollama"
            self.current_model = settings.OLLAMA_MODEL

            jarvis_logger.info(
                "Trying provider: Ollama"
            )

            response = self.providers["ollama"].ask(messages)

            jarvis_logger.info(
                "Provider selected: Ollama"
            )

            return response

        except Exception as e:
            jarvis_logger.warning(
                f"Ollama unavailable ({e}). Falling back to Gemini."
            )

        # -------------------------------
        # Fallback Provider : Gemini
        # -------------------------------
        try:
            self.current_provider = "Gemini"
            self.current_model = settings.GEMINI_MODEL

            jarvis_logger.info(
                "Trying provider: Gemini"
            )

            response = self.providers["gemini"].ask(messages)

            jarvis_logger.info(
                "Provider selected: Gemini"
            )

            return response

        except Exception:
            jarvis_logger.exception(
                "All providers failed."
            )

            raise RuntimeError(
                "No AI providers are currently available."
            )