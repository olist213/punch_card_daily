# strings

文本是一种字符串数据类型，任何单引号、双引号或三引号下的数据都是字符串，有不同的字符串方法和内置函数来处理字符串。

要检查一个字符串的长度，使用len()方法。

## 创建字符串

```python
#coding: utf-8

#创建字符串
letter = 'P'
print(letter)
print(len(letter))

greeting = 'Hello World'
print(greeting)
print(len(greeting))

sentence = "this is a test"
print(sentence)

# 创建多行字符串
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

```

## 连接字符串

可以将字符串连接在一起，合并或连接字符串被称为连接。

```python
first_name = 'liang'
last_name = 'cheng'
space = ' '
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))
```

## 字符串转义

在python和其他编程语言中，后面跟着一个字符就是转义字符。

常见的转义字符：

- `\n`:换行
- `\t`:tab（8个字符）
- `\\`:斜线
- `\'`:单引号（'）
- `\"`:双引号（"）





## 字符串格式化

`%`操作符用于格式化一组包含在"元组"（一个固定大小的列表）中的变量，以及一个格式化的字符串，其中包含正常的文本和“参数指定起”，特殊符号包括"%s","%d","%f","%.number of digitsf"。

- %s：sting
- %d：整数
- %f：浮点数
- "%.number of digitsf"：固定精度的浮点数



## 新的格式化字符串(str.format)

说明：在python3的语法中可用。

代码:

```python
first_namem = 'liang'
last_name = 'cheng'
language = 'python'
format_sting = 'i am {} {}. i study {}'.format(first_name,last_name,language)
print(format_sting)

# num运算
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # 保留小数点后两位
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output 
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.00
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64

# string and num
radius = 10
pi = 3.14
area = pi * radius ** 2
format_sting = '半径为 {} 圆的面积为：{:.2f}'.format(radius, area)
print(format_sting)
```

- F-strings(python3.6+)

代码：

```python
#f-sting , 报语法错误
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

- Python字符串作为字符序列

python字符串也是序列，叫字符序列，和lists和tuples一样的访问方式。

> 解开字符串的包装

代码：

```python
# unpacking characters
language = 'python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

- 通过索引访问字符串的内容

> 第一个字符的下标所有为0，字符串的最后一个字符的下标索引为字符长度减1。

![String index](https://raw.githubusercontent.com/olist213/olistimg/master/upic/string_index.png)

代码：

```python
# strings by index
language = 'python'
first_letter = language[0]
print(first_letter) # p
second_letter = language[1]
print(second_letter) #y

last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

> 如果想从一个字符串的右边开始索引，那么可以使用负数索引，-1是最后一个索引。

代码：

```python
last_letter =  language[-1] # n
second_letter = language[-2] # o 
print(last_letter,second_letter)
```

- 切割python字符串

在python中，可以将字符串切割成子字符串。

代码：

```python
# 切割字符串
language = 'python'
first_three = language[0:3] # pyt
print(first_three)

last_three = language[3:6]
print(last_three) #hon

last_three = language[-3:]
print(last_three) #hon

last_three = language[3:]
print(last_three) #hon
```

- 反转字符串

代码：

```python
# 反转字符串
greeting = 'hello, world'
print(greeting[::-1]) # dlrow ,olleh
```

- 切片时跳过字符

代码：

```python
# 切割时跳过字符
## 通过向切片方法传递步骤参数，可以在切片时跳过字符。

language = 'python'
pto = language[0:6:2]
print(pto) #pto
```

## 字符串函数

有许多字符串方法，允许我们对字符串进行格式化。

- Capitalize()：将字符串的第一个字符转换成大写字母。

代码：

```python
challenge = 'thirty days of python'
print(challenge.capitalize()) # Thirty days of python
```

- Count()：返回字串在字符串中出现的次数，count(substring, start=.., end=..)，start是用于计数的起始索引，end用于计算的最后索引。

代码：

```python
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y',7,14)) #1
print(challenge.count('th')) #2
```

- Endswith()：检查一个字符串是否是以执行的字符结尾。

代码：

```python
#endswith
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False
```

- expandtabs()：用空格替换制表符，默认制表符的大小为8，可以设置制表符的大小。

代码：

```python
# expandtabs()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) # thirty  days    of      pytho
print(challenge.expandtabs(10)) # thirty    days      of        python
```

- find()：返回查找的子串第一次出现的索引位置，如果没有找到返回-1。

代码：

```python
# find
challenge = 'thirty days of python'
print(challenge.find('on')) # 19
print(challenge.find('th')) # 0
```

- rfind()：返回查找的子串最后出现索引的位置，如果没有找到返回-1。

```python
# rfind
challenge = 'thirty days of python'
print(challenge.rfind('y')) # 16
print(challenge.rfind('th')) # 17
```

- format()：将字符串格式为更漂亮的输出。

代码：

```python
#format
first_name = 'liang'
last_name= 'cheng'
age = 230
job = 'teacher'
country = 'Findlan'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name,last_name,age,job,country)
print(sentence)
```

- index()：返回子字符串的最低索引，附加参数指示开始和结束索引（默认为0和字符串长度-1）。如果未找到子字符串，则会引发 valueError。

```python
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7
print(challenge.index(sub_string, 9)) # ValueError
print(challenge.index('th')) # 0
print(challenge.index('o')) # 12
```

- rindex()：返回子串的最高索引，附加参数表示起始和结束索引（默认为0和字符串长度-1）。

  ```python
  # rindex
  challenge = 'thirty days of python'
  sub_string = 'da'
  print(challenge.rindex(sub_string)) # 7
  # print(challenge.rindex(sub_string, 9)) # ValueError
  print(challenge.rindex('th')) # 17
  print(challenge.rindex('o')) # 19
  ```

- isalnum()：检查字母或者数字



- isalpha()：检查是否所有字符串元素都是字母字符。



- isdecimal()：检查是否所有字符串元素都是数字。



- isdigit()：检查一个字符串中的所有字符是否是数字（0-9和其他一些数字的unicode字符）。



- isnumeric()：检查字符串中的所有字符是否都是数字或数字相关的（就像isdigit()，只接受更多的符号，比如 ½）。



- isidentifier()：检查一个有效的标识符——它检查一个字符串是否是一个有效的变量名。



- islower()：检查字符串中的所有字母字符是否都是小写



- isupper()：检查字符串中的所有字母字符是否都是大写



- join()：返回一个连接的字符串



- strip()：从字符串的开头和结尾删除所有给定的字符



- replace()：用给定的字符串替换子字符串



- split()：拆分字符串，使用给定的字符串或空格作为分隔符



- title()：返回一个开头字母大小写的字符串



- swapcase()：将所有大写字符转换为小写，将所有小写字符转换为大写字符



- startswith()：检查字符串是否以指定的字符串开头

















