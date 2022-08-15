# Создать текстовый файл (не программно). 
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.


with open('salary.txt', 'r', encoding='utf-8') as f:
    rows = list(f.read().splitlines())

    data = []

    for i in range(len(rows)):
        data.append(rows[i].split())
    
    count = 0
    for key, value in data:
        count += float(value)
        if  float(value) <= 20000.00:
            print(key)
    print(count)
    print(f'Средний доход {len(rows)} сотрудников = {count / len(rows)}')