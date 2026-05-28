user_numbers = input("Введите список чисел через пробел:")
numbers = [int(x) for x in user_numbers.split()]


numbers.sort()


target = int(input("Введите искомое число :"))


low = 0
high = len(numbers) - 1
position = -1

while low <= high:
    mid = (low + high) // 2
    guess = numbers[mid]

    if guess == target:
        position = mid
        break

    if guess > target:
        high = mid - 1
    else:
        low = mid + 1

if position != -1:
    print(f"Элемент найден на позиции с индексом:{position}")
else:
    print("Искомый элемент в списке не найден.")
