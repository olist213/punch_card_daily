![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x.png)

---

# lists(列表)

在python中，有四种集合数据类型，分别为：

- list：列表是一个集合，有序，可修改的，允许有重复的成员。
- tuple：元组，是一个有序，不可修改的集合，允许有重复的成员。
- set：是一个无序，无所有、不可修改的集合，可以添加新成员，不允许有重复的成员。
- dictionary：是一个无序的、可修改和可索引的集合，没有重复的成员。

列表是不同类型数据的集合，是有序的，可修改的，一个列表可以是空的，也可以有不同的数据类型。

## 如何创建列表（list）

> 可以通过两种方式创建

- 使用内置函数list

```python
lst = list()
```

```python
empty_list = list()
print(len(empty_list))
```

- 使用方括号

```python
lst = []
```

```python
empty_list = []
print(len(empty_list))
```

代码：

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

animal_products = ['milk', 'meat', 'butter', 'yoghurt']

web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']

countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits', fruits)
print('Number of fruits:', len(fruits))

print('vegetables', vegetables)
print('Number of vegetables:', len(vegetables))

print('animal_products', animal_products)
print('Number of animal_products:', len(animal_products))

print('web_techs', web_techs)
print('Number of web_techs:', len(web_techs))

print('countries', countries)
print('Number of countries:', len(countries))

# output
# ('Fruits', ['banana', 'orange', 'mango', 'lemon'])
# ('Number of fruits:', 4)
# ('vegetables', ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'])
# ('Number of vegetables:', 5)
# ('animal_products', ['milk', 'meat', 'butter', 'yoghurt'])
# ('Number of animal_products:', 4)
# ('web_techs', ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB'])
# ('Number of web_techs:', 7)
# ('countries', ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'])
# ('Number of countries:', 5)
```

- 列表的元素可以是不同的数据类型。

```python
lst = ['Asabeneh', 250, True, {'country':'Finland','city':'Helsinki'}]
```

## 使用正向索引获取元素

我们使用索引来访问列表中的每个元素，一个列表的索引从0开始，下面的图清楚的显示了索引的起始位置。

![List index](https://raw.githubusercontent.com/olist213/olistimg/master/upic/list_index.png)

代码：

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)

second_fruit = fruits[1]
print(second_fruit)

last_fruit = fruits[3]
print(last_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)
```

## 使用负数索引访问元素

负数索引意味着从末尾开始，-1指的是最后一项，-2指的是倒数第二项。

![List negative indexing](https://raw.githubusercontent.com/olist213/olistimg/master/upic/list_negative_indexing.png)

代码：

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit= fruits[-4]
print(first_fruit) # banana
first_fruit= fruits[-1]
print(first_fruit) # lemon
first_fruit= fruits[-2]
print(first_fruit) # mango
```

Unpacking list items

代码：

```python
# Unpacking List Items，只有在python3中可用。

lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# output
# item1
# item2
# item3
# ['item4', 'item5']

print("-------------------")

# # example
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, last_fruit, *rest = fruits 
print(first_fruit)
print(second_fruit)
print(last_fruit)
```

![image-20210910213214622](https://raw.githubusercontent.com/olist213/olistimg/master/upic/image-20210910213214622.png)

代码：

```python
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first) #1 
print(second) #2
print(third) #3
print(rest) # [4,5,6,7,8,9]
print(tenth) #10
```

## 从列表中切割元素

正向索引。我们可以通过指定start、end和step来指定一个正向索引的范围，返回值将是一个新的列表。(默认值为 start = 0, end = len(lst) - 1 (最后一项), step = 1)

代码：

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon= fruits[1:]
orange_and_lemon = fruits[::2]
print(all_fruits)
print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

# output
# ['banana', 'orange', 'mango', 'lemon']
# ['banana', 'orange', 'mango', 'lemon']
# ['orange', 'mango']
# ['orange', 'mango', 'lemon']
# ['banana', 'mango']
```



负数索引。我们可以通过指定开始、结束和增量来指定一个负数索引的范围，返回值将是一个新的列表。

代码：

```python
# 负数索引
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]
orange_and_mango = fruits[-3:-1]
orange_mango_lemon = fruits[-3:]
reverse_fruits = fruits[::-1]

print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(reverse_fruits)

# output
# ['banana', 'orange', 'mango', 'lemon']
# ['orange', 'mango']
# ['orange', 'mango', 'lemon']
# ['lemon', 'mango', 'orange', 'banana']
```

## 修改列表中的元素

列表中元素可以被修改，并且是有序的集合。

代码：

```python
# 修改列表

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits) # ['avocado', 'orange', 'mango', 'lemon']

fruits[1] = 'apple'
print(fruits) # ['avocado', 'apple', 'mango', 'lemon']

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits) # ['avocado', 'apple', 'mango', 'lime']
```

