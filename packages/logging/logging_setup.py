from collections.abc import Callable
from pathlib import Path
import functools
import logging
import logging.config

from packages.path_utility import get_project_root_path

@functools.lru_cache(maxsize=None)
def setup_base_logging() -> logging.Logger:
    """Setup base logging, including formatting (so logs are kept similar)

    Returns:
        logging.Logger: Configured logger, with level = logger_level
    """
    path_to_logging_conf = Path(
        get_project_root_path(), "packages", "logging", "logging.conf"
    )

    logging.config.fileConfig(
        str(path_to_logging_conf),
        disable_existing_loggers=False
    )

    return logging.getLogger("MLplayground")


def log_function_call(
        function : Callable,
        signature_level : int = logging.INFO,
        return_level : int = logging.DEBUG):
    """Wrapper for logging function calls

    Logs the function signature with level = signature_level, and the return
    value(s) with level = return_level. Set any of these to 0 to skip the 
    logging step.

    Args:
        function (Callable): Function that shall be logged. Given automatically
            if used as a wrapper
        logger (logging.Logger): Logger to use for logging.
        signature_level (int, optional): Logging level to use for logging the
            function signature. Defaults to logging.INFO
        return_level (int, optional): Logging level to use for logging the
            function return value(s). Defaults to logging.DEBUG
    
    Returns:
        Callable: Function that logs function-signature, runs function, logs
            the returned value, then returns the returned value
    """
    logger = setup_base_logging()

    @functools.wraps(function)
    def wrapper_log_function_call(*args, **kwargs):
        """Actual logging wrapper"""

        args_ = [repr(arg) for arg in args]
        kwargs_ = [f"{key}={value!r}" for key, value in kwargs.items()]
        signature = ", ".join(args_ + kwargs_)

        logger.log(
            signature_level,
            f"Calling {function.__name__} with signature: ({signature})"
        )

        return_value = function(*args, **kwargs)

        logger.log(
            return_level,
            f"{function.__name__!r} returned {return_value!r}"
        )
        return return_value
    
    return wrapper_log_function_call