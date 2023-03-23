from razdel import tokenize
import codecs
import re

# -*- coding: windows-1251 -*-

# tokenization

for i in range(1, 101):
    with codecs.open('fileOutput%i.txt' %i, "r", "utf_8_sig") as f:
        text_original = f.read()

    tokens = set(tokenize(text_original))
    tokens_new = [_.text for _ in tokens]

    with codecs.open('tokens/list_words%i.txt' % i, "w") as f1:
        for j in tokens_new:
            result = re.sub("[^а-яА-я]", "", str(j))
            if result != "":
                f1.write(result + '\n')


