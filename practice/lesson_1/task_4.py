# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print(f'x > 0 до ∞')
    print(f'y > 0 до ∞')
elif quarter == 2:
    print(f'x < 0 до -∞')
    print(f'y > 0 до ∞')
elif quarter == 3:
    print(f'x < 0 до -∞')
    print(f'y < 0 до -∞')
elif quarter == 4:
    print(f'x > 0 до ∞')
    print(f'y < 0 до -∞')
else:
    print('такой четверти не существует')