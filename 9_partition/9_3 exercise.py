# https://pyneng.readthedocs.io/ru/latest/exercises/09_exercises.html


def get_int_vlan_map(config_file):
    access_config = {}
    trunk_config = {}

    with open(config_file) as config:
        for line in config:
            line = line.rstrip()
            if line.startswith("interface"):
                int_f = line.split()[1]
            elif "access vlan" in line:
                access_config[int_f] = int(line.split()[-1])
            elif "trunk allowed" in line:
                trunk_config[int_f] = [int(v) for v in line.split()[-1].split(",")]
        return access_config, trunk_config


dict_of_intf = get_int_vlan_map('config_sw1.txt')
print(dict_of_intf)
