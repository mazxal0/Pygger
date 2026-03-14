from datetime import datetime
from dataclasses import dataclass, field

from .levels import LogLevel


@dataclass(slots=True)
class Record:
    level: LogLevel
    message: str
    name: str
    timestamp: datetime = field(default_factory=datetime.now)
