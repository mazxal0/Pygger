from typing import Optional
from .record import Record


class Formatter:
    def __init__(self, template: Optional[str] = None) -> None:
        self.template = template or "[{timestamp}] [{level}] [{name}] [{message}]"

    def __call__(self, record: Record) -> str:
        return self.format(record)

    def set_template(self, template: Optional[str] = None) -> None:
        if template is None:
            return None
        self.template = template

    def format(self, record: Record) -> str:
        return self.template.format(
            timestamp=record.timestamp,
            level=record.level,
            name=record.name,
            message=record.message,
        )
