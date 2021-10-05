duration = int(input())
m = duration // 60
h = duration // 3600
d = duration // 86400
if duration < 60:
    s = duration
    print(s, 'сек')
elif 3600 > duration >= 60:
    s = duration % 60
    print(m, 'мин', s, 'сек')
elif 86400 > duration >= 3600:
    s = duration % 60
    m = m % 60
    print(h, 'час', m, 'мин', s, 'сек')
elif duration >= 86400:
    s = duration % 60
    m = m % 60
    h = h // 7
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
