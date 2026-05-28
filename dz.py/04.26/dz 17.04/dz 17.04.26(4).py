

def fibonacci(n):
    f_1 = float(input("Введите первое число: "))
    f_2 = float(input("Введите второе число: "))
    
    f_list = [f_1, f_2]
    while len(f_list) < n:

        next_val = f_list[-1] + f_list[-2]
        f_list.append(next_val)
    return f_list


fib = int(input("Введите количество чисел в последоватильности:"))
print(fibonacci(fib))
