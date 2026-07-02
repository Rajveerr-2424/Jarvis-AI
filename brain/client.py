from brain.gemini import GeminiBrain


class Brain:
    def __init__(self):
        self.provider = GeminiBrain()

    def ask(self, prompt: str) -> str:
        return self.provider.generate(prompt)