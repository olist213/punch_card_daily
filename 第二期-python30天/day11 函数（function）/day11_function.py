#coding: utf-8

## 无参数的函数

def generate_full_name():
    first_name = 'liang'
    last_name = 'cheng'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name()

def add_two_numbers():
    num_one = 1
    num_two = 2
    total = num_one + num_two
    print(total)

add_two_numbers()

## return value

def generate_full_name():
    first_name = 'liang'
    last_name = 'cheng'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def add_two_numbers():
    num_one = 1
    num_two = 2
    total = num_one + num_two
    return total

print(add_two_numbers())

## 单个参数的函数

def greetings(name):
    message = name + ', welcome to python for everyone'
    return message

print(greetings('liangcheng')) # liangcheng, welcome to python for everyone

def add_ten(num):
    ten = 10
    return num + ten

print(add_ten(10)) # 20

def square_number(x):
    return x ** x

print(square_number(10)) # 10000000000

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area

print(area_of_circle(5)) # 78.5

def sum_of_numbers(n):
    total = 10
    for i in range(n+1):
        total += i
    print(total)
    return total

print(sum_of_numbers(10)) # 65
print(sum_of_numbers(100)) # 5060

## 两个参数

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Full Name: ', generate_full_name('liang','cheng'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print('sum of two numbers: ', sum_two_numbers(1, 2))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1992))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N'
    return weight

print('Weight of an object in newtons: ', weight_of_object(100, 9.81))

## 键值传餐

def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(print_fullname(first_name='liang', last_name='cheng'))

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(num1=2, num2=3))

## 返回一个字符串

def print_name(firstname):
    return firstname

print(print_name('liang'))

def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(print_fullname(first_name='liang', last_name='cheng'))

## 返回数字

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print('sum of two numbers: ', sum_two_numbers(1, 2))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1992))

## 返回布尔值

def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False

print(is_even(10)) # True
print(is_even(11)) # False

## 返回列表

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(find_even_numbers(10)) # [0, 2, 4, 6, 8, 10]

## 默认参数

def greetings(name = 'peter'):
    message = name + ', welcome to python for everyone'
    return message

print(greetings())
print(greetings('liangcheng')) 

def generate_full_name(first_name = 'liang', last_name = 'cheng'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print('Full Name: ', generate_full_name())
print('Full Name: ', generate_full_name('liang','cheng'))

def weight_of_object(mass, gravity = 9.81):
    weight = str(mass * gravity) + ' N'
    return weight

print('Weight of an object in newtons: ', weight_of_object(100))
print('Weight of an object in newtons: ', weight_of_object(100, 1.62))

def calculate_age(birth_year, current_year = 2021):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(1992)) # 29

## 任意多个参数

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    
    return total

print(sum_all_nums(2,3,5)) # 10

## 函数中的默认参数和任意数量的参数

def generate_groups(team, * args):
    print(team)
    for i in args:
        print(i)

print(generate_groups('Team-a', 'ha', 'za', 'ca'))

# 函数作为另一个函数的参数

def square_number(n):
    return n * n

def do_something(f,x):
    return f(x)

print(do_something(square_number,3)) # 9

