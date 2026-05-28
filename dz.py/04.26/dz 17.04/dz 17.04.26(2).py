import math

def cos(x_rad, n_terms):
    cos_1 = 0
    for n in range(n_terms):
        num = math.pow(-1, n) * math.pow(x_rad, 2*n)
        den = math.factorial(2 * n)
        cos_1 += num / den
    return cos_1

enter_x = float(input("Введите значение угла в градусах: "))
terms = int(input("Введите количество членов ряда для точности: "))

enter_rad = math.radians(enter_x)

result = cos(enter_rad, terms)

print(f"Результат по формуле:{result}\n"
      f"Результат math.cos({enter_x}°): {math.cos(enter_rad)}")