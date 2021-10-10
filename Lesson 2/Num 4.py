workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in workers:
    splited = ''.join(i).split(' ')
    name = splited.pop(-1)
    print('Привет,', name.title()+'!')
