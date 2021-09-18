# coding: utf-8

from typing import Type


try:
    print(10 + '5')
except:
    print('发生了一些错误')


try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('发生了一些错误')

# Enter your name:liangcheng
# Year you were born:1999
# 发生了一些错误

try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print("类型错误导致")
except ValueError:
    print("属性值有问题")
except ZeroDivisionError:
    print("zero division error occured")

# Enter your name:liang
# Year you were born:1999
# 类型错误导致

try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print("类型错误导致")
except ValueError:
    print("属性值有问题")
except ZeroDivisionError:
    print("zero division error occured")
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

# Enter your name:liangcheng
# Year you were born:1998
# 类型错误导致
# I alway run.

try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)