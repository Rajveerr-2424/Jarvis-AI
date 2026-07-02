from brain.manager import BrainManager
from config.settings import settings
from conversation.manager import ConversationManager
from core.logger import jarvis_logger
from memory.service import MemoryService
from ui.console import (
    error,
    jarvis_response,
    show_banner,
    show_status,
    user_prompt,
)


class Jarvis:
    def __init__(self):
        self.brain = BrainManager()
        self.conversation = ConversationManager()
        self.memory_service = MemoryService()

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
                # --------------------------------------------------
                # 1. Check persistent memory first
                # --------------------------------------------------
                memory_answer = self.memory_service.answer_from_memory(
                    user_input
                )

                if memory_answer:
                    jarvis_logger.info("Answer served from memory.")
                    jarvis_response(memory_answer)
                    continue

                # --------------------------------------------------
                # 2. Save new memories
                # --------------------------------------------------
                remembered, reply = self.memory_service.process(
                    user_input
                )

                if remembered:
                    jarvis_logger.info("New memory stored.")
                    jarvis_response(reply)
                    continue

                # --------------------------------------------------
                # 3. AI Conversation
                # --------------------------------------------------
                messages = self.conversation.build_messages(
                    user_input
                )

                response = self.brain.ask(messages)

                self.conversation.add_user(user_input)
                self.conversation.add_assistant(response)

                jarvis_logger.info("Response generated successfully.")

                jarvis_response(response)

            except Exception as e:
                jarvis_logger.exception(
                    f"Unhandled exception: {e}"
                )

                error(
                    "Sorry Sir, something went wrong while processing your request."
                )