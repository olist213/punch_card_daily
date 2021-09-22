# day20 pip

![30DaysOfPython](https://github.com/Asabeneh/30-Days-Of-Python/raw/6e96bc3e1f2b55667d6fd07758af12b6595545f5/images/30DaysOfPython_banner3@2x.png)

---

## 什么是PIP？

pip是首选安装程序的意思，使用pip来安装不同的python包，python包包含了一个或多个python模块，通过引入python包将其导入到应用程序中，不必编写每一个应用程序。

## 安装pip

如果你还没有安装，下面的命令是pip的安装方式。

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py  
```

在终端输入以下命令检查是否安装成功。

```bash
pip --version
pip 21.2.1 from /opt/homebrew/lib/python3.9/site-packages/pip (python 3.9)
```

正如你看到的，我当前使用的版本为21.2.1，如果你看到和如上的输出，那就说明pip已安装。

让我们看看Python社区中用于不同目的的一些包。只是为了让你知道，有很多包可以用于不同的应用。

- NumPy是用Python进行科学计算的基本软件包，包含如下内容：
  - 一个强大的N维数组对象
  - 复杂的（广播）功能
  - 用于集成C/C++和Fortran代码的工具
  - 有用的线性代数、傅里叶变换和随机数能力

- 安装

  - ```bash
    pip install numpy
    ```

让我们开始使用numpy,打开python交互式外壳，编写Python，然后导入numpy，如下所示。

```bash
❯ python3
Python 3.9.5 (default, May  3 2021, 19:12:05) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.20.3'
>>> lst = [1,2,3,4,5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 5
array([ 5, 10, 15, 20, 25])
>>> np_arr + 2
array([3, 4, 5, 6, 7])
```

pandas是一个开源、BSD许可的库，为python编程语言提供高性能、易于使用的数据结构和熟悉分析工具。

```bash
pip install pandas
```

接下来，让我们导入网页浏览器模块，它可以帮我们打开任何网站，这个模块默认安装在python3中。

代码：

```python
## web browser module

import webbrowser

url_lists = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.google.com'
]

for url in url_lists:
    webbrowser.open_new_tab(url)
```

## 卸载包

如果你想卸载已安装的软件包，可以使用下面的命令删除

```bash
pip uninstall packagename
```

## 列出包清单

要查看我们机器上安装的软件包。我们可以使用pip list。

```bash
pip list
```

![image-20210922101707735](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922101707735.png)



## 显示包的相关信息

显示一个包的信息。

```bash
pip show packagename
```

语法：

```python
❯ pip show pandas
Name: pandas
Version: 1.2.4
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: 
Author-email: 
License: BSD
Location: /opt/homebrew/lib/python3.9/site-packages
Requires: pytz, python-dateutil, numpy
Required-by: 
```

如果我们想得到更多的细节，只需添加--verbose

```python
❯ pip show --verbose pandas
Name: pandas
Version: 1.2.4
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: https://pandas.pydata.org
Author: 
Author-email: 
License: BSD
Location: /opt/homebrew/lib/python3.9/site-packages
Requires: pytz, numpy, python-dateutil
Required-by: 
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Python :: 3.9
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

## pip freeze

生成已安装的Python包及其版本，其输出结果适合在需求文件中使用。requirements.txt文件是一个文件，它应该包含一个 Python 项目中所有已安装的Python包。

语法：

```python
❯ pip freeze
aiohttp==3.6.2
altgraph==0.17
argcomplete==1.12.3
asgiref==3.4.1
async-timeout==3.0.1
attrs==19.3.0
backoff==1.11.1
beautifulsoup4==4.9.3
bs4==0.0.1
censys==2.0.5
```

pip freeze提供了我们所使用的安装包以及包版本，可以结合requirements.txt一起部署。

## 从url中读取

现在你已经熟悉了如何读取或写入位于你本地机器上的文件。有时，我们想从一个网站上使用URL或从一个API上读取。API是应用程序接口的意思。它是一种在服务器之间交换结构化数据的手段，主要是json数据。为了打开一个网络连接，我们需要一个叫做request的包--它允许打开一个网络连接并实现CRUD（创建、读取、更新和删除）操作。在这一节中，我们将只讨论CRUD的读取和获取部分。

安装requests模块：

```python
pip install requests
```

在requests中，可以使用get()，status_code，headers，text和json方法。

- get()：打开一个网络连接并从url中获取数据，返回一个响应对象
- status_code：获取数据后，我们可以检查操作的状态（成功、错误等）。
- headers：检查标头类型。
- text：从获取的响应对象中提取文本。
- json：提取json数据。

- 让我们从https://www.w3.org/TR/PNG/iso_8859-1.txt读取txt文件。

代码：

```python
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
```

- 让我们从api中读取数据，api是应用程序接口，它是一种在服务器之间交互结构数据的手段，主要是json数据，让我们来读取这个api中的内容：https://www.gstatic.com/ct/log_list/v2/log_list.json。

代码：

```python
import requests

url = 'https://www.gstatic.com/ct/log_list/v2/log_list.json'
response = requests.get(url)
print(response)
print(response.status_code)
obj = response.json()
print(obj['operators'][0])

<Response [200]>
200
[{'name': 'Google', 'email': ['google-ct-logs@googlegroups.com'], 'logs': [{'description': "Google 'Argon2021' log", 'log_id': '9lyUL9F3MCIUVBgIMJRWjuNNExkzv98MLyALzE7xZOM=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAETeBmZOrzZKo4xYktx9gI2chEce3cw/tbr5xkoQlmhB18aKfsxD+MnILgGNl0FOm0eYGilFVi85wLRIOhK8lxKw==', 'url': 'https://ct.googleapis.com/logs/argon2021/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2018-06-15T02:30:13Z'}}, 'temporal_interval': {'start_inclusive': '2021-01-01T00:00:00Z', 'end_exclusive': '2022-01-01T00:00:00Z'}}, {'description': "Google 'Argon2022' log", 'log_id': 'KXm+8J45OSHwVnOfY6V35b5XfZxgCvj5TV0mXCVdx4Q=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEeIPc6fGmuBg6AJkv/z7NFckmHvf/OqmjchZJ6wm2qN200keRDg352dWpi7CHnSV51BpQYAj1CQY5JuRAwrrDwg==', 'url': 'https://ct.googleapis.com/logs/argon2022/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2019-12-17T18:38:01Z'}}, 'temporal_interval': {'start_inclusive': '2022-01-01T00:00:00Z', 'end_exclusive': '2023-01-01T00:00:00Z'}}, {'description': "Google 'Argon2023' log", 'log_id': '6D7Q2j71BjUy51covIlryQPTy9ERa+zraeF3fW0GvW4=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE0JCPZFJOQqyEti5M8j13ALN3CAVHqkVM4yyOcKWCu2yye5yYeqDpEXYoALIgtM3TmHtNlifmt+4iatGwLpF3eA==', 'url': 'https://ct.googleapis.com/logs/argon2023/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2019-12-17T18:38:01Z'}}, 'temporal_interval': {'start_inclusive': '2023-01-01T00:00:00Z', 'end_exclusive': '2024-01-01T00:00:00Z'}}, {'description': "Google 'Xenon2021' log", 'log_id': 'fT7y+I//iFVoJMLAyp5SiXkrxQ54CX8uapdomX4i8Nc=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAER+1MInu8Q39BwDZ5Rp9TwXhwm3ktvgJzpk/r7dDgGk7ZacMm3ljfcoIvP1E72T8jvyLT1bvdapylajZcTH6W5g==', 'url': 'https://ct.googleapis.com/logs/xenon2021/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2019-06-17T21:23:01Z'}}, 'temporal_interval': {'start_inclusive': '2021-01-01T00:00:00Z', 'end_exclusive': '2022-01-01T00:00:00Z'}}, {'description': "Google 'Xenon2022' log", 'log_id': 'RqVV63X6kSAwtaKJafTzfREsQXS+/Um4havy/HD+bUc=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE+WS9FSxAYlCVEzg8xyGwOrmPonoV14nWjjETAIdZvLvukPzIWBMKv6tDNlQjpIHNrUcUt1igRPpqoKDXw2MeKw==', 'url': 'https://ct.googleapis.com/logs/xenon2022/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2019-06-17T21:23:01Z'}}, 'temporal_interval': {'start_inclusive': '2022-01-01T00:00:00Z', 'end_exclusive': '2023-01-01T00:00:00Z'}}, {'description': "Google 'Xenon2023' log", 'log_id': 'rfe++nz/EMiLnT2cHj4YarRnKV3PsQwkyoWGNOvcgoo=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEchY+C+/vzj5g3ZXLY3q5qY1Kb2zcYYCmRV4vg6yU84WI0KV00HuO/8XuQqLwLZPjwtCymeLhQunSxgAnaXSuzg==', 'url': 'https://ct.googleapis.com/logs/xenon2023/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2019-12-17T18:38:01Z'}}, 'temporal_interval': {'start_inclusive': '2023-01-01T00:00:00Z', 'end_exclusive': '2024-01-01T00:00:00Z'}}, {'description': "Google 'Aviator' log", 'log_id': 'aPaY+B9kgr46jO65KB1M/HFRXWeT1ETRCmesu09P+8Q=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE1/TMabLkDpCjiupacAlP7xNi0I1JYP8bQFAHDG1xhtolSY1l4QgNRzRrvSe8liE+NPWHdjGxfx3JhTsN9x8/6Q==', 'url': 'https://ct.googleapis.com/aviator/', 'mmd': 86400, 'state': {'readonly': {'timestamp': '2016-11-30T13:24:18Z', 'final_tree_head': {'sha256_root_hash': 'LcGcZRsm+LGYmrlyC5LXhV1T6OD8iH5dNlb0sEJl9bA=', 'tree_size': 46466472}}}}, {'description': "Google 'Icarus' log", 'log_id': 'KTxRllTIOWW6qlD8WAfUt2+/WHopctykwwz05UVH9Hg=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAETtK8v7MICve56qTHHDhhBOuV4IlUaESxZryCfk9QbG9co/CqPvTsgPDbCpp6oFtyAHwlDhnvr7JijXRD9Cb2FA==', 'url': 'https://ct.googleapis.com/icarus/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2017-03-06T19:35:01Z'}}}, {'description': "Google 'Pilot' log", 'log_id': 'pLkJkLQYWBSHuxOizGdwCjw1mAT5G9+443fNDsgN3BA=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEfahLEimAoz2t01p3uMziiLOl/fHTDM0YDOhBRuiBARsV4UvxG2LdNgoIGLrtCzWE0J5APC2em4JlvR8EEEFMoA==', 'url': 'https://ct.googleapis.com/pilot/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2014-09-02T20:41:44Z'}}}, {'description': "Google 'Rocketeer' log", 'log_id': '7ku9t3XOYLrhQmkfq+GeZqMPfl+wctiDAMR7iXqo/cs=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEIFsYyDzBi7MxCAC/oJBXK7dHjG+1aLCOkHjpoHPqTyghLpzA9BYbqvnV16mAw04vUjyYASVGJCUoI3ctBcJAeg==', 'url': 'https://ct.googleapis.com/rocketeer/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2015-08-04T19:00:05Z'}}}, {'description': "Google 'Skydiver' log", 'log_id': 'u9nfvB+KcbWTlCOXqpJ7RzhXlQqrUugakJZkNo4e0YU=', 'key': 'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEEmyGDvYXsRJsNyXSrYc9DjHsIa2xzb4UR7ZxVoV6mrc9iZB7xjI6+NrOiwH+P/xxkRmOFG6Jel20q37hTh58rA==', 'url': 'https://ct.googleapis.com/skydiver/', 'mmd': 86400, 'state': {'usable': {'timestamp': '2017-03-06T19:35:01Z'}}}]}]
```

如果我们获取的是JSON数据，我们就使用响应对象的json()方法。对于txt、html、xml和其他文件格式，我们可以使用文本。

## 创建包

我们根据一些标准将大量的文件组织在不同的文件夹和子文件夹中，这样我们就可以很容易地找到和管理它们。如你所知，一个模块可以包含多个对象，如类、函数等。一个包可以包含一个或多个相关模块。一个包实际上是一个包含一个或多个模块文件的文件夹。让我们创建一个名为mypackage的包，使用以下步骤。

代码：

```python
# coding: utf-8

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return (a - b)

def multiple(a, b):
    return (a * b)

def division(a, b):
    return (a / b)

def remainder(a, b):
    return (a % b)

def power(a, b):
    return a ** b
```

代码：

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :greet.py
@说明    :
@时间    :2021/09/22 11:39:52
@作者    :liangcheng
@版本    :1.0
'''

def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to xxx'
```

结构目录如下：

![image-20210922114040034](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210922114040034.png)



让我们开始导入自定义的包并使用。

代码：

```python
from mypackage import arithmetics
print(arithmetics.add_numbers(1,2,3,4)) # 10
print(arithmetics.subtract(5,3)) # 2
print(arithmetics.multiple(5,3)) # 15
print(arithmetics.division(5,3)) # 1.6666666666666667
print(arithmetics.remainder(5,3))  # 2
print(arithmetics.power(5,3))  # 2

from mypackage import greet
print(greet.greet_person('liang', 'cheng')) # liang cheng, welcome to xxx
```

## 关于包的更多信息

- 数据库

  - SQLAlchemy或者SQLObject - 面向对象访问多个不同的数据库系统

    - ```
      pip install SQLAlchemy
      ```

- Web Development

  - Django - 高级网络框架

    - ```
      pip install django
      ```

  - Flask - 基于Werkzeug、Jinja 2的Python微型框架（它有BSD授权

    - ```
      pip install flask
      ```

- HTML Parser

  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML/XML解析器是为快速周转项目（如屏幕刮擦）设计的，将接受不良标记。

    - ```
      pip install beautifulsoup4
      ```

  - PyQuery - 用Python实现jQuery；显然比BeautifulSoup快。

- XML Processing

  - ElementTree - Element类型是一个简单而灵活的容器对象，被设计用来在内存中存储分层的数据结构，比如简化的XML信息集。

- GUI

  - PyQT - 跨平台的QT框架
  - Tklnter - 传统的Python用户界面工具包

- Data Analysis, Data Science and Machine learning

  - Numpy - Numpy(numeric python)被称为Python中最流行的机器学习库之一。
  - Pandas - 是一个数据分析、数据科学和机器学习的Python库，提供高层次的数据结构和各种各样的分析工具。
  - SciPy - SciPy是一个面向应用开发者和工程师的机器学习库。SciPy库包含优化、线性代数、整合、图像处理和统计等模块。
  - Scikit-Learn - 它是NumPy和SciPy。它被认为是处理复杂数据的最佳库之一。
  - TensorFlow - 是一个由谷歌建立的机器学习库
  - Keras - 被认为是Python中最酷的机器学习库之一。它为表达神经网络提供了一种更简单的机制。Keras还提供了一些最好的工具，用于编译模型、处理数据集、图形的可视化，以及更多。

- Network

  - requests - 是一个包，我们可以用它来向服务器发送请求（GET, POST, DELETE, PUT）。

    - ```
      pip install requests
      ```











