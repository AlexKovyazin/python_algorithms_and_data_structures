"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

user_num = int(input('Введите количество элементов ряда чисел: '))
var = 1
res = 0

for i in range(user_num):
    res += var
    var = var / (-2)
print(res)