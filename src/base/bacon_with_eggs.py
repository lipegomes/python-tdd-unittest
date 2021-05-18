def bacon_with_eggs(n):
    assert isinstance(n, int), "n must be int"

    if n % 3 == 0 and n % 5 == 0:
        return "Bacon with Eggs"
