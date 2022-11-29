# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.2b

from sys import argv

file, ext_file = argv[1], argv[2]

ignore = ["duplex", "alias", "configuration"]
# f = open('test.txt', 'w') <<-- For tests

with open(file) as config, open(ext_file, 'w') as dst:
    for line in config:
        words = line.split()
        cross_words = set(words) & set(ignore)
        if not line.startswith("!") and not cross_words:
            dst.write(line)