## 检查列表中的元素

检查某个元素是否在列表里面，使用`in`操作符。

代码：

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) #True

does_exist = 'lime' in fruits
print(does_exist) # False
```

## 往列表中追加元素

使用`appen()`方法。

代码：

```python
lst = list()
list.append(item)
```

代码：

```python
# 追加元素
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits) #['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
```

## 往列表里面插入元素

使用insert()方法。insert()方法需要两个参数一个是index索引，一个是需要插入的值。

语法：

```python
lst = ['item1', 'item2']
lst.insert(index, item)
```

代码：

```python
#  插入元素
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(3, 'apple')
print(fruits) # ['banana', 'orange', 'mango', 'apple', 'lemon']
```

## 从列表中移除元素

使用remove()方法。

语法：

```python
lst = ['item1','item2']
lst.remove(item1)
```

## 使用pop移除元素

pop()方法删除指定的索引，如果没有指定索引，那么默认删除最后一个元素

语法：

```python
lst = ['item1', 'item2']
lst.pop()
lst.pop(1)
```

代码：

```python
# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.pop()) # lemon
print(fruits) # ['banana', 'orange', 'mango']
print(fruits.pop(1)) # orange
print(fruits) # ['banana', 'mango']
```

## 使用del()删除元素

del()方法会删除指定的索引，也可以用来删除索引范围内的项目，同时还可以完全删除列表。

语法：

```python
lst = ['item1', 'item2']
del lst[index]
del lst
```

代码：

```python
# del
print("-----del-------")
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits) # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits) # ['orange', 'lemon']

del fruits[1:3]
print(fruits) # ['orange']

# del fruits
# print(fruits) # NameError: name 'fruits' is not defined
```

## 清除列表中的元素

clear()方法清空列表。

语法：

```python
lst = ['item1', 'item2']
lst.clear()
```

代码：

```python
# clear()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) # []
```

## 拷贝列表

我们可以通过以下方式将一个列表重新赋值给一个新的变量来复制它：list2 = list1。

现在，`list2`是`list1`的引用，我们对 list2 所做的任何修改也会修改原始的 list2。但在很多情况下，我们不喜欢修改原始数据，而希望有一个不同的副本。避免上述问题的方法之一是使用 copy() 。

语法：

```python
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

代码：

```python
# copy
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy) # ['banana', 'orange', 'mango', 'lemon']
```

## joining lists

在Python中，有几种方法可以将两个或多个列表连接起来。

> 使用+操作符

语法：

```python
list3 = list1 + list2
```

代码：

```python
# joining list
positive_numbers = [1,2,3,4,5]
zero = [0]
negative = [-5,-4,-3,-2,-1]
integers = negative + zero + positive_numbers 
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
```

- 使用 extend() 方法进行连接，extend() 方法允许在一个列表中追加列表。请看下面的例子。

语法：

```
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

代码：

```python
# extend
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print(num1) # [0, 1, 2, 3, 4, 5, 6]
```

## 统计元素在列表中的个数

语法：

```python
lst = ['item1', 'item2']
lst.count(item)
```

代码：

```python
# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) # 1

age = [22,45,22,34,21,22,35]
print(age.count(22)) # 3
```

## 查找元素的索引

index()方法返回列表中某个元素的索引。

语法：

```python
lst = ['item1', 'item2']
lst.index(item1)
```

代码：

```python
# index()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('banana')) # 0
age = [22,45,22,34,21,22,35]
print(age.index(22)) # 0
```

## 反向列表

列表反向排序

语法：

```
lst = ['item1', 'item2']
lst.reverse(item1)
```

代码：

```python
# reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
age = [22,45,22,34,21,22,35]
age.reverse()
print(age) # [35, 22, 21, 34, 22, 45, 22]
```

## 列表元素排序

要对列表进行排序，我们可以使用sort()方法或内置函数sorted() 。sort()方法将列表中的项目按升序重新排序，并修改原始列表。如果sort()方法的一个参数reverse等于true，它将以降序排列列表。

```python
# sort()

lst = ['item1', 'item2']
lst.sort() # 升序
lst.sort(reverse=True) # 降序
```

代码：

```python
# sort 排序
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) # ['banana', 'lemon', 'mango', 'orange']

fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

age = [22,45,22,34,21,22,35]
age.sort()
print(age) # [21, 22, 22, 22, 34, 35, 45]

age.sort(reverse=True)
print(age) # [45, 35, 34, 22, 22, 22, 21]
```

- sorted

返回有序的列表，而不需要修改原始列表 例子。

代码：

```python
## sorted
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits)) # ['banana', 'lemon', 'mango', 'orange']

# reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
```

# 练习

...