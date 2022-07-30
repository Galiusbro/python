# Вычислить число pi c заданной точностью d 
# Пример: - при d = 0.001, π = 3.141.   10^{-1} ≤ d ≤10^{-10}


d = len(input('Укажите точность вычисления Пи (Пример 0.01): '))
print(d)

def pi_calculation(accuracy):
    if accuracy > 12:
        print('Точность задана вне диапазона 10^{-1} ≤ d ≤10^{-10}. \nПопробуйте снова')        
    else:
        pi = '3.1415926535'
        print(f'Число пи с точностью до 10го знака после запятой: \n{pi}')
        pi = pi[0:accuracy]

        s = 3
        i = 1
        sgn = 1
        while str(s)[:d] != pi :
            s +=sgn/(i*(i+1)*(2*i+1))
            sgn *= -1
            i += 1
        print(str(s)[0:accuracy])

pi_calculation(d)
