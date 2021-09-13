# 元组（tuples）

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210911125421369.png)

---

元组是有序且不可修改的不同数据类型的集合，元组使用()来表示，一旦创建了元组，就不能改变它的值，不能在元组中使用add、insert、remove方法，因为他们是不可修改的，与列表不同，元组的方法比较少。与元组有关的方法如下：

- tuple()：创建一个空元组。
- count()：计算元组中指定元素的数量。
- index()：在元组中查找指定项的索引。
  - operator:：连接两个或多个元组冰创建一个新元组。

## 创建元组

- 创建空元组。

语法：

```python
empty_tuple = ()
empty_tuple = tuple()
```

- 初始化值

语法：

```
tpl = ('item1', 'item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
```

## 元组长度

使用len()方法。

语法：

```
tpl = ('item1', 'item2', 'item3')

len(tpl)
```

## 访问元组中的元素

同样的，和列表一样，使用正索引和反向索引访问元组中的元素。

![Accessing tuple items](https://raw.githubusercontent.com/olist213/olistimg/master/upic/tuples_index.png)

语法：

```python
tpl = ('item1', 'item2', 'item3')

first_item = tpl[0]
second_item = tpl[1]
```

代码：

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruits = fruits[0]
second_fruits = fruits[1]
last_index = len(fruits) - 1
last_fruits = fruits[last_index]

print(first_fruits)
print(second_fruits)
print(last_fruits
```

- 反向索引

反向索引从最右边开始，第一个为-1，从右往左，如下图：

![Tuple Negative indexing](https://raw.githubusercontent.com/olist213/olistimg/master/upic/tuple_negative_indexing-20210913141440904.png)

语法：

```python
tpl = ('item1', 'item2', 'item3')

first_item = tpl[-2]
second_item = tpl[-3]
```

代码：

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruits = fruits[-4]
second_fruits = fruits[-3]
last_fruits = fruits[-1]

print(first_fruits)
print(second_fruits)
print(last_fruits
```

## 元组切片

可以指定索引范围（开始-结束）来切割出一个子元组，返回一个新元组。

- 正向索引

代码：

```python
## slicing tuples

tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]
all_items = tpl[0:]
middle_two_items = tpl[1:3]

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]
```

- 反向索引

```python
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]
print(all_items) # ('item1', 'item2', 'item3', 'item4')
print(middle_two_items) # ('item2', 'item3')


fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]
```

## 将元组转成列表

因为元组是不可变的，如果需要修改元组，那么就需要先转换成列表，再进行修改。直接使用list()方法就可以。

语法：

```python
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
```

代码：

```python
# 将元组转成列表
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits) # ['apple', 'orange', 'mango', 'lemon'
fruits = tuple(fruits)
print(fruits) # ('apple', 'orange', 'mango', 'lemon')
```

## 检查元组中的元素

可以使用in关键词检查元组中是否存在某个元素，返回一个布尔值。

语法：

```python
tpl = ('item1', 'item2', 'item3', 'item4')
'item1' in tpl # True
```

代码：

```python

# in 

fruits = ('banana', 'orange', 'mango', 'lemon')
print('apple' in fruits) # False
print('orange' in fruits) # True

```

## 将两个或多个元组连接起来

使用+号操作符。

语法：

```python
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')

tpl3 = tpl1 + tpl2
```

代码：

```python
# +
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion')
```

## 删除元组

不允许删除一个元组中的单个项目，但可以使用del来删除元组本身。

语法：

```python
tpl = ('item1', 'item2', 'item3', 'item4')
del tpl
```

代码：

```python
# del
tpl = ('item1', 'item2', 'item3', 'item4')
del tpl
print(tpl) # NameError: name 'tpl' is not defined
```

# 练习 level 1

1、创建一个空元组

代码：

```python
tpl = ()
print(tpl) # ()
```

2、创建一个包含你姐妹和兄弟名字的元组（想象中的兄弟姐妹也可以）。

代码：

```python
tpl_brothers = ('zhangsan', 'lisi', 'wanglaowu')
tpl_sisters = ('luna', 'andi', 'john')
```

3、Join brothers and sisters tuples and assign it to siblings

代码：

```python
brothers_and_sisters = tpl_brothers + tpl_sisters
print(brothers_and_sisters)
wanglaowu_and_luna = brothers_and_sisters[2:4]
print(wanglaowu_and_luna)
```

4、你有几个兄弟姐妹？

```python
tpl_brothers = ('zhangsan', 'lisi', 'wanglaowu')
tpl_sisters = ('luna', 'andi', 'john')

brothers_and_sisters = tpl_brothers + tpl_sisters

print(len(brothers_and_sisters))
```

5、修改siblings tuple，加上你爸爸妈妈的名字，赋值给family_members。

代码：

```python
lst = list(brothers_and_sisters)
lst.append('liuwu')
lst.append('wanghui')
print(lst) # ['zhangsan', 'lisi', 'wanglaowu', 'luna', 'andi', 'john', 'liuwu', 'wanghui']
family_members = tuple(lst)
print(family_members) # ('zhangsan', 'lisi', 'wanglaowu', 'luna', 'andi', 'john', 'liuwu', 'wanghui')
```

# 练习 lever 2

...



