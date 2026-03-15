from pygger import Logger, LogLevel

pygger = Logger(name='pygger', use_color=True)

pygger.log(message="Hello World!", level=LogLevel.WARNING)

pygger.error(message="Error, it's not good")
