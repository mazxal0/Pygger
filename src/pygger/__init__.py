from .levels import LogLevel
from .logger import Logger
from .handlers import BaseHandler, ConsoleHandler
from .record import Record

try:
    import colorama
    colorama.init()
except ImportError:
    pass


__all__ = [
    'LogLevel',
    'Logger',
    'BaseHandler',
    'ConsoleHandler',
    'Record',
]

__version__ = '0.1.0'
