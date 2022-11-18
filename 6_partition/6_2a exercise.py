# https://pyneng.readthedocs.io/ru/latest/exercises/06_exercises.html
# 6.2a

while True:
    entered_address = input("Please, enter the address at format '192.168.0.1': ")
    i = 0
    for dot in entered_address:
        if dot == '.':
            i += 1
    if i != 3:
        entered_address = input("Please, enter the address at format '192.168.0.1': ")

    splitted_ip_address = entered_address.split('.')

    try:
        a = int(splitted_ip_address[0]) * int(splitted_ip_address[1]) * int(splitted_ip_address[2]) * \
            int(splitted_ip_address[3])
    except ValueError:
        print('IP address must be contains only numbers')
    else:
        break

# entered_address = input("Please, enter the address at format '192.168.0.1': ")
splitted_ip_address = entered_address.split('.')
a1, a2, a3, a4 = [
    int(splitted_ip_address[0]),
    int(splitted_ip_address[1]),
    int(splitted_ip_address[2]),
    int(splitted_ip_address[3])
]
if 224 > a1 > 0:
    print('It is an unicast address')
elif 223 < a1 < 240:
    print('It is a multicast address')
elif entered_address == '255.255.255.255':
    print('It is a local broadcast')
elif entered_address == '0.0.0.0':
    print('It is an unassigned address')
else:
    print('Unused address')
