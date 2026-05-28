user_numbers = input("Введите список чисел через пробел (например, 5 6 7 1 2): ")
numbers = [int(x) for x in user_numbers.split()]
target = int(input("Введите искомое число: "))

low = 0
high = len(numbers) - 1
position = -1

while low <= high:
    mid = (low + high) // 2
    
    if numbers[mid] == target:
        position = mid
        break
    
    
    if numbers[low] <= numbers[mid]:  
        if numbers[low] <= target < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:  
        if numbers[mid] < target <= numbers[high]:
            low = mid + 1
        else:
            high = mid - 1

if position != -1:
    print(f"Элемент найден на позиции с индексом: {position}")
else:
    print("Искомый элемент в списке не найден.")
