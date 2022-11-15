# https://pyneng.readthedocs.io/ru/latest/exercises/05_exercises.html
# 5.1a
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

print('Введите имя устройства: ', end='')
equipment = input()
# 5.1b
get_dict = london_co[equipment]
list_of_getted_dict = list(get_dict.keys())
print(f'Введите имя параметра ({" ".join(list_of_getted_dict)}): ', end='')
key = input()
# 5.1c and 5.1d
print(london_co[equipment].get(key.lower(), "Такого параметра нет"))
