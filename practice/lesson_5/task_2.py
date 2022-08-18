# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


candies = 120
take_limit = 28
player_1 = 1
player_2 = 2

print('ЖЕРЕБЬЕВКА! Если выпадет 1 - ходит игрок. Если 2 - комп!\n')
turn = randint(1,2)
print(f'Выпало = {turn}\n')
print(f'Осталось {candies} конфет\n')

 
while candies > 0:
  if candies < take_limit: take_limit = candies
  if turn == 1:
      print('Бери конфеты, ИГРОК!')
      take_palyer_1 = int(input('Сколько конфет берет игрок?: '))
      while turn == 1:
          if take_palyer_1 > 0 and take_palyer_1 < take_limit +1:
              candies = candies - take_palyer_1
              print(f'Осталось {candies} конфет!\n')
              turn = 0
          else: take_palyer_1 = int(input(f'Вы можете взять от 1 до {take_limit} конфет! :'))
            
    
  else:
    if candies > 28:
      take_player_2 = randint(1, take_limit)
    else:
      take_player_2 = candies
    print(f'Комп взял {take_player_2} конфет')
    candies = candies - take_player_2
    print(f'Осталось {candies} конфет!\n')
    turn = 1

if turn == 0:
  print('YOU WIN!')
else:
  print('LOSER!')
  