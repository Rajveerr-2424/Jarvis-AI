import re

from memory.repository import MemoryRepository


class MemoryService:
    def __init__(self):
        self.repository = MemoryRepository()
        self.repository.initialize()

    def process(self, text: str):
        text = text.strip()

        patterns = [
            (
                r"my name is (.+)",
                ("personal", "name"),
            ),
            (
                r"i am (.+)",
                ("personal", "name"),
            ),
            (
                r"my favourite language is (.+)",
                ("coding", "favorite_language"),
            ),
        ]

        for pattern, (category, key) in patterns:
            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:
                value = match.group(1).strip()

                self.repository.remember(
                    category,
                    key,
                    value,
                )

                return (
                    True,
                    f"Remembered your {key}, Sir."
                )

        return False, None
    
    def answer_from_memory(self, text: str):
        text = text.lower()

        if "what is my name" in text:
            value = self.repository.recall("name")

            if value:
                return value

        if "what is my favourite language" in text:
            value = self.repository.recall(
                "favorite_language"
            )

            if value:
                return value

        return None
    
    def list_memories(self):
        return self.repository.list_memories()


    def forget(self, key: str):
        self.repository.forget(key)


    def forget_all(self):
        self.repository.forget_all()