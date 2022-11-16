# https://pyneng.readthedocs.io/ru/latest/exercises/05_exercises.html
# 5.3
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]
template = {"access": access_template, "trunk": trunk_template}
question = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}

mode_interface = input("Введите режим порта ('access' или 'trunk'): ")
n_interface = input("Введите номер порта ('Fa0/1 или Gi1/2'): ")
vlans = input(question[mode_interface])

print(f"interface {n_interface}")
print("\n".join(template[mode_interface]).format(vlans))
