from typing import Optional

from .colors import LEVEL_COLORS, Colors
from .record import Record


class Formatter:
    def __init__(self, template: Optional[str] = None, use_color: bool = True, precision_of_milliseconds: int = 3) -> None:
        self.template = template or "[{timestamp}] {level_tag} [{name}] {message}"
        self.use_color = use_color
        self.precision_of_milliseconds = precision_of_milliseconds

    def __call__(self, record: Record) -> str:
        return self.format(record)

    def set_template(self, template: Optional[str] = None) -> None:
        if template is None:
            return None
        self.template = template

    def format(self, record: Record) -> str:
        level_name = record.level.name if hasattr(record.level, "name") else str(record.level)

        color = LEVEL_COLORS.get(level_name, Colors.RESET)

        if self.use_color:
            level = f"{color}{level_name}{Colors.RESET}"
            level_tag = f"{color}[{level_name}]{Colors.RESET}"
        else:
            level = level_name
            level_tag = f"[{level_name}]"

        timestamp = record.timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")[:-self.precision_of_milliseconds]

        return self.template.format(
            timestamp=timestamp,
            level=level,
            level_tag=level_tag,
            name=record.name,
            message=record.message,
        )
