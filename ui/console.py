from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Prompt Toolkit Style
style = Style.from_dict(
    {
        "": "#00FF7F",             # User input
        "prompt": "bold #00BFFF",  # Prompt
    }
)

session = PromptSession(style=style)


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]JARVIS AI[/bold cyan]\n"
            "[green]Version 0.3[/green]",
            border_style="cyan",
        )
    )


def show_status(provider: str):
    table = Table(show_header=False)

    table.add_row("🟢 Status", "[green]ONLINE[/green]")
    table.add_row("🧠 Provider", f"[cyan]{provider}[/cyan]")
    table.add_row("💾 Memory", "[green]Enabled[/green]")
    table.add_row("🎤 Voice", "[yellow]Disabled[/yellow]")
    table.add_row("🛠 Tools", "[green]Enabled[/green]")

    console.print(table)


def user_prompt():
    return session.prompt(
        [("class:prompt", "You > ")]
    )


def jarvis_response(text: str):
    console.print()

    console.print(
        "[bold bright_cyan]JARVIS >[/bold bright_cyan]"
    )

    console.print(
        f"[bright_cyan]{text}[/bright_cyan]"
    )

    console.print()


def info(text: str):
    console.print(
        f"[green]{text}[/green]"
    )


def warning(text: str):
    console.print(
        f"[yellow]{text}[/yellow]"
    )


def error(text: str):
    console.print(
        f"[bold red]{text}[/bold red]"
    )