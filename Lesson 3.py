nm = input('Имя:')
snm = input('Фамилия:')
age = int(input('Возраст:'))
wt = int(input('Вес:'))
if (age <= 30) and (50 <= wt <= 120):
    print(nm, snm+',', age, 'год, вес', wt, '- хорошее состояние')
elif (age <= 30) and (50 > wt or wt > 120):
    print(nm, snm+',', age, 'год, вес', wt, '- следует правильно питаться')
elif (age > 30) and (wt < 50 or wt > 120):
    print(nm, snm+',', age, 'год, вес', wt, '- требуется заняться собой')
elif (age >= 40) and (wt < 50 or wt > 120):
    print(nm, snm+',', age, 'год, вес', wt, '- следует обратится к врачу!')
else:
    print('Пликлиника закрыта на карантин')
