import sys


def show(param1, param2):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if param1 == param2 == 0:
            for line in f:
                print(line.strip())
        elif param2 != 0:
            line_num = 0
            line_num2 = 0
            for line in f:
                if int(param1)-1 != line_num:
                    line_num += 1
                else:
                    if int(param2) > (line_num + line_num2):
                        print(line.strip())
                        line_num2 += 1
        elif param1 != 0:
            line_num = 0
            for line in f:
                if int(param1)-1 != line_num:
                    line_num += 1
                else:
                    print(line.strip())


if __name__ == '__main__':
    arg2 = 0
    arg1 = 0
    if len(sys.argv) == 2:
        arg1 = sys.argv[1]
    elif len(sys.argv) == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    show(arg1, arg2)
