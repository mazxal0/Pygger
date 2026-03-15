from pygger import Record, LogLevel


def test_record_creation():
    record = Record(
        level=LogLevel.DEBUG,
        message='test message',
        name='test_logger'
    )

    assert record.level == LogLevel.DEBUG
    assert record.message == 'test message'
    assert record.name == 'test_logger'
    assert record.timestamp is not None
