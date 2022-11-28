# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.2

from sys import argv

file = argv[1]

with open(file) as config:
    for line in config:
        if not '!' in line:
            print(line, end=' ')
