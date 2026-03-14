from pygger import Logger, LogLevel

pygger = Logger(name='pygger')

pygger.log(message="Hello World!", level=LogLevel.WARNING)

pygger.error(message="Error, it's not good")


@pygger.trace
def add(a: int, b: int) -> int:
    return a + b


add(10, 5)
