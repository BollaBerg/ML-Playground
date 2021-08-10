import logging

from packages.logging.logging_setup import get_logger


def test_get_logger_returns_Logger_instance():
    """Test that get_logger returns an instance of logging.Logger"""
    logger = get_logger("NAME")
    assert isinstance(logger, logging.Logger)


def test_get_logger_returns_logger_with_correct_parent():
    """Test that get_logger returns a child of playground - our root logger"""
    logger = get_logger("NAME")
    assert logger.name == "playground.NAME"