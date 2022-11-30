# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.3b


entered_vlan = input('введите номер влана: ')

with open('mac_table.txt', 'r') as config:
    for line in config:
        words = line.split()
        if words and words[0].isdigit() and words[0] == entered_vlan:
            vlan, mac, _, intf = words
            print(f"{vlan:9}{mac:20}{intf}")

# for vlan, mac, interface in sorted(mac_table):
#     print(f'{vlan:<9}{mac:20}{interface}')
