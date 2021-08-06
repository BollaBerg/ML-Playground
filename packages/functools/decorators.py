import functools
from typing import Callable

def simplecache(function: Callable) -> Callable:
    """Decorator to cache a return value from a function.

    The decorator only works if the function has only one possible return value.
    It does not care what arguments are passed, but only caches the result the
    first time the function is called. Then the cache value is used on later
    function calls.

    To remove the cache, delete the function's `_cache`-attribute.

    Usage:
        >>> @simplecache
        >>> def heavy_function():
        ...     return 42
    
    Remove the cache:
        >>> del heavy_function._cache

    Args:
        function (Callable): Function to wrap

    Returns:
        Callable: Wrapped function
    """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        if hasattr(wrapper, "_cache"):
            return wrapper._cache
        
        return_value = function(*args, **kwargs)

        wrapper._cache = return_value
        return return_value
    return wrapper
