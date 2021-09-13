# coding: utf-8

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits)) # 4

st = {'item1', 'item2', 'item3', 'item4'}
print('st集合中是否存在item3：', 'item3' in st) # True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('banana' in fruits) # True

# add
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('apple')
print(fruits) # set(['orange', 'mango', 'lemon', 'banana', 'apple'])

# update

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
fruits.update(vegetables)
print(fruits) # set(['Tomato', 'lemon', 'Onion', 'Potato', 'mango', 'orange', 'Cabbage', 'banana'])

# remove , pop
fruits = {'banana', 'orange', 'mango', 'lemon'}
# print(fruits.pop()) # banana
print(fruits) # {'orange', 'lemon', 'mango'}

# clear 
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.clear()) # None

# del
st = {'item1', 'item2', 'item3', 'item4'}
del st

# list set 转换
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits = set(fruits)
print(fruits) # set(['orange', 'mango', 'lemon', 'banana'])

# 集合连接

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3) # set(['item8', 'item2', 'item3', 'item1', 'item6', 'item7', 'item4', 'item5'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
print(fruits.union(vegetables)) # set(['Tomato', 'lemon', 'Onion', 'Potato', 'mango', 'orange', 'Cabbage', 'banana'])

# update
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # set(['item8', 'item2', 'item3', 'item1', 'item6', 'item7', 'item4', 'item5'] 
print(st1)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
fruits.update(vegetables)
print(fruits) # set(['Tomato', 'lemon', 'Onion', 'Potato', 'mango', 'orange', 'Cabbage', 'banana']

# intersecion

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.intersection(even_numbers)) # set([0, 2, 4, 6, 8, 10]

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.intersection(dragon)) # set(['o', 'n']

# subset super set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}

print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.issubset(even_numbers))  # False
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.issubset(dragon)) # False

# difference
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st2.difference(st1)) # set([] 
print(st1.difference(st2)) # set(['item1', 'item4']) 

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.difference(even_numbers))  # set([1, 3, 9, 5, 7] 
print(whole_numbers.difference(even_numbers)) # set([1, 3, 9, 5, 7])

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.difference(dragon)) # set(['y', 'h', 't', 'p'])

# symmetric difference

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st2.symmetric_difference(st1)) #  set(['item1', 'item4']) 
print(st1.symmetric_difference(st2)) # set(['item1', 'item4']

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}
print(whole_numbers.symmetric_difference(even_numbers))  # set([1, 3, 5, 7, 9]) 
print(whole_numbers.symmetric_difference(even_numbers)) # set([1, 3, 5, 7, 9])

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.symmetric_difference(dragon)) # set(['a', 'p', 'r', 'd', 'g', 'y', 'h', 't'])

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st2.isdisjoint(st1)) # False

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python.isdisjoint(dragon)) # False


## 练习
## 给定集合

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

## 练习 level 1

## 1、求集合 it_companies 的长度
print(len(it_companies)) # 7

## 2、添加twitter到it_companies
it_companies.add('twitter')
print(it_companies) # set(['Google', 'IBM', 'twitter', 'Amazon', 'Facebook', 'Oracle', 'Microsoft', 'Apple'])


## 3、一次插入多个 IT 公司到集合 it_companies

other_companise = ['twitter', 'pd', 'oracle']
it_companies.update(other_companise)
print(it_companies) # set(['Google', 'IBM', 'twitter', 'oracle', 'Amazon', 'Facebook', 'pd', 'Oracle', 'Microsoft', 'Apple'])

## 4、从集合 it_companies 中删除其中一家公司

print(it_companies.pop()) # Google
print(it_companies) #set(['IBM', 'twitter', 'oracle', 'Amazon', 'Facebook', 'pd', 'Oracle', 'Microsoft', 'Apple'])


## 5、删除(remove)和丢弃(discard)有什么区别?

# 我们可以使用 remove() 方法从集合中删除一个项目。如果未找到该项目，remove() 方法将引发错误，因此最好检查该项目是否存在于给定的集合中。但是，discard() 方法不会引发任何错误。



# level 2

## 1、john A and B

print(A.union(B)) #  set([19, 20, 22, 24, 25, 26, 27, 28])

## Find A intersection B

print(A.intersection(B)) # set([19, 20, 22, 24, 25, 26])

## Is A subset of B , A是B的子集嘛？

print(A.issubset(B)) # True

## A和B是不相交的集合吗？

print(A.isdisjoint(B)) # False

## 将A与B相连，B与A相连

## A和B的对称差异是什么

print(B.difference(A)) # set([27, 28])

## 完全删除集合
del A
del B
print("-----------")

# level 3

## 将年龄转换为集合，并比较列表和集合的长度，哪个更大？

set_age = set(age)
print('集合:',set_age)

print(len(age)) # 8
print(len(set_age)) # 5

