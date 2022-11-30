# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.3b

mac_table = []

with open('mac_table.txt') as config:
    for line in config:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            mac_table.append([int(vlan), mac, interface])

for vlan, mac, interface in sorted(mac_table):
    print(f'{vlan:<9}{mac:20}{interface}')
