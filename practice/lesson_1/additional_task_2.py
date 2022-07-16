# проверить число на простоту (т.е. что число делится только на 1 и само на себя)

prime = int(input('Введите число и проверим, простое ли оно: '))

if prime < 2: 
    print('Число меньше двух не является простым.')
else:
    count = 0
    for i in range(2, prime // 2):
        if prime % i == 0:
            count = count + 1
    if count == 0:
        print('Число простое')
    else:
        print('Число не является простым')
