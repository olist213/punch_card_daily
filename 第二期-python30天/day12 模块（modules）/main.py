#coding: utf-8
# main.py文件

import mymodule
print(mymodule.generate_full_name('liang', 'cheng'))

from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name('liang','cheng'))
print(sum_two_nums(1,9))

mass = 10
weight = mass * gravity
print(weight)
print(person['first_name'])

# 在导入过程中，我们可以重命名模块的名称。

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

print(fullname('liang', 'cheng'))
print(total(1, 9))
mass = 10
weight = mass * g
print(weight)
print(p)
print(p['first_name'])

import os

# 创建目录
# os.mkdir('directory_name')

# 改变当前所在目录的位置
os.chdir('/Users/grayash/macpentest/githubm/punch_card_daily/第二期-python30天/directory_name')

# 获取当前工作目录的路径
print(os.getcwd())

# 删除目录
# os.rmdir('directory_name')

# sys

# import sys

# print('welcome {}. enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))

# python3 main.py liangcheng hhhhh
#welcome liangcheng. enjoy hhhhh challenge!

# 统计模块

from statistics import *
ages = [20,20,4,24,25,22,26,20,23,22,26]
print(mean(ages)) # 21.09090909090909
print(median(ages)) # 22
print(mode(ages)) # 20
print(stdev(ages)) # 6.106628291529549

import math
print(math.pi) # 3.141592653589793
print(math.sqrt(2)) # 1.4142135623730951
print(math.pow(2, 3)) # 8.0
print(math.floor(9.81)) # 9
print(math.ceil(9.81)) # 10
print(math.log10(100)) # 2.0

# string

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# random

from random import random, randint
print(random()) # 0.830143363811853
print(randint(5,10)) # 5

#level 1

# 编写一个函数，生成一个六位数/字符的随机用户ID
from random import *
import string
def random_user_id():
    lst = sample('abcdefghijklmnopqrstuvwxyz0123456789', 6)
    str = "".join(lst)
    return str

print(random_user_id())

# 2修改之前的任务。声明一个名为user_id_gen_by_user的函数。它不接受任何参数，但它使用input()接受两个输入。其中一个输入是字符数，第二个输入是应该被生成的ID的数量。

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
    
# pls input you number string:16
# pls input you id number:5
# oQukdLByRaZjTwVN
# 2AFHqj3iry0ebMak
# sBkwShq09IpuOQ3F
# Hkxmth7eno4F2ZC0
# cVFGpbULZdTq28t3

# 3、编写一个名为rgb_color_gen的函数。它将生成rgb颜色（3个值，每个值从0到255）。

def rgb_color_gen():
    num1 = randint(0,255)
    num2 = randint(0,255)
    num3 = randint(0,255)
    print('rgb({},{},{})'.format(num1,num2,num3)) # rgb(175,221,174)

print(rgb_color_gen())


