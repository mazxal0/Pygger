import pytest

from pygger import LogLevel
from pygger.record import Record
from pygger.handlers.base import BaseHandler
from pygger.handlers.console import ConsoleHandler
from pygger.handlers.null import NullHandler


def make_record():
    return Record(
        level=LogLevel.INFO,
        message="Hello handler",
        name="test_logger",
    )


def test_base_handler_is_abstract():
    with pytest.raises(TypeError):
        BaseHandler()


def test_null_handler_returns_none():
    handler = NullHandler()
    record = make_record()

    result = handler(record)

    assert result is None


def test_null_handler_prints_nothing(capsys):
    handler = NullHandler()
    record = make_record()

    handler(record)

    captured = capsys.readouterr()

    assert captured.out == ""


def test_console_handler_prints_formatted_record(capsys):
    handler = ConsoleHandler()
    record = make_record()

    handler(record)

    captured = capsys.readouterr()

    assert "Hello handler" in captured.out
    assert "INFO" in captured.out
    assert "test_logger" in captured.out
