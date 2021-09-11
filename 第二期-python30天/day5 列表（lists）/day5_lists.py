# coding: utf-8

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

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit= fruits[-4]
print(first_fruit) # banana
first_fruit= fruits[-1]
print(first_fruit) # lemon
first_fruit= fruits[-2]
print(first_fruit) # mango

print("-------------------")

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

first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first) #1 
print(second) #2
print(third) #3
print(rest) # [4,5,6,7,8,9]
print(tenth) #10

# 切割
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

# 修改列表

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits) # ['avocado', 'orange', 'mango', 'lemon']

fruits[1] = 'apple'
print(fruits) # ['avocado', 'apple', 'mango', 'lemon']

last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits) # ['avocado', 'apple', 'mango', 'lime']


# 检查元素

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist) #True

does_exist = 'lime' in fruits
print(does_exist) # False

# 追加元素
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits) #['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

#  插入元素
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(3, 'apple')
print(fruits) # ['banana', 'orange', 'mango', 'apple', 'lemon']

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.pop()) # lemon
print(fruits) # ['banana', 'orange', 'mango']
print(fruits.pop(1)) # orange
print(fruits) # ['banana', 'mango']

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

# clear()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) # []

# copy
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy) # ['banana', 'orange', 'mango', 'lemon']

# joining list
positive_numbers = [1,2,3,4,5]
zero = [0]
negative = [-5,-4,-3,-2,-1]
integers = negative + zero + positive_numbers 
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# extend
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print(num1) # [0, 1, 2, 3, 4, 5, 6]

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange')) # 1

age = [22,45,22,34,21,22,35]
print(age.count(22)) # 3

# index()
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('banana')) # 0
age = [22,45,22,34,21,22,35]
print(age.index(22)) # 0

# reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
age = [22,45,22,34,21,22,35]
age.reverse()
print(age) # [35, 22, 21, 34, 22, 45, 22]

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

## sorted
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits)) # ['banana', 'lemon', 'mango', 'orange']

# reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']

## 列表解析

a = [(x,y) for x in [1,2] for y in [3,4]]
print(a) # [(1, 3), (1, 4), (2, 3), (2, 4)]

b = [(x,y) for x in [1,2]for y in [3,x]]
print(b) # [(1, 3), (1, 1), (2, 3), (2, 2)]