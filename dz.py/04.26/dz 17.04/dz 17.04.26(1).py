import math

def sin(x_rad, n_terms):
    sin_1 = 0
    for n in range(n_terms):
        num = ((-1)**n) * math.pow(x_rad, 2*n + 1)
        den = math.factorial(2*n + 1)
        sin_1 += num / den
    return sin_1


enter_x = float(input("Введите значение угла в градусах: "))
terms = int(input("Введите количество членов ряда для точности: "))


enter_rad = math.radians(enter_x)

result = sin(enter_rad, terms)

print(f"\nУгол в радианах: {round(enter_rad, 4)}")
print(f"Результат по формуле: {result}")
print(f"Для проверки: {math.sin(enter_rad)}")
