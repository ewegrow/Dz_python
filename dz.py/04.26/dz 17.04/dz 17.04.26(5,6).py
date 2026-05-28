user = input("Введите числа через пробел: ")
numbers = [int(x) for x in user.split()]


if len(numbers) == len(set(numbers)):
    print("Все числа уникальны.")
else:
    print("В списке есть дубликаты.")


search_dupl = {}
for n in numbers:
    search_dupl[n] = search_dupl.get(n, 0) + 1


has_duplicates = any(v > 1 for v in search_dupl.values())
if has_duplicates:
    print("\nПовторяющиеся элементы:")
    for num, count in search_dupl.items():
        if count > 1:
            print(f"Число {num} встречается {count} раз(а)")

print(f"\nСумма: {sum(numbers)}")
print(f"Минимум: {min(numbers)}")
print(f"Максимум: {max(numbers)}")
