#coding: utf-8

print("加法：",3 + 2) #5
print("减法：",3 - 2) #1
print("乘法：",3 * 2) #6
print("除法：",3 / 2) #1
print("除法：",7 / 2) #3
print("不含余数：",7 // 2) #3
print("不含余数：",7 // 3) #2
print("取余：",7 % 3) #1
print("求幂：",2 ** 3) #8

## float 浮点数

print("浮点数：PI", 3.14)
print("浮点数：gravity", 9.81)

## complex 复数

print("复数：", 1 + 2j)
print("复数相乘：", (1 + 2j) * (1 + 1j))

## example 多个变量

a = 2
b = 3

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# output 

# 5
# ('a + b = ', 5)
# ('a - b = ', -1)
# ('a * b = ', 6)
# ('a / b = ', 0)
# ('a % b = ', 2)
# ('a // b = ', 0)
# ('a ** b = ', 8)

# 计算一些数字公式

## 计算圆的面积
radius = 10
area_of_circle = 3.14 * radius ** 2
print("圆的面积为：", area_of_circle) # 314.0

##计算长方形的面积

length = 10
width = 20
area_of_rectangle = length * width
print("长方形的面积为：", area_of_rectangle) # 200

## 计算一个物体的重量
mass = 75
gravity = 9.81
weight= mass * gravity
print(weight,'N')

## 计算液体的密度
mass = 75 # kg
volume = 0.075 # 立方米
density = mass / volume # 1000 kg /m^3
print(density)

## 比较运算符

print(3 > 2) # True
print(3 >= 2) # True
print(3 < 2) # False
print(3 <= 2) # False
print(3 == 2) # False
print(3 != 2) # True
print(len('mango') == len('avocado')) # False
print(len('mango') != len('avocado')) # True
print(len('mango') < len('avocado')) # True
print(len('milk') != len('meat')) # False 
print(len('milk') == len('meat')) # True
print(len('tomato') == len('potato')) # True
print(len('python') > len('dragon')) # False

print('True == True: ', True == True)
print('True == False : ', False == True)
print('False== False : ', False == False)

print('1 is 1', 1 is 1) # True
print('1 is not 2', 1 is not 2) # True
print('A in Asabeneh', 'A' in 'Asabeneh') # True
print('B in Asabeneh', 'B' in 'Asabeneh') # False
print('coding' in 'coding for all') # True
print('a in an','a' in 'an') # True
print('4 is 2 ** 2:', 4 is 2 ** 2) # True


# 逻辑运算符
print('-----------------')
print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False
print(3 < 2 and 4 < 3) # False
print('True and True: ', True and True) # True
print(3 < 2 or 4 > 3) # True
print(3 < 2 or 4 < 3) # False
print(3 < 2 or 4 > 3) # True
print('True or True: ', True or True) # True
print(not 3 > 2) # False
print(not True) # False
print(not False) # True
print(not not True) # True
print(not not False) #False

# 练习

# 1.定义age 整数变量
age = 23

# 2.定义身高，浮点数
height = 180.32

# 3.定义复数
c_number = 1 + 5j

# 4.编写脚本，提示用户输入三角形的地和高，并计算三角形的面积。

base = int(input("请输入三角形的底："))
height = int(input("请输入三角形的高："))
area = 0.5 * base * height
print("三角形的面积为：", area) # 100.0

# 5.编写脚本，提示用户输入三角形的a边、b边、c边，计算三角形的周长。<a+b+c>

a = int(input("pls input a:")) 
b = int(input("pls input b:")) 
c = int(input("pls input c:")) 
perimeter = a + b + c
print(perimeter)

# 6.编写脚本，获取矩形的长与宽，计算其面积和周长。
width = int(input("pls input width:"))
height = int(input("pls input height:"))
area = width * height
print(area)
perimeter = 2 * (width * height)
print(perimeter)

# 7. 编写脚本，获取圆的半径，计算面积（area = pi*r*r）和周长c = 2*pi*r。
pi = 3.14
radius = int(input("pls input radius:"))
area = pi * radius * radius
print(area)
circumference = 2 * pi * radius 
print(circumference)




