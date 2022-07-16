# найти факториал числа

n = int(input('Укажите факториал какого числа будем считать: '))
 
factorial = 1
 
for i in range(2, n+1):
    factorial *= i
     
print(factorial)
