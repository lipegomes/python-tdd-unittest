def sum(x, y):
    """
    Sum x and y

    >>> sum(11, 11)
    22

    >>> sum(10, 20)
    30

    """
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return x + y


def subtraction(x, y):
    """
    Subtraction x and y

    >>> subtraction(-20, 80)
    -100
    """
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return x - y


def multiplication(x, y):
    """
    Multiplication x and y

    >>> multiplication('25', 10)
    Traceback (most recent call last):
    ...
    AssertionError: The x value must be an int or float

     >>> multiplication(5, 10)
     50
    """
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return x * y


def division(x, y):
    """
    Division x and y

    >>> division(2048, 64)
    32.0

    """
    assert isinstance(x, (int, float)), "The numerator value must be an int or float"
    assert isinstance(y, (int, float)), "The denominator value must be greater than zero"
    return x / y


def exponentiation(x, y):
    """
    Exponentiation x and y

    >>> exponentiation(2, -3)
    0.125
    """
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return x ** y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
