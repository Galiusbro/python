# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

def mult_from_end(a):
    b = []
    
    for index in range(len(a) // 2):
        b.append(a[index]*a[-index -1])

    if len(a) % 2 != 0:
        b.append(a[len(a) % 2 + 1] ** 2)

    return b

print(mult_from_end(my_list))
