import re

name_domain = {}


def email_parse(email):
    if re.match(r'\w+@[a-z]+\.\w+', email):
        RE_NAME = re.compile(r'\w{1,}(?=@)')
        RE_DOMAIN = re.compile(r'(?<=\@)[a-z]+\b\.\w+')
        name_domain.setdefault(RE_NAME.findall(
            email)[0], RE_DOMAIN.findall(email)[0])
        print(name_domain)
    else:
        raise ValueError(f'Неверный email: {email}')


email_parse('soeone@geebrains.ru')
