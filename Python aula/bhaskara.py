import math
A = int(input("insira A: "))
B = int(input("insira B: "))
C = int(input("insira C: "))
Delta = B ** 2 - 4 * A * C
if Delta > 0:
    x1 = (-B + math.sqrt(Delta)) / (2 * A)
    x2 = (-B - math.sqrt(Delta)) / (2 * A)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif Delta == 0:
    x = -B / (2 * A)
    print(f"A equação possui uma raiz real:")
    print(f"x = {x}")
else:
    print("delta não pertence aos numeros reais")