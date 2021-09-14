# Conditionals

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210913203033208.png)

---

条件表达式

默认情况下，python脚本中的语句都是从上到下依次执行，可以通过两种方式改变执行的顺序流程：

- 条件执行：如果某个表达式为真，将执行一个或多个语句块。
- 重复语句：只要某个表达式为真，一个或多个语句块就会被重复执行。

![img](https://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg)

## if条件

if用于检查条件是否为真，如果为真，则执行里面的代码块。

![img](https://raw.githubusercontent.com/olist213/olistimg/master/upic/python-if.webp)

语法：

```python
if condition:
		运行的代码
```

代码：

```python
a = 3
if a > 0:
    print('A is a positive number')
```

正如你在上面的例子中看到的，3>0，条件为真，块代码被执行，但是，如果条件为假，我们将看不到结果。为了查看假条件的结果，我们应该查看另一个块代码，这个条件表达式是else。

## if else

如果条件为真，将执行第一个代码块，否则，执行else里面的内容。

语法：

```python
if condition:
		条件为真运行的代码
else:
		条件为假运行的代码
```

代码：

```python
## if...else...

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

如果判断的条件超过两个呢？那么就需要使用到`elif`。

语法：

```python
if condition:
		运行的代码
elif condition:
		运行的代码
else:
		运行的代码
```

代码：

```python
a = 3
if a < 0:
    print('A is a negative number')
elif a > 0:
    print('A is a positive number')
else:
    print('A is zero'
```

## short hand

语法：

```python
code if condition else code
```

代码：

```python
a = 3
print('A is a positive') if a > 0 else print('A is a negative') # A is a positive
```

## 嵌套条件

语法：

```python
if condition:
		code 
		if condition:
				code
```

代码：

```python
a = 0
if a > 0:
    if a % 0 == 0:
        print('A is  a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```



我们可以通过使用逻辑运算符和来避免编写嵌套条件。

## if条件表达式和and逻辑运算符

语法：

```python
if condition and condition:
		code
```

代码：

```python
a = 0
if a > 0 and a % 0 == 0:
    print('A is  a positive and even integer')
    print('A is a positive number')
elif a > 0 and a % 2 != 0:
    print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

## if 和 or 逻辑运算符

语句：

```python
if codition or codition
		code
```

代码：

```python
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access Granted!')
else:
    print('Access Denied')
```

# 练习

## level 1

