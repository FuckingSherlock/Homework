price = [234.5, 476.33, 22, 560, 126, 500.8,
         367.9, 40, 32.7, 634.5, 110, 74.4,
         765, 233, 750, 264.3, 65.6,
         845, 68, 886.45]


def prices(price_list):
    for i in price_list:
        i = str(i)
        temp = i.split('.')
        if len(temp) > 1:
            if int(temp[1]) < 10:
                temp.append('0' + temp.pop(1))
        else:
            temp.append('00')
        print(f'{temp[0]} рублей {temp[1]} копеек')
    print()


prices(price)
print('id до сортировки =', id(price), '\n')
price.sort()
print('id после сортировки =', id(price), '\n')
prices(price)
price_decreasing = sorted(price, reverse=True)
print(price_decreasing)
price.reverse()
price = price[0:5]
price.reverse()
prices(price)
