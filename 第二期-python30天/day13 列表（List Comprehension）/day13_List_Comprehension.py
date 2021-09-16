# coding: utf-8

# 第一种方式
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

# 第二种方式

lst = [i for i in language]
print(type(lst))
print(lst)

# 生成一个数字列表

numbers = [i for i in range(11)]
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [i * i for i in range(11)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers = [(i, i * i) for i in range(11)]
print(numbers) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

# if

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 过滤出正数且是偶数

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0 ]
print(positive_even_numbers) # [4, 6, 8, 10]

# 展开一个三维数组
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lambda

def add_two_nums(a,b):
    return a + b

print(add_two_nums(2,3)) # 5

## lambda匿名函数

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3)) # 5

## 自我调用的lambda函数

print((lambda a, b: a + b)(2,3)) # 5

square = lambda x: x ** 2
print(square(3)) # 9
cube = lambda x : x ** 3
print(cube(3)) # 27

## 多个变量
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5,5,3)) # 22

def power(x):
    return lambda n : x ** n

cube = power(2)(3)
print(cube) # 8

two_power_of_five = power(2)(5)
print(two_power_of_five) # 32

# 练习

# 1、使用列表推导式在列表中只过滤负数和零数

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

p_number = [i for i in numbers if i <= 0]
print(p_number) # [-4, -3, -2, -1, 0]

# 2、将下面的列表的列表扁平化为一个一维的列表。

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lst = [i for row in list_of_lists for pp in row for i in pp]
print(lst)

# 使用列表推导式创建以下元组列表。

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

x = 1
l = [(i * x,x,i,i * (i * x),i * (i * (i * x)),i * (i * (i * (i * x))),i * (i * (i * (i * (i * x))))) for i in range(11) ]
print(l)

# 4、将以下列表展平为新列表：

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

for i in countries:
    for x in i:
        print(list(x))

t = [list(x) for i in countries for x in i]
print(t) # [['Finland', 'Helsinki'], ['Sweden', 'Stockholm'], ['Norway', 'Oslo']]

# 5、将以下列表更改为字典列表：

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict = {}
lst = []

for i in countries:
    for x in i:
        dict['country'] = x[0]
        dict['city'] = x[1]
        lst.append(dict)

print(lst)

# 6

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst = [] 

for i in names:
    for y in i:
        str = " ".join(list(y))
        lst.append(str)
print(lst)
