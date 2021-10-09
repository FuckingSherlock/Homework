info = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
new_info = []
for i in info:
    temp = list(i)
    for any in temp:
        if any.isdigit():
            if int(''.join(temp)) < 10:
                temp.insert(-1, '0')
                i = ''.join(temp)
            i = ''.join(['"', i, '"', ' '])
            break
    i = ''.join([i, ' '])
    new_info.append(i)
print(''.join(new_info))
