import sys


def add(data):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(f'{data}\n')


if __name__ == '__main__':
    inp = sys.argv[1]
    add(inp)
