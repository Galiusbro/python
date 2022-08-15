# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import operator

def read_poly(file):
    import re
    with open(file, 'r') as file:
        for poly in file:
            print(poly)
            s = [int(s) for s in re.findall(r'-?\d+\.?\d*', poly)]
    return(s)

def create_dic(poly):
    poly_dictionary = {}
    value = [poly[i] for i in range(len(poly)) if i % 2]
    keys = [poly[i] for i in range(len(poly)) if not i % 2]
    poly_dictionary = dict(zip(value, keys))
    return poly_dictionary


poly1 = create_dic(read_poly('file.txt'))
poly2 = create_dic(read_poly('file1.txt'))

tuples_of_poly = (poly1, poly2)

resultdict = {}

for dictionary in tuples_of_poly:
    for key in dictionary:
        try:
            resultdict[key] += dictionary[key]
        except KeyError:
            resultdict[key] = dictionary[key]

sorted_tuples = list(sorted(resultdict.items(), key=operator.itemgetter(1)))
print(sorted_tuples)

# Не могу понять как правильно вывести результат
# Прошу помощи!