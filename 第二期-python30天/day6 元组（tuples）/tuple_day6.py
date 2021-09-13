# coding: utf-8

fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruits = fruits[0]
second_fruits = fruits[1]
last_index = len(fruits) - 1
last_fruits = fruits[last_index]

print(first_fruits)
print(second_fruits)
print(last_fruits)

fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruits = fruits[-4]
second_fruits = fruits[-3]
last_fruits = fruits[-1]

print(first_fruits)
print(second_fruits)
print(last_fruits)

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

## negative indexes

tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]
print(all_items) # ('item1', 'item2', 'item3', 'item4')
print(middle_two_items) # ('item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]

# 将元组转成列表
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits) # ['apple', 'orange', 'mango', 'lemon'
fruits = tuple(fruits)
print(fruits) # ('apple', 'orange', 'mango', 'lemon')

# in 

fruits = ('banana', 'orange', 'mango', 'lemon')
print('apple' in fruits) # False
print('orange' in fruits) # True

# +
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion')

# del
tpl = ('item1', 'item2', 'item3', 'item4')
# del tpl
print(tpl) # NameError: name 'tpl' is not defined

# 练习
# 1、创建一个空元组

tpl = ()
print(tpl) # ()

# 2、创建一个包含你姐妹和兄弟名字的元组（想象中的兄弟姐妹也可以）。

tpl_brothers = ('zhangsan', 'lisi', 'wanglaowu')
tpl_sisters = ('luna', 'andi', 'john')

# 3、Join brothers and sisters tuples and assign it to siblings

brothers_and_sisters = tpl_brothers + tpl_sisters
print(brothers_and_sisters)
wanglaowu_and_luna = brothers_and_sisters[2:4]
print(wanglaowu_and_luna)

print(len(brothers_and_sisters))

lst = list(brothers_and_sisters)
lst.append('liuwu')
lst.append('wanghui')
print(lst)
family_members = tuple(lst)
print(family_members)