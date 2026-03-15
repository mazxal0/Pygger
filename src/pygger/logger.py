from time import time
from typing import Optional, List
from functools import wraps
import inspect

from .handlers.base import BaseHandler
from .levels import LogLevel
from .record import Record


class Logger:
    def __init__(
            self,
            name: str,
            handlers: Optional[List[BaseHandler]] = None,
            enabled: bool = True,
    ):
        self.name = name
        self.handlers = handlers or []
        self._enabled = enabled

    def __call__(self, message: str, level: LogLevel = LogLevel.INFO):
        self.log(message, level)

    def log(self, message: str, level: LogLevel = LogLevel.INFO):
        if not self.enabled:
            return

        record = Record(
            name=self.name,
            message=message,
            level=level,
        )

        for handler in self.handlers:
            handler(record)

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

    @enabled.setter
    def enabled(self, enabled: bool):
        self._enabled = enabled

    def turn(self, enabled: bool):
        self._enabled = enabled

    def trace(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if self.enabled:
                sig = inspect.signature(func)
                bound = sig.bind(*args, **kwargs)
                bound.apply_defaults()

                params = ", ".join(f"{k}={v}" for k, v in bound.arguments.items())
                self.info(f'Calling the function {func.__name__}({params})')
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

    def trace_class(self, cls):
        funcs = inspect.getmembers(cls, predicate=inspect.isfunction)

        for name, func in funcs:
            if name.startswith('__') and name.endswith('__'):
                continue
            decorated = self.trace(func)
            setattr(cls, name, decorated)

        return cls
