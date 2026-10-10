import math

x = float(input("Введіть значення x: "))

if x >= 6:
    result = 3**(x-4) + math.log(x) + math.log10(x)
elif -1 < x < 6:
    result = x**2 + math.sin(2 * x)
else: # x <= -1:
    result = 2 + 2.7 * x**2
print(f"f(x) = {result}")