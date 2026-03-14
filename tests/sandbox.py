from pygger import Logger, LogLevel

pygger = Logger(name='pyg')

pygger.log(message="Hello World!", level=LogLevel.WARNING)


@pygger.time(precision=2)
def add(n):
    return [1e10 for _ in range(n)]


add(1000)
add(30000)
add(50000022)
