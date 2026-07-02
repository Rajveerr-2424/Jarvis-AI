from typing import List

from ollama import Client

from brain.prompts import SYSTEM_PROMPT
from brain.providers.base import BaseProvider
from config.settings import settings


class OllamaProvider(BaseProvider):
    def __init__(self):
        self.client = Client(host=settings.OLLAMA_HOST)

    def ask(self, messages: List[dict]) -> str:
        ollama_messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

        for message in messages:
            role = message["role"]

            # Convert Gemini's "model" role to Ollama's "assistant"
            if role == "model":
                role = "assistant"

            text = message["parts"][0]["text"]

            ollama_messages.append(
                {
                    "role": role,
                    "content": text,
                }
            )

        response = self.client.chat(
            model=settings.OLLAMA_MODEL,
            messages=ollama_messages,
        )

        return response["message"]["content"]