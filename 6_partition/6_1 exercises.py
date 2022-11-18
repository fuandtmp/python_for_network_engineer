# https://pyneng.readthedocs.io/ru/latest/exercises/06_exercises.html
# 6.1
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
i = 0
while i <= len(mac) - 1:
    result.append(mac[i].replace(':', '.'))
    i += 1
print(result)

