
# 1

# class soda:
#     def __init__(self, flavour = None):
#         self.flavour = flavour


#     def __str__(self):
#         if self.flavour:
#             return f"У вас газировка с {self.flavour} вкусом"
#         return "У вас обычная газировка"
    


# 2


# class Math:
#     def addition(self, a, b):
#         print(f"Результат сложения: {a + b}")

#     def substraction(self, a, b):
#         print(f"Результат вычитания: {a - b}")

#     def multiplication(self, a, b):
#         print(f"Результат умножения: {a * b}")

#     def division(self, a, b):
#         if a or b == 0:
#             print("Ошибка: деление на ноль невозможно.")
#         else:
#             print(f"Результат деления: {a / b}")

    

# 3

# class Car:
#     def __init__(self, color, car_type, year):
#       self.color = color
#       self.ctype = car_type
#       self.year = year

#     def start_engine(self):
#        print("Автомобиль заведен")

#     def stop_engine(self):
#        print("Автомобиль заглушен")

#     def set_year(self, year):
#         self.year = year

#     def set_type(self, car_type):
#         self.type = car_type

#     def set_color(self, color):
#         self.color = color



# 4
# import math

# class Sphere:
#     def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
#         self.radius = float(radius)
#         self.x = float(x)
#         self.y = float(y)
#         self.z = float(z)

#     def get_volume(self):
#         return (4 / 3) * math.pi * (self.radius ** 3)

#     def get_square(self):
#         return 4 * math.pi * (self.radius ** 2)

#     def get_radius(self):
#         return self.radius

#     def get_center(self):
#         return (self.x, self.y, self.z)

#     def set_radius(self, radius):
#         self.radius = float(radius)

#     def set_center(self, x, y, z):
#         self.x = float(x)
#         self.y = float(y)
#         self.z = float(z)

#     def is_point_inside(self, x, y, z):
#         distance_squared = (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2

#         return distance_squared <= self.radius**2



# 5
# class SuperStr(str):
#     def is_repeatance(self, s):
#         if not isinstance(s, str) or not s or not self:
#             return False
        

#         if len(self) % len(s) != 0:
#             return False
            

#         count = len(self) // len(s)
#         return s * count == self

#     def is_palindrom(self):

#         cleaned_str = self.lower()
#         return cleaned_str == cleaned_str[::-1]

