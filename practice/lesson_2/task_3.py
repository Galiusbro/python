# Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
# Привер - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


num = int(input('Введите целое число: '))

def subsequence(num):
    res = 0
    a = {1: 1}
    for n in range(2, num + 1):
        res += (1 + (1/n)) ** n
        a[n] = round(res)
    return a

print(subsequence(num))
