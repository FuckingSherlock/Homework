import timeit
from random import randint

src = [randint(0, 100) for _ in range(3000)]

my_dict = {i: 0 for i in src}
for i in src:
    my_dict[i] += 1
result = [i for i in my_dict if my_dict[i] == 1]
print(result)


code_to_test = """
from random import randint
src = [randint(0, 100) for _ in range(3000)]
my_dict = {i: 0 for i in src}
for i in src:
    my_dict[i] += 1
result = [i for i in my_dict if my_dict[i] == 1]
"""

elapsed_time = timeit.timeit(code_to_test, iber=100)/100
print(elapsed_time)
