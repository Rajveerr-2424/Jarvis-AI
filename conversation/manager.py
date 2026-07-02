from collections import deque
from typing import List


class ConversationManager:
    """
    Maintains the short-term conversation context.
    This context only exists during the current session.
    """

    def __init__(self, max_messages: int = 20):
        self.messages = deque(maxlen=max_messages)

    def add_user(self, text: str):
        self.messages.append(
            {
                "role": "user",
                "parts": [{"text": text}],
            }
        )

    def add_assistant(self, text: str):
        self.messages.append(
            {
                "role": "model",
                "parts": [{"text": text}],
            }
        )

    def build_messages(self, current_message: str) -> List[dict]:
        history = list(self.messages)

        history.append(
            {
                "role": "user",
                "parts": [{"text": current_message}],
            }
        )

        return history

    def clear(self):
        self.messages.clear()