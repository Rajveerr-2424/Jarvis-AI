from brain.client import Brain
from config.settings import settings
from core.logger import jarvis_logger
from ui.console import (
    show_banner,
    show_status,
    user_prompt,
    jarvis_response,
    error,
)


class Jarvis:
    def __init__(self):
        self.brain = Brain()
        jarvis_logger.info("Jarvis initialized.")

    def start(self):
        show_banner()
        show_status(settings.MODEL)

        jarvis_logger.info("Jarvis started successfully.")

        while True:
            user_input = user_prompt()

            jarvis_logger.info(f"User: {user_input}")

            if user_input.lower() in {"exit", "quit"}:
                jarvis_response("Goodbye, Sir.")
                jarvis_logger.info("Jarvis shutting down.")
                break

            try:
                response = self.brain.ask(user_input)

                jarvis_logger.info("Response generated successfully.")

                jarvis_response(response)

            except Exception as e:
                jarvis_logger.exception(str(e))
                error("Something went wrong.")