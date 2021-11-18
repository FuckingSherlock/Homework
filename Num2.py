import traceback


class OwnException(Exception):
    def __str__(self):
        return "Сидра перепил? На ноль нельзя делить!"


divisible = input()
divider = input()

try:
    divisible = int(divisible)
    divider = int(divider)
    result = divisible/divider
except ZeroDivisionError:
    try:
        raise OwnException
    except OwnException as exc:
        print(traceback.format_exc())
# except ValueError:
#     raise ValueError
else:
    print(f'{divisible}/{divider}={result}')

print('Код продолжает выполнение...')
