print("Дана строка с четыремя примера текста:\nHello World, a b c, test, test1 test test3 test4 test5.\n"
    "Наша задача узнать количество слов в каждом примере: ")
text_1 = "Hello World"
text_2 = "a b c"
text_3 = "test"
text_4 = "test1 test test3 test4 test5"
result_1 = (len(text_1.split()))
result_2 = (len(text_2.split()))
result_3 = (len(text_3.split()))
result_4 = (len(text_4.split()))
print ('Итоговым количеством слов в каждом примере будет:', result_1, result_2, result_3, result_4)
while True:
 question = input("Хотите ввести свой текст, чтобы узнать количество слов ? да / нет :")
 if question == 'да':
    question_1 = input("Введите вашу строку:")
    res_que = (len(question_1.split()))
    print('Количесто слов в вашей строке:', res_que)
 elif question == 'нет':
    print('Всего доброго.')
    break
 else:
    print('Ошибка ввода, попробуйте заново.')