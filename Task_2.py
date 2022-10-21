# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = input('Введите размер списка: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)

new_list = []
# new_list = [2, 3, 4, 5, 6]
# n = len(new_list)

new_list1 = []
import random

for i in range(n):
    a = random.randint(0,30)
    new_list.append(a)


b = 0
for i in range(b,n-1):
    if b<n:
        a = new_list[b] * new_list[n-1]
        new_list1.append(a)
        b += 1
        n -= 1

print(new_list)
print(new_list1)