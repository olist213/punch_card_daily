#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :web_scraping.py
@说明    :
@时间    :2021/09/26 19:22:27
@作者    :liangcheng
@版本    :1.0
'''


import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

status = response.status_code
print(status) # 200


import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpading':'3'})

table = tables[0]

for td in table.find('tf').find_all('td')
    print(td.text)
