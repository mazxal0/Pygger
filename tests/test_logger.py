from pygger import Logger, LogLevel, BaseHandler
from pygger.record import Record


class FakeHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.records = []

    def __call__(self, record):
        self.records.append(record)

    def emit(self, record):
        self.records.append(record)


def test_logger_has_name():
    logger = Logger(name="test_logger")

    assert logger.name == "test_logger"


def test_logger_is_enabled_by_default():
    logger = Logger(name="test_logger")

    assert logger.enabled is True


def test_logger_can_be_disabled_in_constructor():
    logger = Logger(name="test_logger", enabled=False)

    assert logger.enabled is False


def test_logger_log_sends_record_to_handler():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger.log("Hello", LogLevel.INFO)

    assert len(handler.records) == 1
    record = handler.records[0]

    assert isinstance(record, Record)
    assert record.name == "test_logger"
    assert record.message == "Hello"
    assert record.level == LogLevel.INFO


def test_logger_call_uses_log():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger("Hello from call", LogLevel.WARNING)

    assert len(handler.records) == 1
    record = handler.records[0]

    assert record.message == "Hello from call"
    assert record.level == LogLevel.WARNING


def test_logger_info_method():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger.info("Info message")

    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.INFO
    assert handler.records[0].message == "Info message"


def test_logger_warning_method():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger.warning("Warning message")

    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.WARNING
    assert handler.records[0].message == "Warning message"


def test_logger_error_method():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger.error("Error message")

    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.ERROR
    assert handler.records[0].message == "Error message"


def test_logger_critical_method():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger.critical("Critical message")

    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.CRITICAL
    assert handler.records[0].message == "Critical message"


def test_logger_debug_method():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    logger.debug("Debug message")

    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.DEBUG
    assert handler.records[0].message == "Debug message"


def test_logger_does_not_log_when_disabled():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler], enabled=False)

    logger.info("Should not be logged")

    assert len(handler.records) == 0


def test_logger_enabled_setter_works():
    logger = Logger(name="test_logger")

    logger.enabled = False
    assert logger.enabled is False

    logger.enabled = True
    assert logger.enabled is True


def test_logger_turn_changes_enabled_state():
    logger = Logger(name="test_logger")

    logger.turn(False)
    assert logger.enabled is False

    logger.turn(True)
    assert logger.enabled is True


def test_logger_trace_logs_function_call():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    @logger.trace
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5
    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.INFO
    assert "Calling the function add(a=2, b=3)" == handler.records[0].message


def test_logger_trace_does_not_log_when_disabled():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler], enabled=False)

    @logger.trace
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5
    assert len(handler.records) == 0


def test_logger_time_logs_execution_time():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    @logger.time()
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5
    assert len(handler.records) == 1
    assert handler.records[0].level == LogLevel.INFO
    assert "Time if calling the function add is" in handler.records[0].message
    assert "seconds" in handler.records[0].message


def test_logger_time_with_precision_logs_execution_time():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    @logger.time(precision=3)
    def add(a, b):
        return a + b

    result = add(2, 3)

    assert result == 5
    assert len(handler.records) == 1
    assert "Time if calling the function add is" in handler.records[0].message


def test_logger_trace_class_decorates_all_methods():
    handler = FakeHandler()
    logger = Logger(name="test_logger", handlers=[handler])

    @logger.trace_class
    class MathOps:
        def add(self, a, b):
            return a + b

        def sub(self, a, b):
            return a - b

    obj = MathOps()

    assert obj.add(5, 2) == 7
    assert obj.sub(5, 2) == 3

    assert len(handler.records) == 2
    assert "Calling the function add(self=" in handler.records[0].message
    assert "Calling the function sub(self=" in handler.records[1].message
