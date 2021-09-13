# day7 set

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210913145308384.png)

---

set是元素的集合，set是无序和无索引的不同元素的集合，在python中，set用于存储唯一项，可以找到集合之间的并集、交集、差集、对称差集、子集、超集和不相交集。

## 创建集合

可以使用大括号`{}`来创建一个集合或者使用`set()`内置函数。

- 创建空白集合

语法：

```python
st = {}

st = set()
```

- 创建集合并初始化

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

## 得到集合的长度

使用`len()`方法。

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

## 访问集合中的元素

使用循环来进行访问。

## 检查集合中是否存在某元素

使用`in`关键字。

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
print('st集合中是否存在item3：', 'item3' in st) # True
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('banana' in fruits) # True
```

## 往集合里面添加元素

一旦创建了集合，就无法更改任何内容，但可以添加其他元素。

- 使用add()方法

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

代码：

```python
# add
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('apple')
print(fruits) # set(['orange', 'mango', 'lemon', 'banana', 'apple'])
```

- 使用update()方法添加过个元素，update()接受一个列表参数。

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
fruits.update(vegetables)
print(fruits) # set(['Tomato', 'lemon', 'Onion', 'Potato', 'mango', 'orange', 'Cabbage', 'banana'])
```

## 从set集合中删除某个元素

可以使用remove()方法从集合中删除一个元素，如果没有找到该元组，将引发错误，因此首先需要检查删除的元素是否村存在。

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item3')
```

pop()方法将随机删除一个元素，返回删除的元素。

代码：

```python
# remove , pop
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop()) # banana
print(fruits) # {'orange', 'lemon', 'mango'}
```

## 清空集合

使用clear()方法。

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

代码：

```python
# clear 
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.clear()) # None
```

## 删除集合

使用del()方法。

语法：

```python
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

## 将列表转换成集合

可以将list转换成set，也可以将set转换成list，当list转换成set的时候，会删除重复项。

语法：

```python
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)
```

代码：

```python
# list set 转换
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits = set(fruits)
print(fruits) # set(['orange', 'mango', 'lemon', 'banana'])
```

## 将集合连接起来

使用union()或者update()方法连接两个集合。

- union这个方法返回一个新的集合

语法：

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3) # set(['item8', 'item2', 'item3', 'item1', 'item6', 'item7', 'item4', 'item5'])
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
print(fruits.union(vegetables)) # set(['Tomato', 'lemon', 'Onion', 'Potato', 'mango', 'orange', 'Cabbage', 'banana'])
```

- update()，将一个集合插入给定的集合中。

语法：

```python
# update
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # set(['item8', 'item2', 'item3', 'item1', 'item6', 'item7', 'item4', 'item5'] 
print(st1)
```

代码：

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
fruits.update(vegetables)
print(fruits) # set(['Tomato', 'lemon', 'Onion', 'Potato', 'mango', 'orange', 'Cabbage', 'banana']
```

## 查找交叉项

交集返回两个集合中都有的元素。

语法：

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)
```

代码：

```python
# intersecion

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.intersection(even_numbers)) # set([0, 2, 4, 6, 8, 10]

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon)) # set(['o', 'n']
```

## 检查子集和超集

- subset（子集）：issubset()
- Super set（超集）：issuperset()

语法：

```python
# subset super set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}

print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True
```

代码：

```python
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.issubset(even_numbers))  # False
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.issubset(dragon)) # False
```

## 检查两组之间的差异

使用difference方法。

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st2.difference(st1)) # set([] 
print(st1.difference(st2)) # set(['item1', 'item4']) 
```

代码：

```python
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.difference(even_numbers))  # set([1, 3, 9, 5, 7] 
print(whole_numbers.difference(even_numbers)) # set([1, 3, 9, 5, 7])

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.difference(dragon)) # set(['y', 'h', 't', 'p'])
```



## 寻找两个集合之间的对称差异

它返回两个集合之间的对称差异。这意味着它返回一个包含两个集合中所有项目的集合，除了两个集合中都存在的项目，数学上： (A\B) ∪ (B\A)。

语法：

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st2.symmetric_difference(st1)) #  set(['item1', 'item4']) 
print(st1.symmetric_difference(st2)) # set(['item1', 'item4']
```



代码：

```python
whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.symmetric_difference(even_numbers))  # set([1, 3, 5, 7, 9]) 
print(whole_numbers.symmetric_difference(even_numbers)) # set([1, 3, 5, 7, 9])

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.symmetric_difference(dragon)) # set(['a', 'p', 'r', 'd', 'g', 'y', 'h', 't'])
```

## 连接集合

如果两个集合没有一个或多个公共项，我们称它们为不相交的集合。我们可以使用 isdisjoint() 方法检查两个集合是联合还是不相交。

语法：

```python
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st2.isdisjoint(st1)) # False
```

代码：

```python
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.isdisjoint(dragon)) # Fals
```

# 练习

## 给定集合

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```



# 练习 leve1

## 1、求集合 it_companies 的长度
```python
print(len(it_companies)) # 7
```



## 2、添加twitter到it_companies
```python
it_companies.add('twitter')
print(it_companies) # set(['Google', 'IBM', 'twitter', 'Amazon', 'Facebook', 'Oracle', 'Microsoft', 'Apple'])
```




## 3、一次插入多个 IT 公司到集合 it_companies

```python
other_companise = ['twitter', 'pd', 'oracle']
it_companies.update(other_companise)
print(it_companies) # set(['Google', 'IBM', 'twitter', 'oracle', 'Amazon', 'Facebook', 'pd', 'Oracle', 'Microsoft', 'Apple'])
```



## 4、从集合 it_companies 中删除其中一家公司

```python
print(it_companies.pop()) # Google
print(it_companies) #set(['IBM', 'twitter', 'oracle', 'Amazon', 'Facebook', 'pd', 'Oracle', 'Microsoft', 'Apple'])
```




## 5、删除(remove)和丢弃(discard)有什么区别?

> 我们可以使用 remove() 方法从集合中删除一个项目。如果未找到该项目，remove() 方法将引发错误，因此最好检查该项目是否存在于给定的集合中。但是，discard() 方法不会引发任何错误。

# 练习 level 2



## 1、john A and B

```python
print(A.union(B)) #  set([19, 20, 22, 24, 25, 26, 27, 28])
```

## 2、Find A intersection B

```python
print(A.intersection(B)) # set([19, 20, 22, 24, 25, 26])
```

## 3、Is A subset of B , A是B的子集嘛？

```python
print(A.issubset(B)) # True
```

## 4、A和B是不相交的集合吗？

```python
print(A.isdisjoint(B)) # False
```

## 5、将A与B相连，B与A相连



## 6、A和B的对称差异是什么

```python
print(B.difference(A)) # set([27, 28])
```

## 7、完全删除集合
```python
del A
del B
```

# 练习 level3

## 1、将年龄转换为集合，并比较列表和集合的长度，哪个更大？

```python
set_age = set(age)
print('集合:',set_age)

print(len(age)) # 8
print(len(set_age)) # 5
```

## 2、解释以下数据类型的区别：字符串、列表、元组和集合

- strings：字符串类型，也可以进行索引取值。
- list：列表是一个集合，有序，可修改的，允许有重复的成员。
- tuple：元组，是一个有序，不可修改的集合，允许有重复的成员。
- set：是一个无序，无所有、不可修改的集合，可以添加新成员，不允许有重复的成员