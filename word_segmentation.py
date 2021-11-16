from underthesea import word_tokenize

list_word = []

with open('word.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        list_word.append(word_tokenize(line, format='text'))

with open('word_segmentation.txt', 'w', encoding='utf-8') as f:
    for word in list_word:
        for w in word:
            f.write(w + '\n')