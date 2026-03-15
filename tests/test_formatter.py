from pygger import LogLevel
from pygger.record import Record
from pygger.formatter import Formatter


def test_formatter_returns_string():
    formatter = Formatter(use_color=False)
    record = Record(
        level=LogLevel.INFO,
        message="Hello",
        name="test_logger",
    )

    result = formatter(record)

    assert isinstance(result, str)


def test_formatter_default_template_contains_main_fields():
    formatter = Formatter(use_color=False)
    record = Record(
        level=LogLevel.INFO,
        message="Hello",
        name="test_logger",
    )

    result = formatter(record)

    assert "Hello" in result
    assert "INFO" in result
    assert "test_logger" in result


def test_formatter_custom_template():
    formatter = Formatter(
        template="{level} - {message}",
        use_color=False,
    )
    record = Record(
        level=LogLevel.ERROR,
        message="Boom",
        name="core",
    )

    result = formatter(record)
    print(result)
    assert result == "ERROR - Boom"


def test_formatter_set_template():
    formatter = Formatter(template="{message}", use_color=False)
    formatter.set_template("{level}: {message}")

    record = Record(
        level=LogLevel.WARNING,
        message="Watch out",
        name="test",
    )

    result = formatter(record)

    assert result == "WARNING: Watch out"


def test_formatter_set_template_none_does_not_change_template():
    formatter = Formatter(template="{message}", use_color=False)

    formatter.set_template(None)

    assert formatter.template == "{message}"
