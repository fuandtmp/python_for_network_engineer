# https://pyneng.readthedocs.io/ru/latest/exercises/05_exercises.html
# 5.2
# получаем IP адрес от пользователя в формате "192.168.0.1/24"
prefix = input('Введите ip адрес: ')
# разделяем IP адрес и маску
ip_and_mask = prefix.split('/')
# Записываем отделенный IP от маски в переменную
ip_address = str(ip_and_mask[0])
# Записываем отделенную маску от IP в переменную
mask = int(ip_and_mask[1])
# Получаем из строки список, для обращения к октетам IP по индексам
splitted_ip_address = ip_address.split('.')
# Записываем октеты IP в отдельные переменные
ip1, ip2, ip3, ip4 = [
    int(splitted_ip_address[0]),
    int(splitted_ip_address[1]),
    int(splitted_ip_address[2]),
    int(splitted_ip_address[3]),
]

# шаблон вывода IP адреса
template = '''
IP Address:
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''
# Преобразование ip и маски в двоичный формат
bin_mask = ('1' * mask) + ('0' * (32 - mask))
bin_ip1, bin_ip2, bin_ip3, bin_ip4 = [
    format(int(splitted_ip_address[0]), '08b'),
    format(int(splitted_ip_address[1]), '08b'),
    format(int(splitted_ip_address[2]), '08b'),
    format(int(splitted_ip_address[3]), '08b')
]
bin_ip = str(bin_ip1) + str(bin_ip2) + str(bin_ip3) + str(bin_ip4)
# Записываем октеты маски в отдельные переменные
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]
bin_network = str(bin_ip[0:mask] + ('0' * (32 - mask)))
# шаблон вывода маски подсети
template_mask = '''
Mask:
{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
n1, n2, n3, n4 = [
    int(bin_network[0:8], 2),
    int(bin_network[8:16], 2),
    int(bin_network[16:24], 2),
    int(bin_network[24:32], 2),
]
template_network = '''
Network:
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
# в соотвествии с шаблоном выводим IP и маску
print(template.format(0, ip1, ip2, ip3, ip4))
print(template_mask.format(mask, m1, m2, m3, m4))
print(template_network.format(0, n1, n2, n3, n4))


