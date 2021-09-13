# 字典（Dictionaries）

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210913192939754.png)

---

字典是无序、可修改、成对（键:值）的数据类型集合。

## 创建字典

要创建字典，使用大括号{}或者dict()内置函数。

语法：

```python
empty_dict = {}

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct)
```

代码：

```python
person = {
    'first_name':'liang',
    'last_name':'cheng',
    'age':130,
    'country':'finland',
    'is_married':False,
    'skills':['php', 'python', 'bash', 'mysql'],
    'address':{
        'street':'space street',
        'zipcode':'02909'
    }
}
```

上述代码可以看到，字典可以包含多种数据类型，字符串、布尔值、列表、元素、集合和字典。

## 字典大小

检查"键:值"对的数量，使用len方法。

代码：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
print(len(person)) # 7
```

## 访问字典中的元素

可以通过引用键名来访问字典里的值。

语法：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dict['key1'])
print(dict['key4'])
```

代码：

```python
print(person['first_name']) # liang
print(person['country']) # finland
print(person['skills'][0]) # php
print(person['address']['street']) # space street
```

如果一个字典中所访问的键不存在，那么就会报错，为了避免这个错误，首先就必须检查需要访问的键是否存在，可以使用get方法，如果键不存在，则返回None。

``` python
print(person['city']) # none
```

## 向字典中添加元素

语法：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

代码：

```python
person = {
    'first_name':'liang',
    'last_name':'cheng',
    'age':130,
    'country':'finland',
    'is_married':False,
    'skills':['php', 'python', 'bash', 'mysql'],
    'address':{
        'street':'space street',
        'zipcode':'02909'
    }
}

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

## 修改字典中的元素

语法：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value1-1-1'
```

代码：

```python
person['first_name'] = 'qing'
person['age'] = 222
print(person) # {'first_name': 'qing', 'last_name': 'cheng', 'skills': ['php', 'python', 'bash', 'mysql'], 'country': 'finland', 'age': 222, 'address': {'street': 'space street', 'zipcode': '02909'}, 'is_married': False}
```

## 检查字典中的键

使用in操作符去检查键是否存在。

语法：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key1' in dct)
print('key5' in dct)
```



## 从字典中删除键和值对

- pop(key):删除具有指定键名的项。
- popitem():删除最后一项
- del():删除具有指定键名的项。

语法：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1')

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()

del dct['key2']
```

代码：

```python
print(person.pop('first_name')) # qing
print(person.popitem()) # ('last_name', 'cheng')
del person['is_married']
print(person) # {'skills': ['php', 'python', 'bash', 'mysql'], 'country': 'finland', 'age': 222, 'address': {'street': 'space street', 'zipcode': '02909'}
```

## 将字典转换成元组

用items()方法。

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # [('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1'), ('key4', 'value4')]
```

## 清空字典

使用clear()方法。

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.clear()
```

## 删除字典

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

## 拷贝字典

使用copy()方法复制字典。

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
```

## 获取字典的键作为列表

使用keys()方法。

语法：

```python
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_keys = dct.keys()
print(dct_keys) # ['key3', 'key2', 'key1', 'key4']
```

## 获取字典值作为列表

使用values()方法。

语法：

```python
# values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_values = dct.values()
print(dct_values) # ['value3', 'value2', 'value1', 'value4']
```

# 练习

