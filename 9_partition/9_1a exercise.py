# https://pyneng.readthedocs.io/ru/latest/exercises/09_exercises.html

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]


def to_make_conf_access_ports(interfaces, template, psecurity=None):
    for key, value in interfaces.items():
        print("interface " + key)
        for command in template:
            if command.endswith("vlan"):
                print(f'{command} {value}')
            else:
                print(f'{command}')
        if psecurity:
            for ps_commands in psecurity:
                print(f'{ps_commands}')


to_make_conf_access_ports(access_config, access_mode_template)
print('=' * 60 + ' STARTS SECOND ACCESS TEMPLATE ' + '=' * 60)
to_make_conf_access_ports(access_config_2, access_mode_template)
print('=' * 60 + ' STARTS PORT SECURITY ACCESS TEMPLATE ' + '=' * 60)
to_make_conf_access_ports(access_config, access_mode_template, port_security_template)
