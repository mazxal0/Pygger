from typing import Optional

from .base import BaseHandler
from ..formatter import Formatter


class ConsoleHandler(BaseHandler):
    def __init__(self, formatter: Optional[Formatter] = None) -> None:
        super().__init__(formatter)

    def emit(self, message: str) -> None:
        print(message)
