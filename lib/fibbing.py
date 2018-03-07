from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """Return the nth fibonacci number

    :param n: nth fib number index
    :return: nth fib number

    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(6)
    13
    """
    if n < 3:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
