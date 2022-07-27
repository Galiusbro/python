# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))

def dec_in_binar(n):
    flag = 0
    if n < 0:
        n = n * -1
        flag = 1

    binar = ''    
    while n > 0:
        binar = str(n % 2) + binar
        n = n // 2

    if flag > 0: binar += '1'
    return binar

print(dec_in_binar(num))
