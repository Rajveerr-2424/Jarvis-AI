from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


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
    return console.input("[bold blue]You > [/bold blue]")


def jarvis_response(text: str):
    console.print(f"[bold cyan]Jarvis >[/bold cyan] {text}\n")


def info(text: str):
    console.print(f"[green]{text}[/green]")


def error(text: str):
    console.print(f"[bold red]{text}[/bold red]")