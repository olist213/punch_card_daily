# day17 Exception Handling

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210918152056488.png)

---

python使用try和except来优雅的处理错误，bug的优雅处理是一种简单的编程习惯，程序在检测到错误时并以一种可控的方式去处理这个错误。通常情况下，程序会向终端或日志汇中输出错误的描述信息，使得应用程序也更加稳健，导致异常可能是一个错误的输入、一个错误的文件名、无法找到某个文件、一个故障的iO设备。

我们在上一节已经介绍了不同的Python错误类型。如果我们在程序中使用 try 和 except，那么在这些代码块中就不会产生错误。

![Try and Except](https://raw.githubusercontent.com/olist213/olistimg/master/upic/try_except.png)

语法：

```python
try:
  	如果一切正常，此处进行代码编写
except:
  	如果出现问题，此处的代码会运行
```

代码：

```python
try:
    print(10 + '5')
except:
    print('发生了一些错误')
```

上面的这个例子中，第二个操作数是字符串，数字+字符串将报错，得转成同一类型的才能相加，如果按上面的代码执行，就将执行except里面的代码。

代码：

```python
try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('发生了一些错误')

# Enter your name:liangcheng
# Year you were born:1999
# 发生了一些错误
```

上面的代码中，except块将会执行，然后上面的错误信息比较笼统，无法知道具体的错误信息。

在下面的例子中，它将处理错误，也会告诉我们错误种类。

代码：

```python
try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print("类型错误导致")
except ValueError:
    print("属性值有问题")
except ZeroDivisionError:
    print("zero division error occured")

# Enter your name:liang
# Year you were born:1999
# 类型错误导致
```

由上面的代码可以知道，引发错误的原因是类型错误（TypeError）。现在，让我们添加一个额外的区块。

代码：

```python
try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print("类型错误导致")
except ValueError:
    print("属性值有问题")
except ZeroDivisionError:
    print("zero division error occured")
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

# Enter your name:liangcheng
# Year you were born:1998
# 类型错误导致
# I alway run.
```

将上面的代码缩短：

代码：

```python
try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
```

## Python中的参数打包和解压

使用两个运算符

- *for tuples
- **for dictionaries

让我们以下面这个例子为例。它只接受参数，但我们有列表。我们可以把列表拆开，然后把它变成参数。

## 打包（解压）

### 解压列表

代码：

```python
def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]

# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
print(sum_of_five_nums(lst))
```

当我们运行这段代码时，会产生一个错误，因为这个函数以数字（而不是列表）作为参数。让我们对列表进行解包/解构。

代码：

```python
def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst)) # 15
```

除了上述的解包操作，还可以在有起点和终点的范围的内置函数中使用解包。

代码：

```python
numbers = range(2, 7)
print(list(numbers)) # [2, 3, 4, 5, 6]

args = [2, 7]
numbers = range(*args)
print(list(numbers)) # [2, 3, 4, 5, 6]
```

列表或元组也可以这样解包：

代码：

```python
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest) # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(one, middle, last) # 1 [2, 3, 4, 5, 6] 7
```

### 解压字典

代码：

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. he is {age} year old.'

dct = {'name':'liang', 'country':'china', 'city':'beijing', 'age':28}
print(unpacking_person_info(**dct)) # liang lives in china, beijing. he is 28 year old.
```

## 打包

有时我们永远不知道需要向一个Python函数传递多少个参数。我们可以使用打包方法来允许我们的函数接受无限数量或任意数量的参数。

### 打包列表

代码：

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1,2,3)) # 6
print(sum_all(1,2,3,4,5,6,7)) # 28
```

### 打包字典

代码：

```python
def packing_person_info(**kwargs):

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

# {'name': 'liang', 'country': 'china', 'city': 'shanghai', 'age': 18}
print(packing_person_info(name='liang',country='china',city='shanghai',age=18))
```

## Spreading in Python

代码：

```python
lst_one = [1,2,3]
lst_two = [4,5,6]
lst = [0, *lst_one, *lst_two]
print(lst) # [0, 1, 2, 3, 4, 5, 6]

country_lst_one = ['Finland', 'sweden', 'norway']
country_lst_two= ['denmak', 'icelang', 'china']
nordic_country = [*country_lst_one, * country_lst_two]
# ['Finland', 'sweden', 'norway', 'denmak', 'icelang', 'china']
print(nordic_country)
```

## 枚举

如果我们对列表的索引感兴趣，可以使用enumerate内置函数来获取列表中每个项目的索引。

代码：

```python
for index, item in enumerate([20, 30, 40]):
    print(index, item)

# 0 20
# 1 30
# 2 40
```

代码：

```python
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'the country {i} has been found at index {index}')

```

## zip

有的时候，我们向在循环时（如for循环）合并列表，就可以使用zip函数。

代码：

```python
# zip
fruits = ['banana', 'orange', 'mango', 'lemon','lime']
vegetables = ['tomato','potato', 'cabbage', 'onion','carrot']
fruits_and_vegetables = []
for f,v in zip(fruits, vegetables):
    fruits_and_vegetables.append({'fruit':f, 'veg':v})

# [{'fruit': 'banana', 'veg': 'tomato'}, {'fruit': 'orange', 'veg': 'potato'}, {'fruit': 'mango', 'veg': 'cabbage'}, {'fruit': 'lemon', 'veg': 'onion'}, {'fruit': 'lime', 'veg': 'carrot'}]
print(fruits_and_vegetables)
