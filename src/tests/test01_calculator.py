from src.base.calculator import sum, subtraction, multiplication, division, exponentiation

calc1 = sum(10, 30)
print(calc1)

calc2 = subtraction(25, 15)
print(calc2)

calc3 = multiplication(7, 8.5)
print(calc3)

calc4 = division(2048, 64)
print(calc4)

calc5 = exponentiation(7, 7)
print(calc5)

try:
    calc6 = division(-8, 2)
    print(calc6)
except AssertionError as e:
    print(f"Invalid calculation: {e}")

try:
    calc7 = sum(1, "2")
    print(calc7)
except AssertionError as e:
    print(f"Invalid calculation: {e}")

try:
    calc8 = sum("20", 2)
    print(calc8)
except AssertionError as e:
    print(f"Invalid calculation: {e}")

calc9 = multiplication(77, 0.322)
print(calc9)
