#!/usr/bin/env python

## web browser module

import webbrowser

url_lists = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.google.com'
]

# for url in url_lists:
#     webbrowser.open_new_tab(url)

# requests

import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

# <Response [200]>
# 200
# {'date': 'Wed, 22 Sep 2021 02:30:48 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Thu, 22 Sep 2022 02:30:48 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'x-backend': 'ssl-mirrors', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}

# requests api

import requests

url = 'https://www.gstatic.com/ct/log_list/v2/log_list.json'
response = requests.get(url)
print(response)
print(response.status_code)
obj = response.json()
print(obj['operators'][:1])


from mypackage import arithmetics
print(arithmetics.add_numbers(1,2,3,4)) # 10
print(arithmetics.subtract(5,3)) # 2
print(arithmetics.multiple(5,3)) # 15
print(arithmetics.division(5,3)) # 1.6666666666666667
print(arithmetics.remainder(5,3))  # 2
print(arithmetics.power(5,3))  # 2

from mypackage import greet
print(greet.greet_person('liang', 'cheng')) # liang cheng, welcome to xxx

