import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

print("Создание таблицы")
cursor.execute('''
CREATE TABLE Employees (
    Name TEXT,
    Position TEXT,
    Department TEXT,
    Salary REAL
)
''')

print("Вставка записей")
employees_data = [
    ('Иван Иванов', 'Developer', 'IT', 4500.00),
    ('Пётр Петров', 'Manager', 'Sales', 5500.00),
    ('Анна Сидорова', 'Manager', 'HR', 5200.00),
    ('Мария Николаева', 'Specialist', 'Sales', 3500.00)
]
cursor.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?)', employees_data)
connection.commit()

print("Обновление данных")
cursor.execute('''
UPDATE Employees
SET Position = 'Senior Developer', Salary = 6000.00
WHERE Name = 'Иван Иванов'
''')
connection.commit()

print("Добавление поля HireDate")
cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')
connection.commit()

print("Добавление дат приема на работу")
dates = [
    ('2023-01-15', 'Иван Иванов'),
    ('2022-05-10', 'Пётр Петров'),
    ('2024-03-01', 'Анна Сидорова'),
    ('2023-11-20', 'Мария Николаева')
]
cursor.executemany('UPDATE Employees SET HireDate = ? WHERE Name = ?', dates)
connection.commit()


print("\nСТАНДАРТНЫЕ ЗАПРОСЫ ВЫБОРКИ")


cursor.execute("SELECT * FROM Employees WHERE Position = 'Manager'")
print("Менеджеры:", cursor.fetchall())


cursor.execute("SELECT * FROM Employees WHERE Salary > 5000")
print("Зарплата > 5000:", cursor.fetchall())


cursor.execute("SELECT * FROM Employees WHERE Department = 'Sales'")
print("Отдел Sales:", cursor.fetchall())


cursor.execute("SELECT AVG(Salary) FROM Employees")
print(f"Средняя зарплата: {cursor.fetchone()[0]:.2f} $")

print("Реализация логики функций через встроенные возможности Python + SQLite")


def check_employee_status(position, salary, department, action_type):
    if action_type == 'managers' and position == 'Manager':
        return 1
    if action_type == 'high_salary' and salary > 5000:
        return 1
    if action_type == 'sales' and department == 'Sales':
        return 1
    return 0


connection.create_function("match_policy", 4, check_employee_status)

print("Менеджеры:")
cursor.execute("SELECT Name, Position FROM Employees WHERE match_policy(Position, Salary, Department, 'managers') = 1")
print(cursor.fetchall())

print("Зарплата > 5000:")
cursor.execute("SELECT Name, Salary FROM Employees WHERE match_policy(Position, Salary, Department, 'high_salary') = 1")
print(cursor.fetchall())


print("Удаление таблицы")
cursor.execute('DROP TABLE Employees')
connection.commit()
print("Таблица 'Employees' успешно удалена.")

connection.close()
