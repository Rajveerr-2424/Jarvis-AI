import random
import re
import secrets
import string

from tools.core.base import BaseTool


class PasswordTool(BaseTool):
    name = "Password Generator"
    description = "Generates secure random passwords."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "password",
        "generate password",
        "strong password",
        "random password",
    )

    DEFAULT_LENGTH = 12
    MIN_LENGTH = 4
    MAX_LENGTH = 128

    def execute(self, text: str) -> str:
        text = text.lower()

        match = re.search(r"\b(\d{1,3})\b", text)

        if match:
            length = int(match.group(1))
        else:
            length = self.DEFAULT_LENGTH

        if length < self.MIN_LENGTH:
            return (
                f"Password length must be at least "
                f"{self.MIN_LENGTH} characters."
            )

        if length > self.MAX_LENGTH:
            return (
                f"Password length cannot exceed "
                f"{self.MAX_LENGTH} characters."
            )

        characters_lower = string.ascii_lowercase
        characters_upper = string.ascii_uppercase
        characters_digits = string.digits
        characters_special = string.punctuation

        password = [
            secrets.choice(characters_lower),
            secrets.choice(characters_upper),
            secrets.choice(characters_digits),
            secrets.choice(characters_special),
        ]

        all_characters = (
            characters_lower
            + characters_upper
            + characters_digits
            + characters_special
        )

        password.extend(
            secrets.choice(all_characters)
            for _ in range(length - 4)
        )

        random.SystemRandom().shuffle(password)

        password = "".join(password)

        return (
            f"Generated Password ({length} characters)\n\n"
            f"{password}"
        )