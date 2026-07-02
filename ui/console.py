from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

console = Console()

# Style for prompt_toolkit
style = Style.from_dict(
    {
        # Default typed text
        "": "#00FF7F",

        # Prompt
        "prompt": "bold #00BFFF",
    }
)

# Reuse one prompt session
session = PromptSession(style=style)


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]JARVIS AI[/bold cyan]\n"
            "[green]Version 0.2[/green]",
            border_style="cyan",
        )
    )


def show_status(provider: str):
    table = Table(show_header=False)

    table.add_row("🟢 Status", "[green]ONLINE[/green]")
    table.add_row("🧠 Provider", provider)
    table.add_row("💾 Memory", "[yellow]Disabled[/yellow]")
    table.add_row("🎤 Voice", "[yellow]Disabled[/yellow]")

    console.print(table)


def user_prompt():
    return session.prompt(
        [("class:prompt", "You > ")]
    )


def jarvis_response(text: str):
    console.print(
        "\n[bold bright_cyan]JARVIS>[/bold bright_cyan]"
    )

    console.print(
        f"[bright_cyan]{text}[/bright_cyan]\n"
    )


def info(text: str):
    console.print(f"[green]{text}[/green]")


def error(text: str):
    console.print(f"[bold red]{text}[/bold red]")