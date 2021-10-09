info = ['в', '5', 'часов', '17', 'минут',
        'температура', 'воздуха', 'была', '+5', 'градусов']
indexes = []
new_info = []
for i in info:
    temp = list(i)
    for any in temp:
        if any.isdigit():
            if int(''.join(temp)) < 10:
                temp.insert(-1, '0')
                i = ''.join(temp)
                # indexes.append(info.index(i))
            # else:
            #     # indexes.append(info.index(i))
            # print(i)
            new_info.extend(['"', i, '"', ' '])
        else:
            new_info.extend([i, ' '])
print(''.join(new_info))
#     if info.index(i) in indexes:
#         new_info.extend(['"', i, '"', ' '])
#     else:
#         new_info.extend([i, ' '])
# print(''.join(new_info))
