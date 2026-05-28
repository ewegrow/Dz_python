import csv
import json
import os

JSON_FILE = "employees.json"
CSV_FILE = "employees.csv"


def load_json_data():
    if not os.path.exists(JSON_FILE):
        print(f"[-] Файл {JSON_FILE} не найден. Создан пустой список.")
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[-] Ошибка чтения JSON. Файл поврежден или пуст.")
        return []


def json_to_csv():
    data = load_json_data()
    if not data:
        print("[-] Нет данных для конвертации.")
        return

    fieldnames = list(data[0].keys())

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for employee in data:
            row = employee.copy()
            if isinstance(row.get("languages"), list):
                row["languages"] = ", ".join(row["languages"])
            writer.writerow(row)

    print(f"[+] Данные успешно сохранены в файл: {CSV_FILE}")



def add_employee_to_json():
    data = load_json_data()

    print("\n--- Добавление сотрудника в JSON ---")
    name = input("Введите имя и фамилию: ").strip()
    birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ").strip()

    try:
        height = int(input("Введите рост (см): "))
        weight = float(input("Введите вес (кг): "))
    except ValueError:
        print("[-] Ошибка: рост и вес должны быть числами!")
        return

    car_input = input("Есть ли машина? (да/нет): ").strip().lower()
    car = True if car_input in ["да", "yes", "y", "1"] else False

    langs_input = input("Введите языки программирования через запятую: ")
    languages = [lang.strip() for lang in langs_input.split(",") if lang.strip()]

    new_emp = {
        "name": name,
        "birthday": birthday,
        "height": height,
        "weight": weight,
        "car": car,
        "languages": languages,
    }

    data.append(new_emp)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("[+] Сотрудник успешно добавлен в JSON-файл.")



def add_employee_to_csv():
    print("\n--- Добавление сотрудника в CSV ---")
    name = input("Введите имя и фамилию: ").strip()
    birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ").strip()

    try:
        height = int(input("Введите рост (см): "))
        weight = float(input("Введите вес (кг): "))
    except ValueError:
        print("[-] Ошибка: рост и вес должны быть числами!")
        return

    car_input = input("Есть ли машина? (да/нет): ").strip().lower()
    car = "True" if car_input in ["да", "yes", "y", "1"] else "False"

    langs_input = input("Введите языки программирования через запятую: ")
    languages = ", ".join(
        [lang.strip() for lang in langs_input.split(",") if lang.strip()]
    )

    fieldnames = ["name", "birthday", "height", "weight", "car", "languages"]
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {
                "name": name,
                "birthday": birthday,
                "height": height,
                "weight": weight,
                "car": car,
                "languages": languages,
            }
        )

    print("[+] Сотрудник успешно добавлен в CSV-файл.")


def find_employee_by_name():
    data = load_json_data()
    search_name = input("Введите имя для поиска: ").strip().lower()

    found = False
    for emp in data:
        if search_name in emp.get("name", "").lower():
            print("\n[ Информация о сотруднике ]")
            for key, value in emp.items():
                print(f"{key}: {value}")
            found = True

    if not found:
        print("[-] Сотрудник с таким именем не найден.")


def filter_by_language():
    data = load_json_data()
    search_lang = input("Введите язык программирования: ").strip().lower()

    print(f"\nСотрудники со знанием {search_lang.upper()}:")
    count = 0
    for emp in data:
        langs = [str(lang).lower() for lang in emp.get("languages", [])]
        if search_lang in langs:
            print(f"- {emp.get('name')} {emp.get('languages')}")
            count += 1

    if count == 0:
        print("[-] Ни один сотрудник не владеет этим языком.")


def average_height_by_year():
    data = load_json_data()
    try:
        target_year = int(input("Введите год рождения для фильтра: "))
    except ValueError:
        print("[-] Ошибка: год должен быть числом.")
        return

    heights = []
    for emp in data:
        birthday = emp.get("birthday", "")
        try:
            emp_year = int(birthday.split(".")[-1])
            if emp_year < target_year:
                heights.append(emp.get("height", 0))
        except (ValueError, IndexError):
            continue

    if heights:
        avg_height = sum(heights) / len(heights)
        print(
            f"\n[+] Средний рост сотрудников, родившихся до {target_year} года: {avg_height:.2f} см"
        )
    else:
        print(f"[-] Нет сотрудников, родившихся до {target_year} года.")


def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("               ГЛАВНОЕ МЕНЮ")
        print("=" * 50)
        print("1. Считать JSON и сохранить в CSV")
        print("3. Добавить нового сотрудника в JSON-файл")
        print("4. Добавить нового сотрудника в CSV-файл")
        print("5. Вывести информацию о сотруднике по имени")
        print("6. Фильтр сотрудников по языку программирования")
        print("7. Посчитать средний рост (фильтр по году рождения)")
        print("0. Выход")
        print("=" * 50)

        choice = input("Выберите действие (0-7): ").strip()

        if choice == "1":
            json_to_csv()
        elif choice == "3":
            add_employee_to_json()
        elif choice == "4":
            add_employee_to_csv()
        elif choice == "5":
            find_employee_by_name()
        elif choice == "6":
            filter_by_language()
        elif choice == "7":
            average_height_by_year()
        elif choice == "0":
            print("[+] Программа завершена. Всего доброго!")
            break
        else:
            print("[-] Некорректный ввод. Пожалуйста, выберите пункт от 0 до 7.")


if __name__ == "__main__":
    main_menu()

