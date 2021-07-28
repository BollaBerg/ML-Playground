from collections.abc import Callable
import functools
import logging

from packages.logging import get_logger

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
    logger = get_logger()

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