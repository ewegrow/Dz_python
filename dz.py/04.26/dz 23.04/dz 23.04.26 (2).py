def dec_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    return dec_binary(n // 2) + str(n % 2)


number = int(input("Введите десятичное число:"))

if number == 0:
    result = "0"
else:
    result = dec_binary(number)

print(f"Двоичный вид:{result}")

