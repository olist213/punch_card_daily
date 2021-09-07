#coding: utf-8

#pring
print("hello,world")
print("hello,world","my name is liangcheng")

#len
#输出5
print(len("hello"))

#输出0
a = ""
print(len(a))

#输出3,tuple
b = ("a","b","c")
print(len(b)) 

# list 输出5
c = [1,2,3,4,5]
print(len(c))

# range 输出9
d = range(1,10)
print(len(d))

# dict 字典 输出1
e = {"name":"liangcheng"}
print(len(e))

# set 输出5 
f = {1,2,3,4,"laohu"}
print(len(f))

# str
## 输出<type 'str'>
print(type(str(10)))

# int
##  输出：<type 'int'> 
print(type(int('123')))

#float
## 
print(type(float(10)))