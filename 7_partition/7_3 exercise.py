# https://pyneng.readthedocs.io/ru/latest/exercises/07_exercises.html
# 7.3

template = "{0:9} {1:20} {2}"

with open('mac_table.txt') as config:
    for line in config:
        words = line.split()
        try:
            mac_address = str(words[1])
            first_octet_mac = int(mac_address[:4], 16)
            if type(first_octet_mac) == int:
                print(template.format(words[0], words[1], words[3]))
        except:
            pass
