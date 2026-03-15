from .base import BaseHandler


class NullHandler(BaseHandler):
    """Handler that discards all log messages."""

    def emit(self, message: str) -> None:
        pass
