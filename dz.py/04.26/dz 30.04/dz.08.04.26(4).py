print("Дана строка. Замените в этой строке все появления\n"
"Буквы h на букву H, кроме первого и последнего вхождения.")
question = input("Введите свою стройку содержащую символы h или H\nИли посмотрите пример из " \
"домашнего задания.\nСвоя строка / Дз:")
if question == 'Дз':
    text_1 = "hhhabchghhh"
    first_w = text_1.find('h')
    last_w = text_1.rfind('h')
    mid = text_1[first_w + 1:last_w].replace('h','H')
    result = text_1[:first_w+1] + mid + text_1[last_w:]
    print ('Итог:', result)
elif question == 'Своя строка':
    question_2 = input ("Введите строку:")
    first_w1 = question_2.find('h')
    last_w1 = question_2.rfind('h')
    mid_1 = question_2[first_w1 + 1:last_w1].replace('h','H')
    result_1 = question_2[first_w1 + 1] + mid_1 + question_2[last_w1]
    print ('Итог:', result_1)