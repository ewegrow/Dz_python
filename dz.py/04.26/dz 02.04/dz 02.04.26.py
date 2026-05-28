program_1 = input("Выберите вариант вывода, сразу или с задержкой ?")
if program_1 == 'сразу':
    print ('hello world')
    print ('It is my first python program')
    print ('And it is the end of my program')
    print ('Bye-bye')
elif program_1 == 'с задержкой':
    import time
    print ('hello world')
    time.sleep (1.2)
    print ('It is my first python program')
    time.sleep (1.2)
    print ('And it is the end of my program')
    time.sleep (1.2)
    print ('Bye-bye')
