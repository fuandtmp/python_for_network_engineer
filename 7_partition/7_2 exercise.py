# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.2a

from sys import argv

file = argv[1]

ignore = ["duplex", "alias", "configuration"]

with open(file) as config:
    for line in config:
        words = line.split()
        cross_words = set(words) & set(ignore)
        if not line.startswith("!") and not cross_words:
            print(line.rstrip())
