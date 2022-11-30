# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.3


with open('mac_table.txt') as config:
    for line in config:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            print(f'{vlan:9}{mac:20}{interface}')
