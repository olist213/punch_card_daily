# 第二章 知识点

# 0x01 简述

第二章主要的内容是讲关于内置函数的，内置函数都是全局可用的，不需要导入相关的模块就可以直接使用，一些常见的内置函数如下：
print()，len()，type()，int()，float()，str()，input()，list()，dict()，min()，max()，sum()，sorted()，open()，file()，help()和dir()等函数。

python的其他内置函数可以查看下这张表。https://docs.python.org/3.9/library/functions.html

![image-20210903152139086](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210903152139086.png)

---

# 0x02 函数理解与代码实战：

先从常见的函数开始：

## print

说明：print是打印的意思，旨在打印字符及字符串。

代码：

```python
print("hello,world") 
# 输出：hello,world
```



## len

说明：len返回对象的长度，参数可以是序列（例如：字符串、字节、元组、列表或者范围）或者集合（例如字典，set或frozen set）。

代码：

```python
#len
#string 字符串 输出5
print(len("hello"))

#输出0
a = ""
print(len(a))

#输出3,tuple
b = ("a","b","c")
print(len(b)) 

# list 输出5
c = [1,2,3,4,5]
print(len(c))

# range 输出9
d = range(1,10)
print(len(d))

# dict 字典 输出1
e = {"name":"liangcheng"}
print(len(e))

# set 输出5 
f = {1,2,3,4,"laohu"}
print(len(f))
```



## type

说明：type用来检查数据（对象）的类型。

代码：

```python
# coding: utf-8

# check data types

#int
print(type(10))

# float
print(type(3.14))

#complex
print(type(1 + 3j))

#str
print(type("my name is liangcheng"))

#list
print(type([1,2,3]))

#dict
print(type({'name':'liangcheng'}))

#set
print(type({8.7,9.0,23.89}))

#tuple
print(type((8.7,9.0,23.89)))

```

## str

说明：将一个对象转换成字符串。可以将数字转成字符串格式。

代码：

```python
# str
## 输出<type 'str'>
print(type(str(10)))
```



## int

说明：将一个对象转换成数字型。

代码：

```python
# int
##  输出：<type 'int'> 
print(type(int('123')))
```



## float

说明：浮点型

代码：

```python
#float
## <type 'float'> 
print(type(float(10))
```



## input

说明：将标准输入的内容进行输出，从输入中读取一行，将其转换为字符串。

代码：

```python
#coding: utf-8

'''
python3 输入input.py
please input you name:123
123
'''

print(input('please input you name:')
```

## min

说明：获取最小值

代码：

```python
# output 1
print(min(1,20,12,45))

# output 3
print(min([4,10,3,90])
```

## max

说明：获取最大值

代码：

```python
# output 45
print(max(1,20,12,45))

# output 90
print(max([4,10,3,90]))
```



## sum

说明：求和，求和只对list（列表）有用，如果直接输入数字，会报错。

代码：

```
# print(sum(1,20,12,45))
print(sum([4,10,3,90]))
```



# 0x03 变量

说明：变量是存储数据的内存地址、变量命名不允许以数字、特殊字符、连字符开头，变量可以是简短的名字，但建议使用有描述性的名字，容易区分。

- 变量命名规则：
  - 变量名必须以字母或下划线字符开头
  - 变量名不能以数字开头
  - 变量名只能包含数字字符和下划线（A-z，0-9，_）
  - 变量名区分大小写

有效的变量名：

```python
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

无效的变量名：

```python
first-name
first@name
first$name
num-1
1num
```

python的标准命名格式：蛇形大小写（snake_case），对于包含多个单词的变量，在每个单词后面使用下划线字符，如（first_name,last_name,engine_rotation_speed）。

当我们把某种数据类型分配给一个变量，这叫做变量声明，用=号进行赋值运算，赋值意味着将数据存储在变量中。

```python
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

代码：

```python
# coding: utf-8

first_name = 'liang'
last_name = 'cheng'
country = 'china'
age = 120
is_married = False
skills = ['pentest','ctf','redtem']
person_info = {
    'firstname':'liang',
    'lastname':'cheng',
    'country':'china',
    'aget':12
}

print('first_name',first_name)
print('last_name',last_name)
print('country',country)
print('age',age)
print('is_married',is_married)
print('skills',skills)
print('person_info',person_info)

# 输出
# ('first_name', 'liang')
# ('last_name', 'cheng')
# ('country', 'china')
# ('age', 120)
# ('is_married', False)
# ('skills', ['pentest', 'ctf', 'redtem'])
# 	('person_info', {'lastname': 'cheng', 'aget': 12, 'firstname': 'liang', 'country': 'china'}
```

