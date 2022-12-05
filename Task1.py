#                       Задача 1
# Вычислить число Пи c заданной точностью d
# Пример:  - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

# Для красоты будем чистить консоль при каждом запуске
import os
os.system('clear')

import math

print("Задача вычислить число Пи c заданной точностью d")
d = str(input("Введите число d: "))
print(math.pi)
d_len = len(d.split('.')[1])

# (максимум 15 знаков после запятой)
i = 0
num_pi = str(math.pi)
while i < (d_len + 2) and i < len(num_pi):
    print(num_pi[i], end="")
    i += 1