import codecs
from functools import reduce
import re
from collections import defaultdict

query = input("Write your query: ")
fullQuery = query.split()
tokens = []
dict = {}
dictUpdate = {}
for i in range(1, 101):
    with codecs.open('../2_task/tokens/list_words%i.txt' % i, "r") as f:
        tokens = f.readlines()
        word = tokens[i].strip().lower()
    for i in range(1, 101):
        with codecs.open('../fileOutput%i.txt' % i, "r", "utf_8_sig") as f1:
            while True:
                line = f1.readline()
                if not line:
                    break
                if word in line.strip():
                    dict.setdefault(word, set(list([])))
                    dict[word].add('../fileOutput%i.txt' % i)
            f1.close()
    f.close()

with codecs.open('inverted_array.txt', "w") as f2:
    for key, value in dict.items():
        f2.write("{" + '"count":' + str(len(value)) + "," + '"inverted_array":' + str(list(value)) + "," + '"word": ' + str(key) + "}" + '\n')


for key, value in dict.items():
    for term in fullQuery:
        if term == key:
            for i in value:
                dictUpdate[key] = value


def andDef(dictUpdate):
    print(reduce(set.intersection, map(set, dictUpdate.values())))


def orDef(dictUpdate):
    print(reduce(set.union, map(set, dictUpdate.values())))

if 'или' in fullQuery:
    orDef(dictUpdate)
else:
    andDef(dictUpdate)
