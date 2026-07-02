from dataclasses import dataclass
from datetime import datetime


@dataclass
class Memory:
    key: str
    value: str
    category: str
    created_at: datetime | None = None
    updated_at: datetime | None = None