> 定义多行变量

多行变量可以直接写在一行。

代码：

```python
# 多行变量

first_name, last_name, country, age, is_married = 'liang', 'cheng', 'china', 123, False

print(first_name, last_name, country, age, is_married)

print('first_name',first_name)
print('last_name',last_name)
print('country',country)
print('age',age)
print('is_married',is_married)
```

> 通过input函数获取用户输入的内容作为变量。

```python
# input 变量
first_name = input('pls input first name:')
age = input('pls input age:')

print(first_name)
print(age)

# 输出
# pls input first name:liang
# pls input age:234
# liang
# 234
```



# 0x04 数据类型

check data type:

代码：

```python
# coding: utf-8

first_name = 'liang' # str
last_name = 'cheng' # str
country = 'china' # str
city = 'jiangxi' # str
age = 25 # int

#打印数据类型

#str
print(type(first_name))

# int
print(type(age))

# float
print(type(3.1415))

# complex
print(type(1 + 1j))

# bool
print(type(True))

# list 
print(type([1,2,3,4]))

# dict
print(type({'name':'liangcheng','age':29}))

# tuple
print(type((1,2,3,4)))

# set
print(type(zip([1,2],[3,4])))
```

> 类型转换：将一种数据类型转换为另一种数据类型，当进行算数运算是，字符串数字首先需要转换为int或float，否则就返回一个错误。如果将一个数字和一个字符串连接起来，需要将数字转换为字符串。

代码：

```python
#coding: utf-8

# int to float

num_int = 10
print('num_int',num_int) # 10
num_float = float(num_int) 
print(num_float) # 10.0

# float to int

num_float1 = 9.18
print(int(num_float1))

# int to float
num_int = 10
print('num_int',num_int) # 10
num_str = str(num_int)
print(num_str)

# str to int or float

num_str = '10'
print('num_int',int(num_str))
print('num_int',float(num_str))

# str to list

string1 = 'hello,world'
print('str',string1)
string_list = list(string1)
print(string_list)
```

# 0x05 数字

1、整数（负数、0、正数）：-3、-2、-1、0、1、2、3...

2、浮点数（小数）：-3.5、-2.25、-1.0、0.0、1.1、2.2...

3、复数：1+j、2+4j、1-1j...



## 练习

### level 1

```python
#coding: utf-8

## 练习、level 1

### 2、Write a python comment saying 'Day 2: 30 Days of python programming'

print('Day 2:30 Days of python programming!')

### 3、Declare a first name variable and assign a value to it

first_name = "liang"
print(first_name)

### 4、Declare a last name variable and assign a value to it
last_name = "cheng"
print(last_name)

### 5、Declare a full name variable and assign a value to it


### 6、Declare a country variable and assign a value to it
country = "china"
print(country)

### 7、Declare a city variable and assign a value to it
city = 'beidai'
print(city)

### 8、Declare an age variable and assign a value to it
age = 123
print(age)

### 9、Declare a year variable and assign a value to it
year = 1992
print(year)

### 10、Declare a variable is_married and assign a value to it
is_married = False
print(is_married)

### 11、Declare a variable is_true and assign a value to it
is_true = True
print(is_true)

### 12、Declare a variable is_light_on and assign a value to it
is_light_on = "no"
print(is_light_on)

### 13、Declare multiple variable on one line

first_name, last_name, country, age = "liang", "cheng", "china", 120
print(first_name,last_name,country,age)

```



### 练习： level 2

```python
##Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

## Using the len() built-in function, find the length of your first name

my_name = "liangcheng"
print(len(my_name))

if len(first_name) > len(last_name):
    print("first name to long")
else:
    print(len(first_name))
    print(len(last_name))
    print("last name to long")

## Declare 5 as num_one and 4 as num_two
### Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4

total = num_one + num_two
print(total)

### Subtract num_two from num_one and assign the value to a variable diff 
diff = num_two - num_one
print(diff)

### Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

### Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

### Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

### Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

### Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

## The radius of a circle is 30 meters(一个圆的半径是30米)
### Calculate the area of a circle and assign the value to a variable name of area_of_circle(计算一个圆的面积，并将该值分配给一个名为 area_of_circle 的变量。)
### S=πr²

area_of_circle = 3.14 * (30 ** 2)
print(area_of_circle)

### Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle(计算一个圆的周长，并将该值赋给一个名为circum_of_circle的变量。)
circum_of_circle = 3.14 * 30 * 2
print(circum_of_circle)


### Take radius as user input and calculate the area.(将半径作为用户输入，并计算出面积。)

r = input("pls input r:")
print(3.14 * int(r) ** 2)

### Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names(使用内置的输入函数从用户那里获得名字、姓氏、国家和年龄，并将其值存储到相应的变量名中。)

first_name = input("pls input you first name:")
print(first_name)

last_name = input("pls input you last name:")
print(last_name)

country = input("pls input you country:")
print(country)

age = input("pls input you age:")
print(age)

### Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

'''
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
'''

```



