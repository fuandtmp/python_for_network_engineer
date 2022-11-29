# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.2a

from sys import argv

file = argv[1]
ext_file = argv[2]

ignore = ["duplex", "alias", "configuration"]
# f = open('test.txt', 'w')

with open('config_sw1.txt') as config:
    for line in config:
        words = line.split()
        cross_words = set(words) & set(ignore)
        if not line.startswith("!") and not cross_words:
            newlines = line.rstrip() + '\n'
            ext_file.writelines(newlines)

ext_file.close()
