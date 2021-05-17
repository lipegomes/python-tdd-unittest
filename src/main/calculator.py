def sum(x, y):
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return f"Result of the sum between {x} and {y} is: {x + y}"


def subtraction(x, y):
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return f"Result of the subtraction between {x} and {y} is: {x - y}"


def multiplication(x, y):
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return f"Result of the multiplication between {x} and {y} is: {x * y}"


def division(x, y):
    assert isinstance(x, (int, float)), "The numerator value must be an int or float"
    assert isinstance(y, (int, float)), "The denominator value must be greater than zero"
    return f"Result of the division between {x} and {y} is: {x / y}"


def exponentiation(x, y):
    assert isinstance(x, (int, float)), "The x value must be an int or float"
    assert isinstance(y, (int, float)), "The y value must be an int or float"
    return f"Result of the exponentiation between {x} and {y} is: {x ** y}"
