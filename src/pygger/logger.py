from time import time
from typing import Optional
from functools import wraps

from .levels import LogLevel
from .record import Record
from .formatter import Formatter


class Logger:
    def __init__(
            self,
            name: str,
            template: Optional[str] = None
    ):
        self.name = name
        self.formatter = Formatter(template=template)
        self._enabled = True

    def __call__(self, message: str, level: LogLevel = LogLevel.INFO):
        self.log(message, level)

    def log(self, message: str, level: LogLevel = LogLevel.INFO):
        record = Record(
            name=self.name,
            message=message,
            level=level,
        )

        form_record = self.formatter(record)

        print(form_record)

    def info(self, message: str):
        self.log(message, LogLevel.INFO)

    def warning(self, message: str):
        self.log(message, LogLevel.WARNING)

    def error(self, message: str):
        self.log(message, LogLevel.ERROR)

    def critical(self, message: str):
        self.log(message, LogLevel.CRITICAL)

    def debug(self, message: str):
        self.log(message, LogLevel.DEBUG)

    @property
    def enabled(self):
        return self._enabled

    def turn(self, enabled: bool):
        self._enabled = enabled

    def trace(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if self.enabled:
                self.info(f'Calling the function {func.__name__}')
            return result

        return wrapper

    def time(self, precision=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time()
                result = func(*args, **kwargs)
                end = time()
                if self.enabled:
                    self.info(f'Time if calling the function {func.__name__} is '
                              f'{round(end - start, precision) if precision else end - start} seconds')
                return result

            return wrapper

        return decorator
