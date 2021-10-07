# Задача 2
# Вариант выполнения 1
nums = list(range(1, 1001, 2))
coubs = [i**3 for i in nums]
sum_of_digits = []
sum_of_digits_17 = []
for i in coubs:
    if sum(map(int, str(i))) % 7 == 0:
        sum_of_digits.append(i)
print(sum(sum_of_digits))
coubs = [i+17 for i in coubs]
for i in coubs:
    if sum(map(int, str(i))) % 7 == 0:
        sum_of_digits_17.append(i)
print(sum(sum_of_digits_17))
