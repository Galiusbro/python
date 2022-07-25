# Реализуйте алгоритм перемешивания списка.

import random

a = ["1", "2", "3", "4", "5", "6"]

def shuffle(a):
    for index, element in enumerate(a):
        index1 = random.randrange(len(a))
        index2 = random.randrange(len(a))
        a[index1], a[index2] = a[index2], a[index1]
    return a

print(shuffle(a))
