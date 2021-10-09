# Задача 3
# Вариант выполнения 2
one_end = list(range(21, 92, 10))+[1]
two_end = list(range(2, 5))
exceptions = list(range(11, 15))
n = 1
last = n % 10


def func():
    global n, last
    n += 1
    last = n % 10


while n <= 100:
    if n in exceptions:
        print(n, 'процентов')
        func()
    elif last in two_end:
        print(n, 'процента')
        func()
    elif last in one_end:
        print(n, 'процент')
        func()
    else:
        print(n, 'процентов')
        func()
