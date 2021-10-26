import requests

response = requests.get(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

result = []
search = []

with open('nginx_logs.txt', 'w+') as f:
    f.writelines(response.content.decode('UTF-8'))
    f.seek(0)
    for l in f:
        line = l.split(' ')
        result.append((line[0], line[5], line[6]))
        search.append(l.split(' ')[0])

my_dict = {i: 0 for i in search}

for i in search:
    my_dict[i] += 1

# Полный отчет:
for i in my_dict:
    print(f'IP {i} sent {my_dict[i]} request(s)')

# Спаммер:
keymax = max(my_dict, key=my_dict.get)
print(f'Spammer is {keymax} he sent {my_dict[keymax]} request(s)')
