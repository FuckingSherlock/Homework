import re
import requests


response = requests.get(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('logs.txt', 'w+') as f:
    f.writelines(response.content.decode('UTF-8'))
    f.seek(0)
    for line in f:
        spl = re.split(' |\[|\]|"', line)
        parsed_raw = (spl[0], spl[4]+' '+spl[5], spl[8],
                      spl[9], spl[12], spl[13])
        print(parsed_raw)
