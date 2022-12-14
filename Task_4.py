# Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


n = input('Задайте число: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)
a = n
if n<0:
    n *=-1
elif n == 0:
    print(f'Число 0 в двоичной системе будет 0')
    quit()

new_list = []

while n != 0:
    c = n%2
    n = n//2
    new_list.append(c)

res_1 = "".join(map(str,new_list))

if a > 0:  # Если введено положительное число
    res = res_1[::-1]
else:  # Если введено отрицательное число
    k = '-'
    res = k + res_1[::-1]
print()
print(f'Число {a} в двоичной системе будет {res}')    

