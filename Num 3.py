info = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
while index in range(len(info)):
    if info[index][0:].isdigit() or info[index][1:].isdigit():
        if len(info[index]) < 2:
            info[index] = '0' + info[index][:1]
        elif (int(info[index]) or (-int(info[index]))) < 10:
            info[index] = f'{info[index][:1]}0{info[index][1:]}'
        info[index] = ''.join(['"', info[index], '"', ' '])
    info[index] = ''.join([info[index], ' '])
    index = index + 1
print(''.join(info))
