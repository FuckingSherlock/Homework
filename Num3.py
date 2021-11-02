from functools import wraps


def type_logger(func):
    @wraps(func)
    def tag_logger(*args, **kwargs):
        markup = ''
        for a in args:
            markup += f'{func.__name__}({str(a)}: {type(a)})'
            if (args.index(a) != args.index(args[-1])) or (kwargs and args):
                markup += ', '
        kwargs = list(kwargs.values())
        for k in kwargs:
            if args or len(kwargs) > 1:
                markup += f'{func.__name__}({str(k)}: {type(k)})'
            if kwargs.index(k) != kwargs.index(kwargs[-1]):
                markup += ', '
        return markup
    return tag_logger


@type_logger
def calc_cube(x, y):
    return x ** 3 * y


print(calc_cube(5.4, 5, name='rt', df=89))
