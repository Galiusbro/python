# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]

def check_list(a):
    b = 0
    for i in range(len(a)):
        if i % 2 != 0:
            b += a[i]
    return b

print(check_list(my_list))
