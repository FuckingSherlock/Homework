info = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
new_info = []
for i in info:
    if list(i).pop(-1).isdigit():
        if int(i) < 10:
            i = list(i)
            i.insert(-1, '0')
            i = ''.join(i)
        i = ''.join(['"', i, '"', ' '])
    i = ''.join([i, ' '])
    new_info.append(i)
print(''.join(new_info))
