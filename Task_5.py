# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = input('Задайте число до которого высчитывать список: ')

def is_int(k):
    try:
        int(k)
    except:
        print('Введено не корректное число.')
        quit()

is_int(n)
n = int(n)


if n<0:
    n*=-1

new_list = []
new1_list = []

def negafib(n):
    if n==-1:
        return 1
    elif n==-2:
        return -1
    else:
        return negafib(n+2) - negafib(n+1)

for e in range(-n, 0):
    new_list.append(negafib(e))

new_list.append(0) 

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for e in range(1, n+1):
    new_list.append(fib(e))

print(new_list)
