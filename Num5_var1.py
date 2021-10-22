import timeit
from random import randint

# "В лоб"
src = [randint(0, 100) for _ in range(3000)]
result = [i for i in src if src.count(i) == 1]

code_to_test = """
from random import randint
src = [randint(0, 100) for _ in range(3000)]
result = [i for i in src if src.count(i) == 1]
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
