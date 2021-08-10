import logging
import pytest

from packages.logging.formatters import CustomFormatter

@pytest.fixture
def formatter():
    return CustomFormatter(
        fmt = "%(filename)s %(lineno)d"
    )

@pytest.fixture
def record():
    return logging.LogRecord(
        name="Test",
        level=logging.DEBUG,
        pathname=__file__,
        lineno=69,
        msg="TEST",
        args=None,
        exc_info=None
    )


def test_CustomFormatter_does_not_default_override_anything(formatter, record):
    """Test that CustomFormatter does not override anything by default"""
    formatted = formatter.format(record)
    assert formatted == f"{__name__}.py 69"


def test_CustomFormatter_overrides_filename(formatter, record):
    """Test that CustomFormatter overrides filename when specified"""
    record.filename_override = "new_filename.py"
    formatted = formatter.format(record)
    assert formatted == "new_filename.py 69"


def test_CustomFormatter_overrides_lineno(formatter, record):
    """Test that CustomFormatter overrides lineno when specified"""
    record.lineno_override = 420
    formatted = formatter.format(record)
    assert formatted == f"{__name__}.py 420"
