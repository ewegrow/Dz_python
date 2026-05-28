import string 
from collections import Counter

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:

        for line in infile:
            cleaned_line = line.translate(str.maketrans("","", string.punctuation)).lower()
            
            words = cleaned_line.split()

            if not words:
                outfile.write("Пустая строка.")
                continue

            word_count = Counter(words)
            most_popular_word, count = word_count.most_common(1)[0]

            outfile.write(f"{most_popular_word} {count}\n")
    

process_file("input.txt", "output.txt")

# необходимо создать в дерриктории файл input.txt, чтобы получить потом файл output.txt с выводом результата