# 0x06 扩展内置函数



## abs

说明：返回数字的绝对值。

代码：

```
num = -1
print(abs(num))
```

## all

说明：all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。

> 元素除了是 0、空、None、False 外都算 True。

语法：

> all(iterable)

参数：元素或者列表

代码：

```python
# all

a = [1,2,3,4]
print(all(a)) #true

b = ['a','b','','d']
print(all(b)) #true

c = [0,2,3,4]
print(all(c)) #false

d = (1,2,3,4)
print(all(d)) #true

e = ('a','b','','d')
print(all(e))#false

f = (0,1,2,3)
print(all(f)) # false
```

**注意：**空元组、空列表返回值为True

```
print(all([]))
print(all(()))
```

## any

说明：any()函数用来判断传入的参数是否全部为False，如果是，则返回False，否则返回True。

语法：

> any(iterable)

返回值：如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。

## bin

说明：返回一个整数或者长整数的二进制值。

语法：

> bin(x)

代码：

```python
num1 = 12
print(bin(num1)) # 0b1100
```



## bool

说明：将给定的参数转换为bool类型，如果没有参数，则返回False。

语法：

> bool(x)

代码：

```python
print(bool(0)) # False
print(bool(1)) #True
print(bool()) #False
```

## ~~bytearray~~



## ~~callable~~

说明：**callable()** 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。



## chr

说明：用一个范围在（256）内的整数作为参数，返回对应的字符串。

语法：

> chr(i)

参数i：

> 可以是10进制或者16进制的数字

代码：

```python
print(chr(0x30),chr(0x31),chr(0x61)) # ('0', '1', 'a')
print(chr(48),chr(49),chr(97)) # ('0', '1', 'a')
```

## ~~classmethod~~



## cmp

说明：cmp(x,y)用来比较2个对象，如果`x<y`，则返回`-1`，如果`x==y`，返回`0`，如果`x>y`,则返回`1`。

语法：

> cmp(x,y)



## ~~compile~~

说明：将一个字符串编译为字节代码。



## ~~complex~~~

说明：用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。

语法：

> complex([real[, imag]])

代码：

```python
print(complex(1,2)) #(1+2j)
```

## ~~delattr~~

说明：用于删除属性。



## dict

说明：用于创建一个字典

语法：

```python
class dict(**kwarg)
class dict(mapping,**kwarg)
class dict(iterable,**kwarg)
```

参数说明：

- **kwarg：关键字
- mapping：元素的容器
- iterable：可迭代对象

返回值：字典

代码：

```python
print(dict(a='a',b='b',c='c')) # {'a': 'a', 'c': 'c', 'b': 'b'}
print(dict(zip(['one','two','three'], [1,2,3]))) #{'three': 3, 'two': 2, 'one': 1}
print(dict([('one',1),('two',2),('three',3)])) #{'three': 3, 'two': 2, 'one': 1}
```

## dir

说明：不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。



## eval

说明：执行字符串表达式，并返回表达式的值。

语法：

> eval(expression)

代码：

```python
a = 7
print(eval('a * 3')) #21
```



## ~~enumerate~~



## ~~divmod~~

说明：python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。

语法：

> dived(a,b)

代码：

```python
print(divmod(7,2)) # (3,1)
print(divmod(8,2)) # (4,0)
```



## file

说明：创建一个file对象，别名open()。

代码：

```python
f = file('./1.txt')
print(f.read())
```



## execfile

说明：用来执行一个文件。

语法：

> execfile(filename)



## filter

说明：用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

语法：

> filter(function, iterable)

代码：

```python
def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd,[1,2,3,4,5,6,7,8,9,0])
print(newlist) # [1, 3, 5, 7, 9]
```



```python
# 过滤出1~100中平方根是整数的数
import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

newlist = filter(is_sqr, range(1, 101))
print(newlist) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## float

说明：用于将整数和字符串转换成浮点数。

语法：

> float([x])

参数：x：整数或字符串。



## format

说明：格式化字符串，str.format()，增强了字符串格式化的功能，用`{}`和`:`代替。

代码：

```python
print("{} {}".format("hello","world"))
print("{0} {1}".format("hello","world"))
print("{0} {1} {0}".format("hello","world"))

### output
# hello world
# hello world
# hello world hell

