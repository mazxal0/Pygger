from typing import Optional

from .colors import LEVEL_COLORS, Colors
from .record import Record


class Formatter:
    def __init__(self, template: Optional[str] = None, use_color: bool = True) -> None:
        self.template = template or "[{timestamp}] {level} [{name}] {message}"
        self.use_color = use_color

    def __call__(self, record: Record) -> str:
        return self.format(record)

    def set_template(self, template: Optional[str] = None) -> None:
        if template is None:
            return None
        self.template = template

    def format(self, record: Record) -> str:
        level_name = record.level.name if hasattr(record.level, "name") else str(record.level)

        color = LEVEL_COLORS.get(level_name, Colors.RESET)
        level_colored = f"{color}[{level_name}]{Colors.RESET}" if self.use_color else f'[{level_name}]'

        return self.template.format(
            timestamp=record.timestamp,
            level=level_colored,
            name=record.name,
            message=record.message,
        )
