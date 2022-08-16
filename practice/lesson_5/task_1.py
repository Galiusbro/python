# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

start_str = 'Вот такой текст, содержащий "абв" = забвение, ЗимбАбвэ, а еще самозабвенность и зимбабвийский и абв'
root = 'абв'
start_str_split = start_str.split()

new_set_of_word = []
for word in start_str_split:
    if root not in word.lower():
        new_set_of_word.append(word)

new_str = " ".join(map(str, new_set_of_word))
print(new_str)
