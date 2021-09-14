# loop(循环)

![30DaysOfPython](https://github.com/Asabeneh/30-Days-Of-Python/raw/master/images/30DaysOfPython_banner3@2x.png)

---

- while循环
- for循环

## while循环

使用保留字while来创建一个while循环，直到满足给定的条件，当条件为假时，循环后的代码行将继续执行。

语法：

```python
while condition:
		code goes here
```

代码：

```python
count = 0

while count < 5:
    print(count)
    count = count + 1
```

在上面的代码中，当count的值为5时，条件变为假，也就是循环停止的时候，如果在条件不为真的情况下运行代码，可以使用else。

语法：

```python
while condition:
		code goes here
else:
		code goes here
```

代码：

```python
# while...else...
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

当count为5时，终止循环，执行else语句，结果将5打印出来。

## break和continue - 部分1

- break：当想退出或停止循环时，使用break

语法：

```python
while condition:
		code goes here
		if another_condition:
				break
```

代码：

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

当count为3时，就停止打印，跳出循环。

- continue：通过continue语句，我们可以跳过当前的迭代，继续进行下一个迭代。

语法：

```python
while condition:
		code goes here
		if another_condition:
				continue
```

代码：

```python
# continue
count = 0
while count < 5:
    if count == 3:
        count = count +  1
        continue

    print(count)
    count = count + 1
```

## for循环

for循环用于迭代序列（即列表、元组、字典、集合、字符串）。

- for循环用于列表

语法：

```python
for iterator in lst:
		code goes here
```

代码：

```python
numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number
```

- for循环用于字符串

语法：

```python
for iterator in string:
		code goes here
```

代码：

```python
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
```

- for循环用于元组

语法：

```python
for iterator in tpl:
		code goes here
```

代码：

```python
tpl = (0,1,2,3,4,5)
for number in tpl:
    print(number
```

- for循环用于字典

语法：

```python
for iterator in dict:
		code goes here
```

代码：

```python
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

# ('first_name', 'Asabeneh')
# ('last_name', 'Yetayeh')
# ('skills', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'])
# ('country', 'Finland')
# ('age', 250)
# ('address', {'street': 'Space street', 'zipcode': '02210'})
# ('is_marred', True)
```

- 循环用于set集合

语法：

```python
for iterator in st:
		code goes here
```

代码：

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

## break和continue - 部分2

break:当我们想在循环之前停止循环时，我们使用 break

语法：

```python
for iterator in sequence:
  	code goes here
    
    if condition:
      	break
```

代码：

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

    if number == 3:
        break
```

continue:当我们想在循环的迭代中跳过一些步骤时，我们就会使用continue。

语法：

```python
for iterator in sequence:
  	code goes here
    
    if condition:
      	continue
```

代码：

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

    if number == 3:
        continue

    print('Next number should be ', number + 1) if number != 5 else print('loop end')
print('outside the loop')

# 0
# Next number should be  1
# 1
# Next number should be  2
# 2
# Next number should be  3
# 3
# 4
# Next number should be  5
# 5
# loop end
# outside the loop
```

## range函数

range函数用于数字列表，range(start, end, stop)接受三个参数，start，end，stop，默认情况下，从0开始，增量为1，range序列至少需要一个参数（end）。

代码：

```python
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = list(range(1,11))
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]

st = set(range(0,11,2))
print(st) # set([0, 2, 4, 6, 8, 10])
```

语法：

```python
for iterator in range(start, end, step)
```

代码：

```python
for number in range(11):
		print(number)
```

## 嵌套for循环

语法：

```python
for x in y:
		for t in x:
				print(t)
```

代码：

```python
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# output
# JavaScript
# React
# Node
# MongoDB
# Python
```

## for else

如果我们想在循环结束时执行一些消息，我们使用`else`。

语法：

```python
for iterator in range(start, end, step):
		do something
else:
		print('The loop ended')
```

代码：

```python
for number in range(11):
    print(number)
else:
    print('The loop stops at:', number) # ('The loop stops at:', 10)
```

## pass

在Python中，当语句是必需的（在分号之后），但我们不喜欢在那里执行任何代码，我们可以写pass这个词来避免错误。同时，我们也可以把它作为一个占位符，有需要时再写代码。

代码：

```python
for number in range(11):
		pass
```

# 练习

## 练习 leve1

1、使用 for 循环迭代 0 到 10，使用 while 循环执行相同的操作。

```python
## for

for number in range(11):
    print(number)

## while
number = 0
while number <= 10:
    print(number)
    number = number + 1
```

2、使用for循环遍历10到0，使用while循环做同样的事情。

代码：

```python
### for
for number in range(10, 0, -1):
    print(number)

### while
number = 10
while number <= 10:
    print('while:',number)
    number = number -1

    if number < 0:
        break
```

3、写一个循环，对print()进行7次调用，因此我们在输出端得到以下三角形。

```python
  #
  ##
  ###
  ####
  #####
  ######
  #######
```

代码：

```python
for i in range(7):
    if i == 1:
        print("#")
    if i == 2:
        print("##")
    if i == 3:
        print("###")
    if i == 4:
        print("####")
    if i == 5:
        print("#####")
    if i == 6:
        print("######")
    if i == 7:
        print("#######")
```

4、使用嵌套循环建立下面的内容：

```python
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
```

代码：

```python
for x in range(0, 9):
    for y in range(0, 9):
        print("# ", end="")
    print()
```

5、打印如下内容：

```python
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
```

代码：

```python
for x in range(0,11):
    for y in range(0,11):
        if x != y:
            continue
        print(x,'x',y,'=',x*y)
```

6、使用for循环遍历列表中的['Python', 'Numpy', 'Pandas', 'Django', 'Flask']并打印出项目。

代码：

```python
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for s in lst:
    print(s)
```

7、使用for循环从0到100进行迭代，只打印偶数。

代码：

```python
for i in range(0,100):
    if i % 2 == 0:
        print(i)
```

8、使用 for 循环从 0 到 100 迭代，只打印奇数

代码：

```python
for i in range(0,100):
    if i % 2 != 0:
        print(i)
```

## 练习 level2

1、使用for循环，从0到100进行迭代，并打印所有数字的总和。

代码：

```python
sum = 0
for i in range(0,101):
    sum = sum + i
print(sum)
```

2、使用for循环从0到100进行迭代，并打印所有偶数和所有奇数的总和。

代码：

```python
evens_sum = 0
odds_sum = 0

for i in range(0,101):
    if i % 2 == 0:
        evens_sum = evens_sum + i
    
    if i % 2 != 0:
        odds_sum = odds_sum + i

print(evens_sum) # 2550
print(odds_sum) # 2500
```



















