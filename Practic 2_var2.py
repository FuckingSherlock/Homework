# Задание 2
# Вариант выполнения 2 
# (*Решение задачи под пунктом b, не создавая новый список.)
nums = list(range(1, 1001, 2))
coubs = [i**3 for i in nums]
sum_of_digits = []


def check(lt, point):
    for i in lt:
        i_str = str(i)
        i_list = list(i_str)
        result = [int(item) for item in i_list]
        if sum(result) % 7 == 0:
            point.append(i)
    print(sum(point))


check(coubs, sum_of_digits)
coubs = [i + 17 for i in coubs]
sum_of_digits = []
check(coubs, sum_of_digits)
