import math

f_n = int(input("Введите первое число:"))
s_n = int(input("Введите второе число:"))

nod = math.gcd(f_n, s_n)

print (f"НОД чисел: {f_n} и {s_n}\n"
       f"Равен: {nod}")




#так же читал про алгоритм Евклида, например:

#f_n = int(input("Введите первое число:"))
#s_n = int(input("Введите второе число:"))

#while s_n:
#    f_n, s_n = s_n, f_n % s_n
#print(f_n)

#Вроде как-то так