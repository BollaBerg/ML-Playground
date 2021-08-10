"""
This file is intended to hold logging decorators, to wrap function calls.
"""
from collections.abc import Callable
import functools
import logging
from pathlib import Path
import inspect

def log_function_call(
        logger: logging.Logger,
        signature_level : int = logging.INFO,
        return_level : int = logging.DEBUG
    ):
    """Wrapper for logging function calls

    Logs the function signature with level = signature_level, and the return
    value(s) with level = return_level. Set any of these to 0 to skip the 
    logging step.

    Note: To be able to use arguments in the decorator, this function has two
    levels of sub-functions - log_function_call returns the actual decorator,
    which then returns the actual wrapper function. For more info, see here:
    https://stackoverflow.com/questions/5929107/decorators-with-parameters
    
    Uses extra arguments to log "from" the actual calling file. This enables
    the logger to work correctly while logging filename and line number, instead
    of always logging from "decorators.py, line 64".

    Args:
        logger (logging.Logger): Logger to use for logging the function call.
            Recommend using packages.logging.get_logger(__name__) to get logger.
        logger (logging.Logger): Logger to use for logging.
        signature_level (int, optional): Logging level to use for logging the
            function signature. Defaults to logging.INFO
        return_level (int, optional): Logging level to use for logging the
            function return value(s). Defaults to logging.DEBUG
    
    Returns:
        Callable: Function that logs function-signature, runs function, logs
            the returned value, then returns the returned value
    """
    def decorator(function: Callable):
        """Actual decorator

        Args:
            function (Callable): Function that shall be logged. Given
                automatically if used as a decorator
        """
        @functools.wraps(function)
        def wrapper_log_function_call(*args, **kwargs):
            """Actual logging wrapper"""

            args_ = [repr(arg) for arg in args]
            kwargs_ = [f"{key}={value!r}" for key, value in kwargs.items()]
            signature = ", ".join(args_ + kwargs_)

            extra_arguments = {
                # Override filename with filename of previous step in stack
                "filename_override": Path(inspect.stack()[1].filename).name,
                # Override lineno with line number of previous step in stack
                "lineno_override": inspect.stack()[1].lineno,
            }            

            logger.log(
                signature_level,
                f"Calling {function.__name__!r} with signature: ({signature})",
                extras=extra_arguments
            )

            return_value = function(*args, **kwargs)

            logger.log(
                return_level,
                f"{function.__name__!r} returned {return_value!r}",
                extras=extra_arguments
            )
            return return_value
        return wrapper_log_function_call
    return decorator
