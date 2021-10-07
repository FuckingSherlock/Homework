# Задача 2
nums = list(range(1, 1000, 2))
coubs = [i**3 for i in nums]
# print(coubs)


# temp = [sum(map(int, str(n))) for n in coubs]
# while
#     temp.append
#     coubs.remove
# print(temp)


# sum_of_digits = 0
# sum_of_digits_17 = 0
# for i in temp:
#     if i % 7 == 0:
#         sum_of_digits += i
#     if (i+17) % 7 == 0:
#         sum_of_digits_17 += (i+17)
# print(sum_of_digits)
# print(sum_of_digits_17)


# def multipy(a, b, c):
#     for i in a:
#         if i not in b:
#             b.append(i)
#     for i in b:
#         if i % 7 == 0:
#             c.append(i)
#     return(sum(c))


# print(multipy(temp, sum_of_digits, aliquot))
# print(sum(aliquot))  # Сумма чисел, сумма цифр которых % 7 == 0
