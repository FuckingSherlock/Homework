# modul VALUTES
import re
import requests
import decimal
import datetime
import sys


def currency_rates(VAL):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    valute = re.split('Date="|"|ID', response.text)
    days, month, years = map(int, valute[5].split('.'))
    date = datetime.datetime(years, month, days)
    for i in valute:
        if i.find(f'<CharCode>{VAL}</CharCode>') != -1:
            cource = decimal.Decimal(
                re.split('<Value>|</Value>', i)[1].replace(',', '.'))
            return(f'Курс {VAL} к рублю на {date} равен {cource}')
    return None


if __name__ == '__main__':
    val = sys.argv[1]
    print(currency_rates(val))
