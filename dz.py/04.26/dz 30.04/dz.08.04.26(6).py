Number = int(input("Введите целое число:"))
print ('Последняя цифра',Number % 10)
print ('Количество десятков:', (Number // 10)%10)
Number_one = Number // 100
Number_two = (Number // 10)%10
Number_three = Number %10
Sum_numbers = Number_one + Number_two + Number_three
print('Сумма чисел:', Sum_numbers)