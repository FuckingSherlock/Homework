# Задача 3
# Вариант выполнения 1
one_end = list(range(21, 100, 10))+[1]
two_end = list(range(2, 5))
exceptions = list(range(11, 15))
n = 1
end = n % 10
while n <= 100:
    if n in exceptions:
        print(n, 'процентов')
        n += 1
        end = n % 10
    elif end in two_end:
        print(n, 'процента')
        n += 1
        end = n % 10
    elif end in one_end:
        print(n, 'процент')
        n += 1
        end = n % 10
    else:
        print(n, 'процентов')
        n += 1
        end = n % 10
