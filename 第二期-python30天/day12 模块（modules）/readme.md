# day12 modules

![30DaysOfPython](https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/30DaysOfPython_banner3@2x.png)

---

## 什么是模块？

模块是一个包含一组代码或一组函数的文件，可以被包含在一个应用程序里面，一个模块可以是一个包含单个变量的文件、一个函数或大型的代码库。

## 创建模块

为了创建一个模块，我们把代码写在一个Python脚本中，并把它保存为一个.py文件。在你的项目文件夹中创建一个名为mymodule.py的文件。让我们在这个文件中写一些代码。

代码：

```python
# mymodule.py文件
def generate_full_name(firstname, lastname):
  	return firstname + ' ' + lastname
```

在你的项目目录下建立main.py文件并导入mymodule.py文件。

## 导入模块

如果要导入文件的话，使用import关键字和文件名就可以了。

代码：

```python
# main.py文件
import module
print(mymodule.generate_full_name('liang', 'cheng'))
```

## 从模块导入函数

我们可以在一个文件中包含多个函数，并且可以以不同的方式导入所有函数。

代码：

```python
from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name('liang','cheng'))
print(sum_two_nums(1,9))

mass = 10
weight = mass * gravity
print(weight)
print(person['first_name'])
```

代码：

```python
# mymodule.py
def generate_full_name(firstname, lastname):
  	return firstname + ' ' + lastname


def sum_two_nums(num_one, num_two):
    sum = num_one + num_two
    return sum

# def weight_of_object(mass, gravity = 9.81):
#     weight = str(mass * gravity) + ' N'
#     return weight
gravity = 10


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
```

## 从模块中导入函数并重命名

在导入过程中，我们可以重命名模块的名称。

代码：

```python
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

print(fullname('liang', 'cheng'))
print(total(1, 9))
mass = 10
weight = mass * g
print(weight)
print(p)
print(p['first_name'])
```

# 导入内置模块

像其他编程语言一样，也可以通过使用关键字 import 导入文件/函数来导入模块。让导入大部分时间使用的公共模块。一些常见的内置模块：math、datetime、os、sys、random、statistics、collections、json、re。

## os 模块

使用Python的`OS`模块可以自动执行许多操作系统的任务。Python中的OS模块提供了创建、改变当前工作目录和删除一个目录）、获取其内容、改变和识别当前目录的功能。

代码：

```python
import os

# 创建目录
os.mkdir('directory_name')

# 改变当前所在目录的位置
os.chdir('/Users/grayash/macpentest/githubm/punch_card_daily/第二期-python30天/directory_name')

# 获取当前工作目录的路径
print(os.getcwd())

# 删除目录
# os.rmdir('directory_name')
```

## sys模块

sys模块提供了用于操作Python运行环境不同部分的函数和变量。函数sys.argv返回一个传给 Python 脚本的命令行参数列表。这个列表中索引为0的项目总是脚本的名称，索引为1的项目是从命令行传递的参数。

代码：

```python
import sys

print('welcome {}. enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))

# input:python3 main.py liangcheng hhhhh
# output:welcome liangcheng. enjoy hhhhh challenge!
```

## 一些有用的sys命令

代码：

```python
# 退出sys
sys.exit()

# 为了知道最大的整数变量
sys.maxsize

# 环境变量
sys.path()

# python的版本
sys.version()
```

# 统计模块

统计模块提供数据的数字统计功能，可以使用一些统计函数，如：mean,median,mode,stdev等。

代码：

```python
from statistics import *
ages = [20,20,4,24,25,22,26,20,23,22,26]
print(mean(ages)) # 21.09090909090909
print(median(ages)) # 22
print(mode(ages)) # 20
print(stdev(ages)) # 6.106628291529549
```

## math模块

包含许多数学运算和常数的模块。

代码：

```python
import math
print(math.pi) # 3.141592653589793
print(math.sqrt(2)) # 1.4142135623730951
print(math.pow(2, 3)) # 8.0
print(math.floor(9.81)) # 9
print(math.ceil(9.81)) # 10
print(math.log10(100)) # 2.0
```

现在，我们已经导入了数学模块，它包含了很多可以帮助我们进行数学计算的函数。要检查该模块有哪些功能，我们可以使用help(math)，或者dir(math)。这将显示该模块中的可用函数。如果我们只想从模块中导入一个特定的函数，我们可以按以下方式导入。

代码：

```python
from math import pi
print(pi)
```

也可以一次导入多个函数

代码：

```python
from math import pi, sqrt, pow, floor, ceil, log10
print(math.pi) # 3.141592653589793
print(math.sqrt(2)) # 1.4142135623730951
print(math.pow(2, 3)) # 8.0
print(math.floor(9.81)) # 9
print(math.ceil(9.81)) # 10
print(math.log10(100)) # 2.0
```

但如果我们想导入数学模块中的所有函数，我们可以使用`*`。

代码：

```python
from math import *
print(math.pi) # 3.141592653589793
print(math.sqrt(2)) # 1.4142135623730951
print(math.pow(2, 3)) # 8.0
print(math.floor(9.81)) # 9
print(math.ceil(9.81)) # 10
print(math.log10(100)) # 2.0
```

当我们导入时，我们也可以重命名该函数的名称。

代码：

```python
from math import pi as PI
print(PI)
```

## 字符串模块

字符串模块是一个有用的模块，有很多用途。下面的例子显示了字符串模块的一些用途。

代码：

```python
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

## random模块

现在你对导入模块已经很熟悉了。让我们再做一次导入，以便非常熟悉它。让我们导入随机模块，它可以给我们提供一个0到0.9999之间的随机数....。随机模块有很多函数，但在本节中我们将只使用随机和randint。

代码：

```python
from random import random, randint
print(random()) # 0.830143363811853
print(randint(5,10)) # 5
```

# 练习

## level 1

1、编写一个函数，生成一个六位数/字符的随机用户ID

代码：

```python
from random import *
import string
def random_user_id():
    lst = sample('abcdefghijklmnopqrstuvwxyz0123456789', 6)
    str = "".join(lst)
    return str

print(random_user_id())
```

2、修改之前的任务。声明一个名为user_id_gen_by_user的函数。它不接受任何参数，但它使用input()接受两个输入。其中一个输入是字符数，第二个输入是应该被生成的ID的数量。

代码：

```python
from random import *
import string

def user_id_gen_by_user():
    num_str = int(input("pls input you number string:"))
    num_id = int(input("pls input you id number:"))

    for num in range(num_id):
        lst = sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',num_str)
        str = "".join(lst)
        print(str)

print(user_id_gen_by_user())

## output
## pls input you number string:5
## pls input you id number:5
## i3Pba
## BDLae
## WwgL9
## tJ5Ue
## s5x8M

# pls input you number string:16
# pls input you id number:5
# oQukdLByRaZjTwVN
# 2AFHqj3iry0ebMak
# sBkwShq09IpuOQ3F
# Hkxmth7eno4F2ZC0
# cVFGpbULZdTq28t3
```

3、编写一个名为rgb_color_gen的函数。它将生成rgb颜色（3个值，每个值从0到255）。

代码：

```python
def rgb_color_gen():
    num1 = randint(0,255)
    num2 = randint(0,255)
    num3 = randint(0,255)
    print('rgb({},{},{})'.format(num1,num2,num3)) # rgb(175,221,174)

print(rgb_color_gen())
```

## level 2

