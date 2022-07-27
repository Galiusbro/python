# my_file = open("BabyFile.txt", "w+")
# my_file.write("Привет, файл!")
# my_file.close()

# exit()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


import time

a = str(time.time())
a = a[-1] + a[-2]
print(a)