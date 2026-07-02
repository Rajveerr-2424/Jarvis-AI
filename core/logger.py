from pathlib import Path

from loguru import logger
from rich.console import Console

console = Console()

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

# File logs (full details)
logger.add(
    LOG_DIR / "jarvis.log",
    rotation="10 MB",
    retention="30 days",
    level="DEBUG",
    enqueue=True,
)

# Console logs
logger.add(
    lambda msg: console.print(msg, end=""),
    level="INFO",
    colorize=True,
    format=(
        "[dim][{time:HH:mm:ss}][/dim] "
        # "[{level.icon}] "
        "[bold bright_blue]{level:<8}[/bold bright_blue] "
        "[dim]{module}:{function}:{line}[/dim] "
        "[dim]{message}[/dim]"
    ),
)

jarvis_logger = logger