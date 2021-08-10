import pytest

from packages.functools.decorators import (
    simplecache
)


@pytest.fixture
def cached_function():
    """Create a function wrapped with @simplecache"""
    @simplecache
    def function():
        return 42
    return function


def test_simplecache_sets_cache(cached_function):
    """Test that simplecache caches the result"""
    assert not hasattr(cached_function, "_cache")
    cached_function()
    assert hasattr(cached_function, "_cache")


def test_simplecache_cache_has_right_value(cached_function):
    """Test that cache is set with the correct value"""
    cached_function()
    assert cached_function._cache == cached_function()


def test_simplecache_returns_cached_value(cached_function):
    """Test that cached function actually returns the cached value"""
    cached_function()
    cached_function._cache = "Hello"
    assert cached_function() == "Hello"


def test_simplecache_cache_does_not_bleed(cached_function):
    """Test that simplecache creates a new cache for each cached function"""
    cached_function()

    @simplecache
    def other_cached_function():
        return "Hello"
    
    other_cached_function()

    assert cached_function() == 42
    assert cached_function._cache == cached_function()

    assert other_cached_function() == "Hello"
    assert other_cached_function._cache == other_cached_function()
