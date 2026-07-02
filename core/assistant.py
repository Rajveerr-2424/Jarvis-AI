from brain.manager import BrainManager
from config.settings import settings
from core.logger import jarvis_logger
from ui.console import (
    show_banner,
    show_status,
    user_prompt,
    jarvis_response,
    error,
)
from conversation.manager import ConversationManager
from memory.repository import MemoryRepository



class Jarvis:
    def __init__(self):
        self.brain = BrainManager()
        self.conversation = ConversationManager()

        self.memory = MemoryRepository()
        self.memory.initialize()

        jarvis_logger.info("Jarvis initialized.")

    def start(self):
        show_banner()
        show_status(settings.AI_PROVIDER.capitalize())

        jarvis_logger.info("Jarvis started successfully.")

        while True:
            user_input = user_prompt()

            jarvis_logger.info(f"User: {user_input}")

            if user_input.lower() in {"exit", "quit"}:
                jarvis_response("Goodbye, Sir.")
                jarvis_logger.info("Jarvis shutting down.")
                break

            try:
                messages = self.conversation.build_messages(user_input)

                response = self.brain.ask(messages)

                self.conversation.add_user(user_input)
                self.conversation.add_assistant(response)

                jarvis_logger.info("Response generated successfully.")

                jarvis_response(response)

            except Exception as e:
                jarvis_logger.exception(str(e))
                error("Something went wrong.")