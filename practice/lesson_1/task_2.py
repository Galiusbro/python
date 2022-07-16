# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = 1
y = 2
z = 3

left = not (x or y or z)
right = not x and not y and not z
result = left == right

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
