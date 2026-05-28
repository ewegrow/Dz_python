try:
    weight = float(input("Введите ваш вес в кг:"))
    height = float(input("Введите ваш рост в м или см:"))

    if weight <=0 or height <=0:
     raise ValueError("Вес и рост не могут быть отрицательными\n" \
    "Или равняться нулю.")

    if height > 3:
        height = height / 100

    imt = weight / (height ** 2)
    print(f"Ваш рост равен: {height} м")
    print(f"Индекс массы вашего тела равен:{imt:.2f}")

    if imt <= 18.5:
        print("Недостатная масса тела")
    elif 18.5 <= imt <= 25:
        print("В пределах нормы")
    elif 25 <= imt <= 30:
        print("Избыточная масса тела")
    else:
        print("Ожирение")

except ValueError as e:
    print(f"Ошибка ввода {e}")

except ZeroDivisionError:
    print("Рост не может быть равен нулю")

except Exception:
    print("Произошла непредвиденная ошибка.")