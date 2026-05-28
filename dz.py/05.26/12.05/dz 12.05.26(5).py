file_name  = ("Введите имя файла со списком учащихся:")

try:
    with open(file_name, "r", encoding="8-utf") as file:
        print("\nУчащиеся с оценкой меньше 3 баллов:")
        has_low_grades = False

        for line in file:
            line = line.strip()

            if not line:
                continue

            data = line.split()
            grade = int(data[-1])

            if grade <3:
                last_name = data[0]
                first_name = data[1]

                print(f"-{last_name} {first_name} (Оценка:{grade})")
                has_low_grades = True

        if not has_low_grades:
            print(f"Таких учащихся нет.")

except FileNotFoundError:
    print(f"Ошибка: Файл '{file_name}' не найден.")
except ValueError:
    print("Ошибка: В файле обнаружены некорректные данные")
