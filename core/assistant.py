from brain.manager import BrainManager
from config.settings import settings
from conversation.manager import ConversationManager
from core.commands import CommandHandler
from core.logger import jarvis_logger
from memory.service import MemoryService
from ui.console import (
    error,
    jarvis_response,
    show_banner,
    show_status,
    user_prompt,
)

from tools.core.manager import ToolManager


class Jarvis:
    def __init__(self):
        self.brain = BrainManager()
        self.conversation = ConversationManager()
        self.memory_service = MemoryService()
        self.commands = CommandHandler(self)

        # Tool Manager loads all tools from ToolRegistry
        self.tools = ToolManager()

        jarvis_logger.info("Jarvis initialized.")

    def start(self):
        show_banner()
        show_status(settings.AI_PROVIDER.capitalize())

        jarvis_logger.info("Jarvis started successfully.")

        while True:
            user_input = user_prompt()

            # --------------------------------------------------
            # Slash Commands
            # --------------------------------------------------
            if user_input.startswith("/"):
                action = self.commands.execute(user_input)

                if action == "exit":
                    jarvis_response("Goodbye, Sir.")
                    jarvis_logger.info("Jarvis shutting down.")
                    break

                if action == "handled":
                    continue

            jarvis_logger.info(f"User: {user_input}")

            # --------------------------------------------------
            # Normal Exit
            # --------------------------------------------------
            if user_input.lower() in {"exit", "quit"}:
                jarvis_response("Goodbye, Sir.")
                jarvis_logger.info("Jarvis shutting down.")
                break

            try:
                # --------------------------------------------------
                # Tools
                # --------------------------------------------------
                tool, tool_response = self.tools.process(user_input)

                if tool_response:
                    jarvis_logger.info(
                        f"Tool '{tool.name}' handled request."
                    )

                    jarvis_response(tool_response)
                    continue

                # --------------------------------------------------
                # Persistent Memory Recall
                # --------------------------------------------------
                memory_answer = self.memory_service.answer_from_memory(
                    user_input
                )

                if memory_answer:
                    jarvis_logger.info(
                        "Answer served from persistent memory."
                    )

                    jarvis_response(memory_answer)
                    continue

                # --------------------------------------------------
                # Persistent Memory Save
                # --------------------------------------------------
                remembered, reply = self.memory_service.process(
                    user_input
                )

                if remembered:
                    jarvis_logger.info(
                        "New memory stored."
                    )

                    jarvis_response(reply)
                    continue

                # --------------------------------------------------
                # AI Conversation
                # --------------------------------------------------
                messages = self.conversation.build_messages(
                    user_input
                )

                response = self.brain.ask(messages)

                self.conversation.add_user(user_input)
                self.conversation.add_assistant(response)

                jarvis_logger.info(
                    "Response generated successfully."
                )

                jarvis_response(response)

            except Exception as e:
                jarvis_logger.exception(
                    f"Unhandled exception: {e}"
                )

                error(
                    "Sorry Sir, something went wrong while processing your request."
                )