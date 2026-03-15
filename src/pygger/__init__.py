from .levels import LogLevel
from .logger import Logger


try:
    import colorama
    colorama.init()
except ImportError:
    pass


__all__ = [
    'LogLevel',
    'Logger',
]

__version__ = '0.1.0'
