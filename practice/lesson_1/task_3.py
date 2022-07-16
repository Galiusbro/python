# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

coord_x = int(input('X = '))
coord_y = int(input('Y = '))

if coord_x > 0 and coord_y > 0:
    print('1')
elif coord_x < 0 and coord_y > 0:
    print('2')
elif coord_x < 0 and coord_y < 0:
    print('3')
elif coord_x > 0 and coord_y < 0:
    print('4')
else:
    print('Введено нулевое значение. Попробуйте снова')