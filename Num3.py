tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) <= len(klasses):
    tpl = ((tutors[i], klasses[i]) for i in range(len(tutors)))
    print(*tpl, sep='\n')
else:
    tpl = ((tutors[i], klasses[i]) for i in range(len(klasses)))
    print(*tpl, sep='\n')
    tpl = ((tutors[i+len(klasses)], 'None')
           for i in range((len(tutors) - len(klasses))))
    print(*tpl, sep='\n')

print(type(tpl))  # Доказательство генератора
