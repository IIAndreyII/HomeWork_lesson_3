# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = input('Задайте длинну списка: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)
new_list = []
new_list1 = []

import random
for i in range(0,n):
    
    a = random.randint(0,9) + round(random.random(),2)
    b = round(a%1,2)
    new_list.append(a)
    new_list1.append(b)


print(new_list)
print(new_list1)
print((max(new_list1)) - (min(new_list1)))



