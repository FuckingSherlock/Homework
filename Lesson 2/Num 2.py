info = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
indexes = []
new_info = []
for i in info:
    temp = list(i)
    for any in temp:
        if any.isdigit():
            indexes.append(info.index(i))

    if info.index(i) in indexes:
        i = int(i)
        if i < 10:
            temp.insert((temp.index(i)-4), '0')
            info[i] = ''.join(temp)
        i = str(i)
        new_info.extend(['"', i, '"', ' '])
    else:
        new_info.extend([i, ' '])
sring = ''.join(new_info)
print(sring)

# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
#   'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']


# в "05" часов "17" минут температура воздуха была "+05" градусов
