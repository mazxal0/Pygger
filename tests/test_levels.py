from pygger import LogLevel


def test_names_of_levels():
    assert LogLevel.DEBUG.name == 'DEBUG'
    assert LogLevel.INFO.name == 'INFO'
    assert LogLevel.WARNING.name == 'WARNING'
    assert LogLevel.ERROR.name == 'ERROR'
    assert LogLevel.CRITICAL.name == 'CRITICAL'
