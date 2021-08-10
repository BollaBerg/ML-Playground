import logging
import pytest

from packages.logging.decorators import log_function_call

@pytest.fixture
def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger


def test_log_function_call_logs_function_call(logger, caplog):
    """Test that decorator log_function_call logs with default values"""
    @log_function_call(logger)
    def logged_function(arg):
        return 42
    
    logged_function(69)
    assert "logged_function" in caplog.text
    assert "(69)" in caplog.text
    assert "returned 42" in caplog.text

def test_log_function_call_with_custom_signature_level(logger, caplog):
    """Test that decorator log_function_call uses argument signature_level"""
    @log_function_call(logger, signature_level=logging.CRITICAL)
    def logged_function(arg):
        return 42
    
    logged_function(69)
    signature_record = caplog.records[0]
    assert signature_record.levelname == "CRITICAL"
    assert "logged_function" in signature_record.msg
    assert "(69)" in signature_record.msg

def test_log_function_call_with_custom_return_level(logger, caplog):
    """Test that decorator log_function_call uses argument return_level"""
    @log_function_call(logger, return_level=logging.CRITICAL)
    def logged_function(arg):
        return 42
    
    logged_function(69)
    return_record = caplog.records[1]
    assert return_record.levelname == "CRITICAL"
    assert "logged_function" in return_record.msg
    assert "42" in return_record.msg