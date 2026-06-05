def  fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    try:
        count = int(input("Введите количество чисел Фибоначи:"))

        if count <= 0:
            print("Введите целое положительное число:")
            return
        
        print(f"Первые {count} чисел Фибоначчи:")
        fib_gen = fibonacci(count)
        print(*fib_gen)

    except ValueError:
        print("Ошибка:нужно ввести целое число.")

if __name__ == "__main__":
    main()
    