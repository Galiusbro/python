# def where(f, col):
#     return[x for x in col if f(x)]

data = '1 2 3 4 5 8 15 23 38'.split()

res = map(int, data)
res = list(filter(lambda x: not x%2, res))
print (res)
res = list(map(lambda x:(x, x**2), res))
print(res)


# data = list(map(int, '1 2 3 4 555 6'.split()))


# for e in data:
#     print(e)

# print('========>')

# for e in data:
#     print(e)

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)