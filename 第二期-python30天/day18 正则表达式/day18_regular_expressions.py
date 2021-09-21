# coding: utf-8

## match

import re

txt = 'I love to teach python and javascript'

# 匹配并返回一个对象
match = re.match('I love to teach', txt, re.I)
print(match) # <re.Match object; span=(0, 15), match='I love to teach'>

# 我们可以使用span获得匹配的开始和结束位置的元组
span = match.span()
print(span) # (0, 15)

start, end = span
print(start, end) # 0 15

substring = txt[start:end]
print(substring) # I love to teach



txt = 'I love to teach python and javascript'

match = re.match('I like to teach', txt, re.I)

print(match) # None

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first', txt, re.I)
print(match) # <re.Match object; span=(100, 105), match='first'>

span = match.span()
print(span) # (100, 105)

start, end = span
print(start, end)

substring = txt[start:end] # 100 105
print(substring) # first

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matchs = re.findall('language', txt, re.I)
print(matchs) # ['language', 'language']

matches = re.findall('python', txt, re.I)
print(matches) # ['Python', 'python']

matches = re.findall('Python|python', txt)
print(matches)

matches = re.findall('[Pp]ython', txt)
print(matches)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'javascript', txt, re.I)
print(match_replaced)

match_replaced = re.sub('[Pp]ython', 'javascript', txt, re.I)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt))

['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']


# 编写正则表达式模式

import re

regex_pattern = r'apple'

txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches) # ['apple']

matches = re.findall(regex_pattern, txt, re.I)
print(matches) # ['Apple', 'apple']

regex_pattern = r'[A|a]pple'
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']

# 让我们使用方括号来包含小写和大写

regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']

# 如果我们想寻找香蕉，我们把模式写成如下。

regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'banana', 'apple', 'banana'] 

# 转义字符
regex_pattern = r'\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

# 一个或更多个
regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2019', '8', '2021']

# .
regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['an', 'an', 'an', 'a ', 'ar']

# *

regex_pattern = r'[a].*'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']


# ?

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'
matches = re.findall(regex_pattern, txt)
print(matches) # ['e-mail', 'email', 'Email', 'E-mail']

# 量词

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches) # ['2019', '2021']

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2019', '8', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches) # ['This']

regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6,', '2019', '8,', '2021']