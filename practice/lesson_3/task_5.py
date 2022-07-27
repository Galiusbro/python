# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример: - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


num = int(input('Задайте число: '))

def fibonacci(n):
    a, b = 0, 1
    my_lis = [1, 0, 1]
    if n == 0: my_lis = [0]
    elif n > 1:
        for i in range(n - 1):

            if i % 2 == 0: my_lis.insert(0, (a + b) * -1)
            else: my_lis.insert(0, (a + b))

            my_lis.append(a+b)

            a, b = b, a + b

    return my_lis

print(fibonacci(num))
