
def cyclic_gen(start, end):
    while True:
        for num in range(start, end + 1):
            yield num

def main():
    try:
        total_count = int(input("Введите количество чисел для вывода:"))

        if total_count <= 0:
            print("Введите целое положительное число")
            return
    
        start_num = int(input("Введите начало диапазона:"))
        end_num = int(input("Введите конец диапазона:"))

        print(f"Последовательностью из {total_count} элементов:")

        my_generator = cyclic_gen(start_num, end_num)

        for _ in range(total_count):
            print(next(my_generator), end=" ")
            print()
    except ValueError:
        print("Ошибка: нужно ввести целое число.")

if __name__ == "__main__":
    main()

    