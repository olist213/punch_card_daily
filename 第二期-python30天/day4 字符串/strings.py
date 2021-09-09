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

# 字符串连接

first_name = 'liang'
last_name = 'cheng'
space = ' '
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# 转义字符

print('I hope everyone is enjoying the python challage.\n Are you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash symbol (\\)')
print('this is a \"test\".')

#output
'''
I hope everyone is enjoying the python challage.
 Are you?
Days	Topics	Exercises
Day 1	3	5
Day 2	3	5
Day 3	3	5
Day 4	3	5
This is a backslash symbol (\)
this is a "test".
'''

# 格式化字符串
# 字符串
first_name = 'liang'
last_name = 'cheng'
language = 'python'
format_sting = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(format_sting)

#字符串和数字
radius = 10
pi = 3.14
area = pi * radius ** 2
format_sting = 'The area of circle with a radius %d is %.2f.' %(radius, pi)
print(format_sting)

python_libraries = ['Django', 'Flask', 'NunPy', 'Matplotlib', 'Pandas']
format_sting = 'the following are python libraries: %s' %(python_libraries)
print(format_sting)

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


#f-sting , 报语法错误
# a = 4
# b = 3
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')

# unpacking characters
language = 'python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# strings by index
language = 'python'
first_letter = language[0]
print(first_letter) # p
second_letter = language[1]
print(second_letter) #y

last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

print('-------------------')

last_letter =  language[-1] # n
second_letter = language[-2] # o 
print(last_letter,second_letter)

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

# 反转字符串
greeting = 'hello, world'
print(greeting[::-1]) # dlrow ,olleh

# 切割时跳过字符
## 通过向切片方法传递步骤参数，可以在切片时跳过字符。

language = 'python'
pto = language[0:6:2]
print(pto) #pto

# capitalize

challenge = 'thirty days of python'
print(challenge.capitalize()) # Thirty days of python

#count
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y',7,14)) #1
print(challenge.count('th')) #2

#endswith
challenge = 'thirty days of python'
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs()
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) # thirty  days    of      pytho
print(challenge.expandtabs(10)) # thirty    days      of        python

# find
challenge = 'thirty days of python'
print(challenge.find('on')) # 19
print(challenge.find('th')) # 0

# rfind
challenge = 'thirty days of python'
print(challenge.rfind('y')) # 16
print(challenge.rfind('th')) # 17

#format
first_name = 'liang'
last_name= 'cheng'
age = 230
job = 'teacher'
country = 'Findlan'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name,last_name,age,job,country)
print(sentence)

# index
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7
# print(challenge.index(sub_string, 9)) # ValueError
print(challenge.index('th')) # 0
print(challenge.index('o')) # 12

# rindex
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 7
# print(challenge.rindex(sub_string, 9)) # ValueError
print(challenge.rindex('th')) # 0
print(challenge.rindex('o')) # 12













