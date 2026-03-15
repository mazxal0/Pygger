from pygger import LogLevel


def test_names_of_levels():
    assert LogLevel.DEBUG.name == 'DEBUG'
    assert LogLevel.INFO.name == 'INFO'
    assert LogLevel.WARNING.name == 'WARNING'
    assert LogLevel.ERROR.name == 'ERROR'
    assert LogLevel.CRITICAL.name == 'CRITICAL'


def test_values_of_levels():
    assert isinstance(LogLevel.DEBUG.value, int)
    assert isinstance(LogLevel.INFO.value, int)
    assert isinstance(LogLevel.WARNING.value, int)
    assert isinstance(LogLevel.ERROR.value, int)
    assert isinstance(LogLevel.CRITICAL.value, int)
