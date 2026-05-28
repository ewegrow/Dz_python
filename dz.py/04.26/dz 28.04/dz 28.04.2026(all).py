#1

# numbers = [1, 2, 3]
# result = list(map(str, numbers))

# print(result)



#2

# numbers = [-3, -2, -1, 0, 1, 2, 3]
# result = list(filter(lambda x: x > 0, numbers))
# print(result)

#3

# strings  = ['level', 'noon', 'python', 'hello', 'nun','world', 'eye']
# palindromes = list(filter(lambda s: s == s[::-1], strings))
# print(palindromes)

#4

# import time
# from functools import wraps

# def time_t(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()

#         print(f"Функция '{func.__name__}' выполнена за {end_time - start_time:.10f} секунд")
#         return result
#     return wrapper

# @time_t
# def privet(n):
#     time.sleep(n)
#     return "Готово"

# privet(5)


#5

# from functools import reduce

# rooms = [
#     {"name": "Kitchen", "length": 6, "width": 4},
#     {"name": "Room 1", "length": 5.5, "width": 4.5},
#     {"name": "Room 2", "length": 5, "width": 4},
#     {"name": "Room 3", "length": 7, "width": 6.3},]

# areas = map(lambda room: room["length"] * room["width"], rooms)

# total_area = reduce(lambda x, y: x+y, areas)

# print(f"Общая площадь квартиры: {total_area} м²")

