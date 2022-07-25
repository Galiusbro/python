# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


a = (-10, 5, 4, 6, -2, 16, 2)
 
file = open('file.txt', 'r')

lines = file.readlines()

for n, line in enumerate(lines):
    index1 = int(lines[n])
    print(f'index1 = {index1}')
    index2 = int(lines[n+1])
    print(f'index2 = {index2}')
    res = a[index1] * a[index2]
    print(res)

file.close
