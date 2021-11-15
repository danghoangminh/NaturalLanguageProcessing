from underthesea import word_tokenize

list_word = []

with open("word.txt", "r", encoding="utf-8") as f:
    text = f.readlines()
    for line in text:
        list_word += [word_tokenize(line)]

with open("word_segmentation.txt", "w", encoding="utf-8") as f:
    for line in list_word:
        f.write(str(line) + "\n")