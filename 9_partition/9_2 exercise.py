# https://pyneng.readthedocs.io/ru/latest/exercises/09_exercises.html

trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}


def to_make_conf_trunk_ports(interfaces, template):
    for key, value in interfaces.items():
        print("interface " + key)
        for command in template:
            if command.endswith("allowed vlan"):
                print(f'{command} {str(value).strip("[]")}')
            else:
                print(f'{command}')


to_make_conf_trunk_ports(trunk_config, trunk_mode_template)

