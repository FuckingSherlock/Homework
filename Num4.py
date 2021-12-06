from functools import wraps


def val_checker(decor_func):
    def _val_checker(func_clack):
        @wraps(func_clack)
        def wrapped(x):
            if decor_func(x):
                return func_clack(x)
            else:
                raise ValueError(x)
        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
