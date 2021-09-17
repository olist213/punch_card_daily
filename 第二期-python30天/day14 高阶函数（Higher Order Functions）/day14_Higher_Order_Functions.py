# coding: utf-8

from typing import no_type_check_decorator


def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst): # 函数作为参数
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result) # 15

# 将函数作为另一个函数的返回值返回

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3)) # 9

result = higher_order_function('cube')
print(result(3)) # 27

result = higher_order_function('absolute')
print(result(-3)) # 3

# python闭包

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    
    return add

closure_result = add_ten()
print(closure_result(5)) # 15
print(closure_result(10)) # 20

# python装饰器

## 正常函数
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g()) # WELCOME TO PYTHON

## 使用python装饰器完成上述案例

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting()) # WELCOME TO PYTHON

# 将多个装饰器应用到一个函数上

## 第一个装饰器
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

## 第二个装饰器

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    
    return wrapper

@split_string_decorator
@uppercase_decorator # 在这种情况下，使用装饰器的顺序很重要--.upper()函数对列表不起作用。
def greeting():
    return 'Welcome to Python'

print(greeting()) # ['WELCOME', 'TO', 'PYTHON']

# 大多数时候，我们需要我们的函数接受参数，所以我们可能需要定义一个接受参数的装饰器。

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(firstname, lastname, country):
    print("I am {} {}. I love to tech.".format(firstname, lastname, country))

print_full_name('liang', 'cheng', 'china')

# map function

numbers = [1,2,3,4,5]

def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]

numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]

# 2

numbers_str = ['1','2','3','4','5']
numbers_int = map(int, numbers_str)
print(list(numbers_int)) # [1, 2, 3, 4, 5]

# 3

names = ['aaaa','bbbb','cccc','dddd']

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased)) # ['AAAA', 'BBBB', 'CCCC', 'DDDD']

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased)) # ['AAAA', 'BBBB', 'CCCC', 'DDDD']

# filter

numbers = [1,2,3,4,5] # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers)) # [2, 4]

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers)) # [1, 3, 5]

names = ['aaaaaaaaaaa','bb', 'ccccc','dddddd']

def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names)) # ['aaaaaaaaaaa']

# reduce

import functools

numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total) # 15
