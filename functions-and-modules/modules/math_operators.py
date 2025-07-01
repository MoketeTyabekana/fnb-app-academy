# This module provides basic mathematical operations.
# It includes functions for addition, subtraction, multiplication, division,
# exponentiation, square root, and factorial.


def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(base, exponent):
    """Returns base raised to the power of exponent."""
    return base ** exponent

def square_root(x):
    """Returns the square root of x. Raises ValueError if x is negative."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5

def factorial(n):
    """Returns the factorial of n. Raises ValueError if n is negative."""
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)