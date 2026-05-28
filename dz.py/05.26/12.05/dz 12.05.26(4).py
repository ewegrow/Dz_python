
with open("stop_words.txt", 'r', encoding="utf-8") as file:
    stop_words_content = file.read()
    stop_words = stop_words_content.split()
    stop_words = [word.lower() for word in stop_words]


file_name = input("Введите текст для цензуры: ")

with open(file_name, 'r', encoding="utf-8") as file:
    text = file.read()


censored_text = ""
i = 0

while i < len(text):
    matched = False

    for word in stop_words:
        length = len(word)
        sub_string = text[i : i + length].lower()

        if sub_string == word:
            censored_text += "*"*length

            i+=length
            matched = True
            break

    if not matched:
        censored_text += text[i]
        i +=1

print("\nРезультат цензуры:")
print(censored_text)