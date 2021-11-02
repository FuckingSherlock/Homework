from functools import wraps


def val_checker(func):
    if func == True:
        print('yes')
    return func


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(5)

# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
#
