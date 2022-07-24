# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите любое вещественное число: ')

def sum_of_digits(num):
    sum = 0
    for digit in num:
        if digit.isdigit():
            sum += int(digit)
    return sum


print(f'Сумма всех цифр числа = {sum_of_digits(num)}')
