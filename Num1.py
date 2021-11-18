from re import split
from datetime import date


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extractor(cls, param):
        cls.int_date = list(map(int, split('-', param.date)))
        return cls.int_date

    @staticmethod
    def validation(check):
        val_date = Date.extractor(check)
        try:
            date(val_date[2], val_date[1], val_date[0])
            return 'Correct date'
        except:
            return 'Incorrect date'


date1 = Date('31-11-2001')

print(date1.extractor(date1))
print(date1.validation(date1))
print(Date.validation(date1))
