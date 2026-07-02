from collections import deque


class ConversationManager:
    """
    Maintains the current conversation context.

    This is short-term memory only.
    """

    def __init__(self, max_messages: int = 10):
        self.history = deque(maxlen=max_messages)

    def add_user_message(self, message: str):
        self.history.append(
            {
                "role": "user",
                "content": message,
            }
        )

    def add_assistant_message(self, message: str):
        self.history.append(
            {
                "role": "assistant",
                "content": message,
            }
        )

    def build_prompt(self, current_message: str) -> str:
        prompt = ""

        for message in self.history:
            role = message["role"].capitalize()
            prompt += f"{role}: {message['content']}\n"

        prompt += f"User: {current_message}"

        return prompt

    def clear(self):
        self.history.clear()