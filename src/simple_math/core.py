
"""
Core math utilities for TDD practice.

All functions use basic `float` types only.
"""

from typing import List

def add(a: float, b: float) -> float:
    """
    Return the sum of two numbers.

    Examples:
        >>> add(1.5, 2.5)
        4.0
        >>> add(-3.0, 1.0)
        -2.0
    """
    return a+b


def safe_divide(a: float, b: float) -> float:

    if b==0:
        raise ValueError("denominator must not be zero")
    else:
        return a/b


def average(xs: List[float]) -> float:
    """
    Compute the arithmetic mean of a non-empty list of floats.

    Examples:
        >>> average([1.0, 3.0, 5.0])
        3.0
        >>> average([])
        Traceback (most recent call last):
            ...
        ValueError: xs must not be empty
    """
    if len (xs)==0:
        raise ValueError("xs must not be empty")
    else:
        return sum(xs)/len(xs)
