"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

cnt = 0
for symbol_num in range(32, 128):
    if cnt == 10:
        print()
        cnt = 0
    print(f"{symbol_num} - '{chr(symbol_num)}'", end='\t')
    cnt += 1
