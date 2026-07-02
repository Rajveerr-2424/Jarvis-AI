from typing import List

from google import genai
from google.genai import types

from brain.prompts import SYSTEM_PROMPT
from brain.providers.base import BaseProvider
from config.settings import settings


class GeminiProvider(BaseProvider):
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def ask(self, messages: List[dict]) -> str:
        response = self.client.models.generate_content(
            model=settings.MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=settings.TEMPERATURE,
                max_output_tokens=settings.MAX_OUTPUT_TOKENS,
            ),
        )

        return response.text or ""