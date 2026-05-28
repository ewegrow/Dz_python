try:
    n_one = float(input("Введите первое число:"))
    operation = input("Выберите операцию (+, -, *, /):")
    n_two = float(input("Введите второе число:"))


    if operation == '+':
        result = n_one + n_two
    elif operation == '-':
        result = n_one - n_two
    elif operation == '*':
        result = n_one * n_two
    elif operation == '/':
        result = n_one / n_two
    else:
        raise NameError("Неверная операция")
    

    print(f"Результат: {result}")

except ValueError:
    print("Ошибка: введите число, а не текст")
except ZeroDivisionError:
    print("На ноль делить нельзя.")
except NameError as e:
    print(e)
finally:
    print("Работа калькулятора завершена.")
    

