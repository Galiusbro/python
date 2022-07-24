#n = int(input('Число: '))
#factor = int(input('множитель: '))
#
#def subsequence(n, core):
#    list = [1]
#    for i in range(n-1):
#        list.append(list[-1] * core)
#    print(list)
#
#subsequence(n, factor)




strA = 'Hello world! Hello Hello Hello'
strB = 'Hello'

def findsymbol(a, b):
    count = 0
    for i in range(len(a) - len(b)):
        if a[i :i + len(b)] == b: count += 1
    return count

print(findsymbol(strA, strB))
