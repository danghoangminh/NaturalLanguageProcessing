list_word = {}

with open("word_seg.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        words = line.split()
        for word in words:
            if "_" not in word:
                continue
            if word not in list_word:
                list_word[word] = 1
            else:
                list_word[word] += 1
                
with open("statistic.txt", 'w', encoding='utf-8') as f:
    for key, value in list_word.items():
        f.write(key + " " + str(value) + "\n")