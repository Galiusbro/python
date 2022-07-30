# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from posixpath import split


def original_numbers(my_list):
    my_list = list(map(int, my_list.split())) # на сколько красиво делать вот так? или лучше избегать таких методов?

    new_list = []
    
    for element in my_list:
        if element not in new_list:
            new_list.append(int(element))
    return new_list

my_list = input('Задайте последовательность чисел через пробел: ')

print(original_numbers(my_list))
