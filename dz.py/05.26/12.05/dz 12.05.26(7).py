file_name = input("Введите имя файла для шифрования: ")


RUS_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RUS_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

ENG_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENG_LOWER = "abcdefghijklmnopqrstuvwxyz"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    encrypted_lines = []
    
    for index, line in enumerate(lines):
        shift = index + 1
        encrypted_line = ""
        
        for char in line:
            if char in RUS_UPPER:
                pos = RUS_UPPER.index(char)
                new_pos = (pos + shift) % 33
                encrypted_line += RUS_UPPER[new_pos]
                
            elif char in RUS_LOWER:
                pos = RUS_LOWER.index(char)
                new_pos = (pos + shift) % 33
                encrypted_line += RUS_LOWER[new_pos]
                
            elif char in ENG_UPPER:
                pos = ENG_UPPER.index(char)
                new_pos = (pos + shift) % 26
                encrypted_line += ENG_UPPER[new_pos]
                
            elif char in ENG_LOWER:
                pos = ENG_LOWER.index(char)
                new_pos = (pos + shift) % 26
                encrypted_line += ENG_LOWER[new_pos]
                
            else:
                encrypted_line += char
                
        encrypted_lines.append(encrypted_line)

    print("\nЗашифрованный текст:")
    print("".join(encrypted_lines))

except FileNotFoundError:
    print("Ошибка: Файл не найден.")
