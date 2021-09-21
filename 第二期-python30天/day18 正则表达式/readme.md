# day18 Regular Expressions

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210918165827303.png)

---

正则表达式或RegEx是一个特殊的文本字符串，有助于在数据中寻找模式。RegEx可以用来检查某种模式是否存在于不同的数据类型中。要在Python中使用RegEx，首先我们应该导入RegEx模块，它被称为re。

## re模块

导入该模块，可以用来检测或寻找模式。

语法：

```python
import re
```

### re模块中的方法

为了找到一个模式，我们使用不同的re字符集，允许在一个字符串中搜索匹配。

- re.match()：只在字符串的第一行开始处搜索，如果找到，返回匹配的对象，否则返回None。
- re.search()：如果在字符串的任何地方有一个匹配对象，包括多行字符串，则返回一个匹配对象。
- re.findall()：返回一个包含所有匹配结果的列表。
- re.split：接收一个字符串，在匹配点处进行拆分，并返回一个列表。
- re.sub()：替换一个字符串中的一个或多个匹配项

> match

语法：

```python
re.match(substring, string, re.I)
# substring是需要寻找匹配的字符串，string是原文本，re.I是忽略大小写。
```

代码：

```python
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
```

从上面的例子中可以看到，要查找的子串为I love to tech，只有当该文本以该文本（I love to tech）开始时，匹配函数才能返回一个对象。

代码：

```python
txt = 'I love to teach python and javascript'

match = re.match('I like to teach', txt, re.I)

print(match) # None
```

上述代码查询的字符串为I like to teach，与I love to teach不符合，所以返回的是None。

> search

语法：

```python
re.search(substring, string, re.I)
```

代码：

```python
import re

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
```

正如你所看到的，search比match好得多，因为它可以在整个文本中寻找模式。search返回一个匹配对象，其中包括找到的第一个匹配对象，否则它返回无。一个更好的re函数是findall。这个函数在整个字符串中检查模式，并以列表形式返回所有的匹配对象。

> findall

findall()以列表的形式返回所有的匹配结果

代码：

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matchs = re.findall('language', txt, re.I)
print(matchs) # ['language', 'language']
```

如你所见，language在字符串中出现了2此，所以返回了一个包含两个字符的列表。

代码：

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('python', txt, re.I)
print(matches) # ['Python', 'python']
```

因为使用了re.I，所以匹配的内容不包括大小写，

代码：

```python
matches = re.findall('Python|python', txt)
print(matches)

matches = re.findall('[Pp]ython', txt)
print(matches
```

> 替换子串

代码：

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'javascript', txt, re.I)
print(match_replaced)

match_replaced = re.sub('[Pp]ython', 'javascript', txt, re.I)
print(match_replaced)
```

代码：

```python
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

### 使用RegEx分割文本

代码：

```python
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt))

['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## 编写正则表达式模式

代码：

```python
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
```

- `[]`：一组字符
  - `[a-c]`:等于a或b或c
  - `[a-z]`:等于从a到z的任何一个字母
  - `[A-Z]`:等于从A到Z的任何一个字母
  - `[0-3]`:等于0或1或2或3
  - `[0-9]`:等于0到9
  - `[A-Za-z0-9]`:任意单个字符a到z, A到Z或0到9
- `\`:用于转义特殊字符
  - \d:匹配包含数字的字符串（从0-9的数字）。
  - \D:匹配不含数字的字符串
- `.`:除换行符外的任何字符(\n)
- ^:以...开始
  - `r'^substring'`，例如r'^love'，以love开头的字符。
  - `r'[abc]'`:，不以a,b,c开头的任意字符
- `$`:以...结束
  - `r'substring$'`:例如r'love$'，以love结尾的字符
- `*`:0次或多次
  - `r'[a]*`:可有可无，也可以多次出现。
- `+`:1次或多次
  - `r'[a]+`:至少一次或更多
- `?`:0次或1次
  - `r'[a]?`:0次或1次出现
- `{3}`:刚好三个字符
- `{3}`:至少三个字符
- `{3,8}`:3至8个字符
- `|`:或
  - `r'apple|banana'`：苹果或香蕉
- `()`:捕获和分组

![Regular Expression cheat sheet](https://raw.githubusercontent.com/olist213/olistimg/master/upic/regex.png)

让我们用例子来说明上述的元字符

### 方括号

让我们使用方括号来包含小写和大写

代码：

```python
regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'apple']
```

如果我们想寻找香蕉，我们把模式写成如下。

代码：

```python
regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches) # ['Apple', 'banana', 'apple', 'banana'] 
```

使用方括号和或运算符，设法提取Apple、apple、banana、Banana。

### 正则表达式中的转义字符

代码：

```python
regex_pattern = r'\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']
```

### 一个或更多(+)

代码：

```python
regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2019', '8', '2021']
```

代码：

```python
regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['an', 'an', 'an', 'a ', 'ar']
```

### 0次或多次(*)

零次或多次。该模式可能不出现，也可能出现很多次。

代码：

```python
regex_pattern = r'[a].*'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']
```

### 0次或者一次(?)

零次或一次。该模式可能不出现，也可能出现一次。

代码：

```python
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'
matches = re.findall(regex_pattern, txt)
print(matches) # ['e-mail', 'email', 'Email', 'E-mail']
```

### 正则表达式中的量词

我们可以使用大括号来指定我们要寻找的文本中的子串的长度。让我们想象一下，我们对一个长度为4个字符的子串感兴趣。

代码：

```python
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches) # ['2019', '2021']

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6', '2019', '8', '2021']
```

### cart ^

- 以...开始

代码：

```python
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'
matches = re.findall(regex_pattern, txt)
print(matches) # ['This']
```

- negation(非，相反)

代码：

```python
regex_pattern = r'[^A-Za-z ]+'
matches = re.findall(regex_pattern, txt)
print(matches) # ['6,', '2019', '8,', '2021']
```

# 练习：day 18

