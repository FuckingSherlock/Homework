import requests
import re


response = requests.get(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('logs.txt', 'w+') as f:
    f.writelines(response.content.decode('UTF-8'))
    f.seek(0)
    for line in f:
        PARSING = re.compile(
            r'(?:\d+\.){3}\d+|(?:\w+:)+\w+|(?<=\[).+(?=])|(?<=\")\w+(?=\s+\/)|/\w+/\w+_\d|(?<=\s)\d+(?=\s+)')
        parsed_raw = tuple(PARSING.findall(line)[:6])
        print(parsed_raw)
