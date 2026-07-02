from google import genai
from google.genai import types

from config.settings import settings
from brain.prompts import SYSTEM_PROMPT


class GeminiBrain:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=settings.MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=settings.TEMPERATURE,
                max_output_tokens=settings.MAX_OUTPUT_TOKENS,
            ),
        )

        return response.text