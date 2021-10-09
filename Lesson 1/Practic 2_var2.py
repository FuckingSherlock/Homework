# Задача 2
# Вариант выполнения 2
# Решение всей задачи без создания дополнительных списков
coubs = [i**3 for i in list(range(1, 1001, 2))]


def check(lt, point):
    for i in lt:
        i_str = str(i)
        i_list = list(i_str)
        result = [int(item) for item in i_list]
        if sum(result) % 7 == 0:
            point.append(i)
    print(sum(point))


check(coubs, list())
coubs = [i + 17 for i in coubs]
check(coubs, list())
