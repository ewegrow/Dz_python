file_name = input("Введите имя файла: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    total_sum = 0      
    current_number = ""  

    
    for char in text:
        
        if char.isdigit():
            
            current_number += char
        else:
            if current_number:
                total_sum += int(current_number) 
                current_number = ""  

    
    if current_number:
        total_sum += int(current_number)

    print(f"Сумма всех чисел в файле: {total_sum}")

except FileNotFoundError:
    print("Ошибка: Файл не найден.")
