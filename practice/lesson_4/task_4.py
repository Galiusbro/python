# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# p(x) = a0 * x^k + a1 * x^(k -1) + a2 * x^(k - 2) + ... + a(k - 1) * x + ak

import random

k = int(input('Введите натуральную степень многочлена k: '))

def polynomial(k):
    c = [random.randint(0, 100) for i in range(k+1)]

    s = ''
    for i in range(k):
        if c[i] > 0: s = s + str(c[i]) + f'*x**{k-i} + '
    if c[k] > 0: s = s + str(c[k]) + ' = 0'
    print(f'Многочлен {s} записан в файл')
    return s

with open('file.txt', 'w') as file:
    file.writelines(polynomial(k))
