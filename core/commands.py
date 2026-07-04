import os
import platform

from rich.table import Table

from config.settings import settings
from ui.console import console


class CommandHandler:
    def __init__(self, assistant):
        self.assistant = assistant

    def execute(self, command: str):
        command = command.strip().lower()

        if command == "/help":
            self.help()
            return "handled"

        if command == "/status":
            self.status()
            return "handled"

        if command == "/provider":
            self.provider()
            return "handled"

        if command == "/model":
            self.model()
            return "handled"

        if command == "/memory":
            self.memory()
            return "handled"

        if command.startswith("/forget "):
            key = command.split(maxsplit=1)[1]

            if key == "all":
                self.assistant.memory_service.forget_all()

                console.print(
                    "\n[green]All memories deleted.[/green]\n"
                )

            else:
                self.assistant.memory_service.forget(key)

                console.print(
                    f"\n[green]Deleted memory '{key}'.[/green]\n"
                )

            return "handled"

        if command == "/history":
            self.history()
            return "handled"

        if command == "/version":
            self.version()
            return "handled"

        if command == "/clear":
            self.clear_chat()
            return "handled"

        if command == "/cls":
            os.system("cls" if os.name == "nt" else "clear")
            return "handled"
        
        if command == "/tools":
            self.tools()
            return "handled"

        if command == "/exit":
            return "exit"

        return None

    def help(self):
        table = Table(title="JARVIS Commands")

        table.add_column("Command", style="cyan")
        table.add_column("Description", style="green")

        table.add_row("/help", "Show all commands")
        table.add_row("/status", "Show Jarvis status")
        table.add_row("/provider", "Current provider mode")
        table.add_row("/model", "Current AI model")
        table.add_row("/memory", "Show stored memories")
        table.add_row("/forget <key>", "Delete a memory")
        table.add_row("/forget all", "Delete all memories")
        table.add_row("/history", "Show conversation history")
        table.add_row("/version", "Show version information")
        table.add_row("/clear", "Clear conversation history")
        table.add_row("/cls", "Clear terminal")
        table.add_row("/tools", "Show available tools")
        table.add_row("/exit", "Exit Jarvis")

        console.print(table)

    def status(self):
        table = Table(title="System Status")

        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        if settings.AI_PROVIDER == "auto":
            table.add_row("Provider Mode", "Auto")
            table.add_row("Primary", "Ollama")
            table.add_row("Fallback", "Gemini")
            table.add_row("Current", self.assistant.brain.current_provider)
        else:
            table.add_row("Provider", settings.AI_PROVIDER)
            table.add_row("Current", self.assistant.brain.current_provider)

        table.add_row("Model", self.assistant.brain.current_model)
        table.add_row("Memory", "Enabled")
        table.add_row("Voice", "Disabled")

        console.print(table)

    def provider(self):
        table = Table(title="Provider Information")

        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Mode", settings.AI_PROVIDER)
        table.add_row("Current", self.assistant.brain.current_provider)

        if settings.AI_PROVIDER == "auto":
            table.add_row("Primary", "Ollama")
            table.add_row("Fallback", "Gemini")

        console.print(table)

    def model(self):
        console.print(
            f"\n[cyan]Current Model:[/cyan] {self.assistant.brain.current_model}\n"
        )

    def memory(self):
        memories = self.assistant.memory_service.list_memories()

        table = Table(title="Stored Memories")

        table.add_column("Category", style="cyan")
        table.add_column("Key", style="green")
        table.add_column("Value", style="yellow")

        if not memories:
            console.print("\n[yellow]No memories stored.[/yellow]\n")
            return

        for row in memories:
            table.add_row(
                row["category"],
                row["key"],
                row["value"],
            )

        console.print(table)

    def history(self):
        table = Table(title="Conversation History")

        table.add_column("Role", style="cyan")
        table.add_column("Message", style="white")

        if not self.assistant.conversation.messages:
            console.print(
                "\n[yellow]Conversation history is empty.[/yellow]\n"
            )
            return

        for message in self.assistant.conversation.messages:
            table.add_row(
                message["role"],
                message["parts"][0]["text"],
            )

        console.print(table)

    def version(self):
        table = Table(title="JARVIS Version")

        table.add_column("Property", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Version", "0.3")
        table.add_row("Provider Mode", settings.AI_PROVIDER)
        table.add_row("Current Provider", self.assistant.brain.current_provider)
        table.add_row("Model", self.assistant.brain.current_model)
        table.add_row("Python", platform.python_version())
        table.add_row("Platform", platform.system())

        console.print(table)

    def clear_chat(self):
        self.assistant.conversation.clear()

        console.print(
            "\n[green]Conversation history cleared.[/green]\n"
        )

    def tools(self):
        table = Table(title="JARVIS Tool Catalog")

        table.add_column("Name", style="cyan")
        table.add_column("Enabled", style="green", justify="center")
        table.add_column("Version", style="yellow")
        table.add_column("Description", style="white")

        tools = self.assistant.tools.list_tools()

        if not tools:
            console.print(
                "\n[yellow]No tools registered.[/yellow]\n"
            )
            return

        for tool in tools:
            table.add_row(
                tool.name,
                "Yes" if tool.enabled else "No",
                tool.version,
                tool.description,
            )

        console.print(table)