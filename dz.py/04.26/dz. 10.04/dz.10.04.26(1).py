from math import sin, cos
import time


print(
    "В первой задаче приведены четыре формулы,\n"
    "в которой необходимо найти переменную Y\n"
    "предварительно задав перменные: а, b, x."
)
a = float(input("Введите переменну а:"))
b = float(input("Введите переменную b:"))
x = float(input("Введите переменную x:"))

time.sleep(1)
formula_one = (
    ((a**2) / 3)
    + ((a**2 + 4) / b)
    + (((a**2 + 4) ** 0.5) / 4)
    + ((((a**2 + 4) ** 3) ** 0.5)/4)
)
print(f"В первой формуле\nПеременная Y будет равна числу:{round(formula_one, 2)}")
time.sleep(1)
formula_two = cos(x) + sin(x)
print(f"Во второй формуле\nПеременная Y будет равна числу:{round(formula_two, 2)}")
time.sleep(1)
formula_three = ((cos(x**2)**2) + (sin((2 * x) - 1)**2)) ** (1 / 3)
print(f"Во третьей формуле\nПеременная Y будет равна числу:{round(formula_three, 2)}")
time.sleep(1)
formula_four = (5*x) + (3*(x**2))*(((1+(sin(x))**2))**0.5)
print(f"Во четвертой формуле\nПеременная Y будет равна числу:{round(formula_four, 2)}")