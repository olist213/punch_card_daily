# day15 python type errors

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210917150423860.png)

---

当我们写代码时，经常会写些错别字或者一些其他常见的代码bug，如果代码运行失败，python的解释器会返回bug提示信息，其中包括了bug发生的位置以及bug的类型，有时也会给出可能的修复建议。

让我们逐一看看最常见的错误类型。

## 语法错误

代码：

```python
Python 3.9.5 (default, May  3 2021, 19:12:05) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
```

正如你所看到的，我们犯了一个语法错误，因为我们忘了用小括号把字符串括起来，Python 已经提示了解决方案。python3中print必须使用小括号括起来。

代码：

```python
print('hello world')
```

该错误是一个语法错误（SyntaxError），修复后，我们的代码顺利执行。

## 名称错误（NameError）

代码：

```python
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
```

从上面的信息中可以看到，age这个名字没有被定义。是的，我们确实没有定义age变量，但是我们试图把它打印出来，就好像我们已经声明了它。

代码：

```python
age = 25
print(age)
```

错误的类型是NameError。我们通过定义变量名称来调试这个错误。

## IndexError

> IndexError

代码：

```python
>>> number = [1,2,3,4,5]
>>> number[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

在上面的例子中，Python引发了一个 IndexError，因为列表只有从0到4的索引，所以它超出了范围。

## ModuleNotFoundError

> ModuleNotFoundError

代码：

```python
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
```

在上面的例子中，我在math中故意多加了一个s，导致引发了ModuleNotFoundError错误，让我们通过从math中删除多余的s来解决这个问题。

## 属性错误（AttributeError）

AttributeError

代码：

```python
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
```

正如你所看到的，这里又犯了一个错误! 我试图从数学模块中调用一个PI函数，而不是π。它引发了一个属性错误，这意味着这个函数不存在于这个模块中。让我们通过将PI改为pi来解决这个问题。

代码：

```python
math.pi
```

## keyerror

> KeyError

代码：

```python
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
```

正如你所看到的，在用于获取字典值的键中有一个错字，所以，这是一个键错误。

## TypeError

>  TypeError

代码：

```python
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

在上面的例子中，出现了一个TypeError错误，因为不能将数字和字符串相加，从而引发了TypeError错误。解决方法是需要将所有参数转成字符串或者整形数字。

## ImportError

> ImportError

代码：

数学模块中没有叫power的函数，它有一个不同的名字：pow。让我们来纠正一下。

```python
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (/opt/homebrew/Cellar/python@3.9/3.9.5/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/math.cpython-39-darwin.so)
>>> from math import pow
>>> pow(2,3)
8.0
```

> ValueError

代码：

```python
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
```

在这种情况下，我们不能将给定的字符串改为数字，因为其中有'a'字母。

> ZeroDivisionError

代码：

```python
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

我们不能用数字除以0。

我们已经介绍了一些python的错误类型，如果你想了解更多，请查阅python文档中关于python错误类型的内容。如果你善于阅读错误类型，那么你将能够快速修复你的错误，你也将成为一个更好的程序员。

## 练习

...