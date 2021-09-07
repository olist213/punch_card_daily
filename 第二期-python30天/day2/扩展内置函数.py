# coding: utf-8

# abs

num = -1
print(abs(num))

# all

a = [1,2,3,4]
print(all(a)) #true

b = ['a','b','','d']
print(all(b)) #true

c = [0,2,3,4]
print(all(c)) #false

d = (1,2,3,4)
print(all(d)) #true

e = ('a','b','','d')
print(all(e))#false

f = (0,1,2,3)
print(all(f)) # false

print(all([]))
print(all(()))

# bin

num1 = 12
print(bin(num1)) # 0b1100

#bool
print(bool(0)) # False
print(bool(1)) #True
print(bool()) #False

#chr

print(chr(0x30),chr(0x31),chr(0x61)) # ('0', '1', 'a')
print(chr(48),chr(49),chr(97)) # ('0', '1', 'a')

#complex
print(complex(1,2)) #(1+2j)

#dict
print(dict(a='a',b='b',c='c')) # {'a': 'a', 'c': 'c', 'b': 'b'}
print(dict(zip(['one','two','three'], [1,2,3]))) #{'three': 3, 'two': 2, 'one': 1}
print(dict([('one',1),('two',2),('three',3)])) #{'three': 3, 'two': 2, 'one': 1}

#eval

a = 7
print(eval('a * 3')) #21

#divmod

print(divmod(7,2)) # (3,1)
print(divmod(8,2)) # (4,0)

# file

# f = file('./1.txt')
# print(f.read())

#filter

def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd,[1,2,3,4,5,6,7,8,9,0])
print(newlist) # [1, 3, 5, 7, 9]

## 过滤出1~100中平方根是整数的数

import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

newlist = filter(is_sqr, range(1, 101))
print(newlist) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## format

print("{} {}".format("hello","world"))
print("{0} {1}".format("hello","world"))
print("{0} {1} {0}".format("hello","world"))

### output
# hello world
# hello world
# hello world hell

print("网站名:{name},url:{url}".format(name = "test",url = "http://www.test.com/"))

# 字典设置
dict1 = {"name":"test","url":"http://www.test.com/"}
print("网站名:{name},url:{url}".format(**dict1))

# 通过列表索引
my_lists = ["test","http://www.test.com/"]
print("网站名:{0[0]},url:{0[1]}".format(my_lists))

# getattr

class A(object):
    bar = 1

a = A()
print(a)
print(getattr(a,"bar"))

#hex 
a = 123
print(hex(a))

# iter 

lst = [1,2,3]
for i in iter(lst):
    print(i)
#output
#1
#2
#3

#len

print(len("liangcheng")) # 6
print(len([1,2,3,4,5,6])) # 10

## list

aTuple = ("one","two","three")
print(list(aTuple)) # ['one', 'two', 'three']

## locals

def zens(arg):
    z = 1
    print(locals())

zens(4) #{'z': 1, 'arg': 4}

## map

def square(x):
    return x**2

s = map(square, [1,2,3,4])
print(s) # [1, 4, 9, 16]

### 使用lambda匿名函数
print(map(lambda x: x**2, [1,2,3,4])) # [1, 4, 9, 16]

print(map(lambda x,y: x + y, [1,2,3,4],[5,6,7,8])) # [6, 8, 10, 12]

### 规范名字格式。
name_list = {'tony','wenDi','heLlo Kitty'}

def format_name(s):
    ss = s[0:1].upper() + s[1:].lower()
    return ss

print(list(map(format_name,name_list)))

### filter 与 map 的区别

res = map(lambda x: x > 5, range(10))
print(list(res)) # [False, False, False, False, False, False, True, True, True, True]

res1 = filter(lambda x: x > 5, range(10))
print(res1) # [6, 7, 8, 9]


# next

it = iter([1,2,3,4,5])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break