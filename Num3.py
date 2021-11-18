import traceback


class OwnException(Exception):
    def __init__(self, inp):
        self.inp = inp

    def __str__(self):
        if not self.inp.isdigit():
            return "Вы ввели не число"


nums = []
while True:
    inp = input()
    try:
        inp = int(inp)
    except:
        try:
            raise OwnException(inp)
        except OwnException as exc:
            print(traceback.format_exc())
    else:
        nums.append(inp)
    print(nums)
