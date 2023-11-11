import math

# Частина 1: Обчисліть Z = tan(3*alpha)
alpha = float(input("Введіть значення alpha у градусах: "))
z = math.tan(math.radians(3 * alpha))
print(f"Результат tan(3*alpha): {z}")

# Частина 2: Обчисліть Z = x^n
x = float(input("Введіть значення x: "))
n = int(input("Введіть значення n: "))
result = 1
for i in range(n):
    result *= x
print(f"Результат {x} піднесеного до степеня {n}: {result}")