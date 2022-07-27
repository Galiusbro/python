# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_list = [1.1, 1.2, 3.1, 5, 10.01]

def max_after_point(a):
    max = a[0] % 1
    for index in range(len(a)):
        if max < a[index] % 1: max = a[index]
    return max

def min_after_point(a):
    min = a[0] % 1
    for index in range(len(a)):
        if min > a[index] % 1: min = a[index]
    return min

max = max_after_point(my_list)
min = min_after_point(my_list)

print(round((max - min) % 1, 2))
