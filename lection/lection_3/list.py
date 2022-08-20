# list = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

def f(x):
    return x**3

def k(x):
    return (x-x) - x**2

list = [(i, f(i), i**2, k(i)) for i in range(1, 11) if i % 2 == 0]
print(list)

la = lambda x, y: x + y if x < y else x*y

print(la(2,5))