print("网站名:{name},url:{url}".format(name = "test",url = "http://www.test.com/"))

# 字典设置
dict1 = {"name":"test","url":"http://www.test.com/"}
print("网站名:{name},url:{url}".format(**dict1))

# 通过列表索引
my_lists = ["test","http://www.test.com/"]
print("网站名:{0[0]},url:{0[1]}".format(my_lists))
```



## ~~globals~~

说明：以字典类型返回当前位置的全部全局变量。



## getattr

说明：返回一个对象的属性值。

代码：

```python
class A(object):
    bar = 1

a = A()
print(a)
print(getattr(a,"bar"))
```

## ~~frozenset~~

说明：返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。



## ~~hasattr~~

说明：用于判断对象是否包含对应的属性。



## id

说明：返回对象的唯一标识符，标识符是一个整数。

语法：

> id([object])



## hex

说明：用于将10进制转换成16进制，以字符串形式表示。

语法：

> hex(x)

代码：

```python
#hex 
a = 123
print(hex(a)) #0x7b
```

## help

说明：用于查看函数或模块用途的详细说明。



## hash

说明：用于获取一个对象（字符串或数字）的哈希值。



## input

说明：接受一个标准输入数据，返回为 string 类型。

> 除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。

语法：

> raw_input([prompt])



## int

说明：将一个字符串或数字转换为整形。

语法：

> int(x, base=10)



## isinstance

说明：判断一个对象是否是一个已知的类型，类似 type()。

> isinstance和type的区别：type不会认为子类是一种父亲类型，不考虑继承关系，二isinstance会。



## ~~issubclass~~

说明：用于判断参数 class 是否是类型参数 classinfo 的子类。



## iter

说明：用来生成迭代器。

代码：

```python
lst = [1,2,3]
for i in iter(lst):
    print(i)
#output
#1
#2
#3
```



## len

说明：返回对象（字符、列表、元组）的长度或者项目个数。

语法：

> len(s)

代码：

```python
print(len("liangcheng")) # 6
print(len([1,2,3,4,5,6])) # 10
```

## list

说明：将元组转成列表。

语法：

> list(tup)

代码：

```python
aTuple = ("one","two","three")
print(list(aTuple)) # ['one', 'two', 'three'
```

## locals

说明：以字典类型返回当前位置的全部局部变量。

语法：

> locals()

代码：

```python
def zens(arg):
    z = 1
    print(locals())

zens(4) #{'z': 1, 'arg': 4}
```



## ~~long~~

说明：**Python3.x 版本已删除** **long()** **函数。**



## map

说明：根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

语法：

> map(function, iterable, ...)

```python
# python2

def square(x):
    return x**2

s = map(square, [1,2,3,4])
print(s) # [1, 4, 9, 16]

### 使用lambda匿名函数
print(map(lambda x: x**2, [1,2,3,4])) # [1, 4, 9, 16]

print(map(lambda x,y: x + y, [1,2,3,4],[5,6,7,8])) # [6, 8, 10, 12]

```

⚠️：

- 如果函数有多个参数, 但每个参数的序列元素数量不一样, 会根据最少元素的序列进行。
- map映射名字规范化实例。

```python
### 规范名字格式。
name_list = {'tony','wenDi','heLlo Kitty'}

def format_name(s):
    ss = s[0:1].upper() + s[1:].lower()
    return ss

print(list(map(format_name,name_list)))
```

- [filter](https://www.runoob.com/python/python-func-filter.html)是通过生成 True 和 False 组成的迭代器将可迭代对象中不符合条件的元素过滤掉；而 [map](https://www.runoob.com/python/python-func-map.html) 返回的则是 True 和 False 组成的迭代器。

```python
### filter 与 map 的区别

res = map(lambda x: x > 5, range(10))
print(list(res)) # [False, False, False, False, False, False, True, True, True, True]

res1 = filter(lambda x: x > 5, range(10))
print(res1) # [6, 7, 8, 9]
```

## max

说明：返回给定参数的最大值，参数可以是序列。

语法：

> max(x, y, z, ...)



## ~~memoryview~~

说明：返回给定参数的内存查看对象(memory view)。所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。



## min

说明：返回给定参数的最小值，参数可以为序列。



## next

说明：返回迭代器的下一个项目，要和生成迭代器的`iter`函数一起使用。

语法：

> next(utterable)

代码；

```python
it = iter([1,2,3,4,5])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
# output
# 1
# 2
# 3
# 4
# 5
```



## oct

说明：将一个整数转换成8进制字符串。















## 注意

1、在命名变量的时候，不能使用python自带的预留变量，如果变量名和预留的变量名一样，则会报错。













