staff = ["Иван", "Мария", "Петр", "Илья"]


def thesaurus(names):
    general = {}
    for i in names:
        key = i[0]
        general.setdefault(key, [i])
        if i not in general[key]:
            general[key].append(i)
    print(general)


thesaurus(staff)
