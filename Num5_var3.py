import timeit
from random import randint

src = [randint(0, 100) for _ in range(3000)]


def gen():
    my_dict = {i: 0 for i in src}
    for i in src:
        my_dict[i] += 1
    for i in my_dict:
        if my_dict[i] == 1:
            yield i


result = [gen()]

code_to_test = """
from random import randint
src = [randint(0, 100) for _ in range(3000)]


def gen():
    my_dict = {i: 0 for i in src}
    for i in src:
        my_dict[i] += 1
    for i in my_dict:
        if my_dict[i] == 1:
            yield i


list5 = [gen()]
"""
elapsed_time = timeit.timeit(code_to_test, iber=100)/100
print(elapsed_time)
