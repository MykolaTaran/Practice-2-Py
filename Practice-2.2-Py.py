from power_function_2_2  import calculate_power


x = float(input("Введіть значення x: "))
n = int(input("Введіть значення n: "))
result = calculate_power(x, n)
print(f"Результат {x} піднесеного до степеня {n}: {result}")