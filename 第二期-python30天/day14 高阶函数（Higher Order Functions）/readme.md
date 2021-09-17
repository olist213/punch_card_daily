# day14 Higher Order Functions

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210917135548888.png)

---

在python中，函数有很多的操作，如下：

- 一个函数可以接受一个或多个函数作为参数
- 一个函数可以作为另一个函数的结果被返回
- 函数可被修改
- 可以将一个函数分配给一个变量

这一章节，将讨论：

- 处理作为参数的函数
- 将函数作为另一个函数的返回值返回
- 使用python的封包（closures）和装饰器（decorators）

## 函数作为参数传递

首先定义两个函数，然后另一个函数将函数和值传递给一个函数：

代码：

```python
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst): # 函数作为参数
    summation = f(lst) # 调用
    return summation

result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result) # 15
```

## 将函数作为另一个函数的返回值返回

代码：

```python
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
```

从上面的例子你可以看到，高阶函数根据传递的参数返回不同的函数

## python闭包

python允许一个嵌套的函数访问包围其函数的外部内容，这就是所谓的闭包，在 Python 中，闭包是通过将一个函数嵌套在另一个封装的函数中，然后返回内部函数而创建的。

代码：

```python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    
    return add

closure_result = add_ten()
print(closure_result(5)) # 15
print(closure_result(10)) # 20
```

## python装饰器

装饰器是Python中的一种设计模式，它允许用户在不修改现有对象结构的情况下向其添加新的功能。装饰器通常在你想装饰的函数的定义之前被调用。

代码：

```python
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
```

## 将多个装饰器应用到一个函数上

代码：

```python
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
```

## 接收装饰器中的参数

大多数时候，我们需要我们的函数接受参数，所以我们可能需要定义一个接受参数的装饰器。

代码：

```python
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(firstname, lastname, country):
    print("I am {} {}. I love to tech.".format(firstname, lastname, country))

print_full_name('liang', 'cheng', 'china')
```

# 内置高阶函数

在这一部分中，我们涉及的一些内置高阶函数是map()、filter和reduce。lambda函数可以作为参数传递，lambda函数的最佳使用案例是在map、filter和reduce等函数中。

## python - map函数

map()函数是一个内置函数，它接收一个函数和可迭代的参数。

语法：

```python
map(function, iterable)
```

代码1：

```python
numbers = [1,2,3,4,5]

def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]

numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25]
```

代码2：

```python
numbers_str = ['1','2','3','4','5']
numbers_int = map(int, numbers_str)
print(list(numbers_int)) # [1, 2, 3, 4, 5]
```

代码3：

```python

names = ['aaaa','bbbb','cccc','dddd']

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased)) # ['AAAA', 'BBBB', 'CCCC', 'DDDD']

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased)) # ['AAAA', 'BBBB', 'CCCC', 'DDDD']
```

实际上map所做的是对一个列表进行迭代。例如，它把名字改为大写，并返回一个新的列表。

## python - filter函数

filter()函数调用指定的函数，为指定的迭代器（列表）的每个项目返回布尔值。它过滤满足过滤条件的项目。

语法：

```python
filter(function, iterable)
```

代码：

```python
numbers = [1,2,3,4,5] # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers)) # [2, 4]
```

代码：

```python
numbers = [1,2,3,4,5] # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers)) # [1, 3, 5]
```

代码：

```python
names = ['aaaaaaaaaaa','bb', 'ccccc','dddddd']

def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names)) # ['aaaaaaaaaaa']
```

## python - reduce函数

reduce()函数是在functools模块中定义的，我们应该从这个模块中导入它。像map和filter一样，它需要两个参数，一个函数和一个可迭代数据。然而，它并不返回另一个可迭代数据，而是返回一个单一的值。

代码：

```python
import functools

numbers_str = ['1', '2', '3', '4', '5']
def add_two_nums(x, y):
    return int(x) + int(y)

total = functools.reduce(add_two_nums, numbers_str)
print(total) # 15