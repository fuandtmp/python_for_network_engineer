# https://pyneng.readthedocs.io/ru/latest/exercises/04_exercises.html
# 4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat.replace('Fast', 'Gigabit'))

# 4.2
mac = "AAAA:BBBB:CCCC"
print(mac.replace(':', '.'))

# 4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()[-1].split(',')
print(result)

# 4.4
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans.sort()
result = set(vlans)
print(result)

# 4.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = set(command1.split()[-1].split(','))
command2 = set(command2.split()[-1].split(','))
result = list(command1.intersection(command2))
print(result)

# 4.6
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_list = ospf_route.strip().replace(',', '').split()
print(f'''
Prefix             {ospf_list[0]}
AD/Metric          {ospf_list[1]}
Next-Hop           {ospf_list[3]}
Last update        {ospf_list[4]}
Outbound Interface {ospf_list[5]}
''')
# 4.7 - not done
mac = "AAAA:BBBB:CCCC"
bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))
print(bin_mac)

# 4.8
ip = "192.168.3.1"
list_ip = ip.split('.')
template = '''
IP Address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(template.format(int(list_ip[0]), int(list_ip[1]), int(list_ip[2]), int(list_ip[3])))
