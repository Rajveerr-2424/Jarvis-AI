from brain.client import Brain
from config.settings import settings


class Jarvis:
    def __init__(self):
        self.brain = Brain()

    def start(self):
        print(f"\nGood day, {settings.USER_NAME}.")
        print(f"{settings.ASSISTANT_NAME} is online.\n")

        while True:
            user_input = input("You > ")

            if user_input.lower() in {"exit", "quit"}:
                print("\nGoodbye, Sir.")
                break

            response = self.brain.ask(user_input)

            print(f"\nJarvis > {response}\n")