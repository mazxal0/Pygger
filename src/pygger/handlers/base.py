from abc import ABC, abstractmethod
from typing import Optional

from ..formatter import Formatter
from ..record import Record


class BaseHandler(ABC):

    def __init__(self, formatter: Optional[Formatter] = None) -> None:
        self.formatter = formatter or Formatter()

    def __call__(self, record: Record) -> None:
        message = self.format(record)
        self.emit(message)

    def format(self, record: Record) -> str:
        """Formatting logs record"""
        return self.formatter(record)

    @abstractmethod
    def emit(self, message: str) -> None:
        """Writes logs message"""
        pass
