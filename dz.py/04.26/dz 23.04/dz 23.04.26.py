def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    
    else:
        return binary_search(arr, target, mid + 1, high)
    

user = input("Введите числа через пробел:")
numbers = [int(x) for x in user.split()]
numbers.sort()

number_search = int(input("Введите число для поиска:"))

result = binary_search(numbers, number_search, 0, len(numbers) -1 )

if result != -1:
    print(f"Элемент найден на позиции:{result}")
else:
    print("Элемент в списке не найден")