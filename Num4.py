import json

hobby = open('hobby.csv', 'r')
users = open('users.csv', 'r')

my_dict = {i.strip().replace(',', ' '): 0 for i in users}

for u in my_dict:
    my_dict[u] = hobby.readline().replace(',', ', ').replace('\n', '')
    if my_dict[u] == '':
        my_dict[u] = 'None'

hobby.seek(0)

if len(my_dict) < sum(1 for line in hobby):
    exit(1)

hobby.close()
users.close()

with open('users_hobby.json', 'w+', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)
    f.seek(0)
    print(f.read())
