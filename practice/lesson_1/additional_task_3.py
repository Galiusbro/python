# найти наибольший простой делитель числа

bigNum = int(input('Введите число: '))


largest_prime_divisor = 0
divisor = 2
while divisor * divisor <= bigNum:
    if bigNum % divisor == 0:
        largest_prime_divisor = divisor
        bigNum //= divisor
    else:
        divisor += 1
if bigNum > 1:
    largest_prime_divisor = bigNum

print('Hаибольший простой делитель:', largest_prime_divisor)