# Pygger
This is python logger for my education project


I decide to create own logger because in the near future I want to start write own library of algorithms and structure of data, and so I need to custom logger

### Current version
0.1.2

## Realization
- Log of levels: (Debug, Info and etc)
- Record class
- Formatter class
- Logger class

## Installation
this method can not work, because I will plan the upload the project to pip
```bash
    pip install pygger
```

or git

```bash
    git clone https://github.com/mazxal/pygger
    cd pygger
    uv sync
```

## Quick Example of code

```python
from pygger import Logger, LogLevel

pygger = Logger(name='pygger')

pygger.log(message="Hello World!", level=LogLevel.WARNING)

pygger.error(message="Error, it's not good")


@pygger.trace
def add(a: int, b: int) -> int:
    return a + b


add(5, 8)
```

## Example Output

```text
[2026-03-14 22:54:53.566210] [WARNING] [pygger] [Hello World!]
[2026-03-14 22:54:53.567221] [ERROR] [pygger] [Error, it's not good]
[2026-03-14 22:54:53.567221] [INFO] [pygger] [Calling the function add]
```

## Log Levels
- INFO = 20: level which shows some information
- DEBUG = 10: level which uses to debug system code
- WARNING = 30: level alert the maybe error
- ERROR = 40: the error level
- CRITICAL = 50: infrastructure crashed

## Architecture

#### The library has several of main components:

- **LogLevel** - contains level of logs
- **Record** - store information about one record
- **Formatter** - object which get record-object and return string
- **Logger** - main object which connect other entities and logs the events

## Roadmap

now I haven't any plans for the future of this library

## License

MIT