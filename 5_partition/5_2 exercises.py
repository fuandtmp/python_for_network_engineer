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
# шаблон вывода IP адреса
template = '''
IP Address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
# Преобразование маски в двоичный формат
bin_mask = ('1' * mask) + ('0' * (32 - mask))

# Записываем октеты маски в отдельные переменные
m1, m2, m3, m4 = [
    int(bin_mask[0:8], 2),
    int(bin_mask[8:16], 2),
    int(bin_mask[16:24], 2),
    int(bin_mask[24:32], 2),
]
# шаблон вывода маски подсети
template_mask = '''
Mask:
{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
# в соотвествии с шаблоном выводим IP и маску
print(template.format(int(splitted_ip_address[0]), int(splitted_ip_address[1]), int(splitted_ip_address[2]),
                      int(splitted_ip_address[3])))
print(template_mask.format(mask, m1, m2, m3, m4))
