# 函数（function）

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210915160032065.png)

---

到目前为止，已经用了许多python的内置函数，本节重点讨论自定义函数。

## 定义函数

函数时可重复使用的代码块，或旨在执行某项任务的编程语句，要定义或声明函数，python提供了def关键字。仅在函数被调用时函数内部的代码才会被执行。

## 声明并调用函数

当创建一个函数时，称之为声明一个函数，当开始使用时，称之为调用函数，在声明函数时可以带参数，也可以不带参数。

语法：

```python
# 声明函数
def function_name():
  	codes
    codes

# 调用函数
function_name()
```

## 不带参数的函数

可以在没有参数的情况下，声明函数。

代码：

```python
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
```

## 函数返回值 - 第一部分

函数可以有返回值，如果函数没有返回语句，则函数的值为none，改写上述代码，让其返回值。

代码：

```python
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
```

## 带参数的函数

在一个函数中，可以传递不同的数据类型（数字、字符串、布尔值、列表、元组、字典、集合）作为函数的参数。

- 单个参数

语法：

```python
def function_name(parameter):
  	codes
    codes
    
print(function_name(argument))
```

代码：

```python
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
```

- 两个参数

语法：

```python
def function_name(para1, para2):
  	codes
    codes
    
print(function_name(arg1, arg2))
```

代码：

```python
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
```

## 用键和值传递参数

语法：

```python
def function_name(para1, para2):
  	codes
    codes
    
print(function_name(para1 = 'john', para2 = 'doe'))
```

代码：

```python
def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(print_fullname(first_name='liang', last_name='cheng'))

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(num1=2, num2=3))
```

## 函数的返回值 - 第二部分

如果不使用函数的返回值，那么返回的默认为None，要使用函数的返回值，就使用关键字return，后跟需要返回的变量，可以从一个函数中返回任何类型的数据。

- 返回一个字符串

代码：

```python
def print_name(firstname):
    return firstname

print(print_name('liang'))

def print_fullname(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(print_fullname(first_name='liang', last_name='cheng'))
```

- 返回数字

代码：

```python
def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum

print('sum of two numbers: ', sum_two_numbers(1, 2))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1992))
```

- 返回布尔值

代码：

```python
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True
    return False

print(is_even(10)) # True
print(is_even(11)) # False
```

- 返回列表

代码：

```python
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

print(find_even_numbers(10)) # [0, 2, 4, 6, 8, 10]
```

## 带默认参数的函数

语法：

```python
def function_name(param = value):
  		codes
    	codes
      
function_name()
function_name(arg)
```

代码：

```python
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
```

> 存在默认参数的函数，默认参数需要放到参数最后。

## 任意数量的参数

如果不知道传递给函数的参数的数量，可以通过在参数名前添加*号来创建一个可以接受任何参数的函数。

语法：

```python
def function_name(*args):
  	codes
    codes
    
function_name(param1, param2, param3,...)
```

代码：

```python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    
    return total

print(sum_all_nums(2,3,5)) # 10
```

## 函数中的默认参数和任意数量的参数

代码：

```python
def generate_groups(team, * args):
    print(team)
    for i in args:
        print(i)

print(generate_groups('Team-a', 'ha', 'za', 'ca'))
```

## 函数作为另一个函数的参数

代码：

```python
def square_number(n):
    return n * n

def do_something(f,x):
    return f(x)

print(do_something(square_number,3)) # 9
```

# 练习

## level 1















