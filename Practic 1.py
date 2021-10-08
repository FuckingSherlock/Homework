# Задача 1
duration = int(input())
second = duration % 60
minutes = duration % 60
hours = duration // 3600
days = duration // 86400
if duration < 60:
    print(duration, 'сек')
elif 3600 > duration >= 60:
    minutes = duration // 60
    print(minutes, 'мин', second, 'сек')
elif 86400 > duration >= 3600:
    minutes = duration // 60 % 60
    print(hours, 'час', minutes, 'мин', second, 'сек')
else:
    hours = duration % 86400 // 3600
    print(days, 'дн', hours, 'час', minutes, 'мин', second, 'сек')
