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

# 8.计算斜率，y = 2x - 2
## 额，直线方程，y = kx + b，斜率就是k

# 9.斜率为（m=y2-y1/x2-x1）。求点（2，2）与点（6，10）之间的斜率和欧几里得距离
## pass，-_-|

# 如果知道直线方程 y = kx + b ,那么 k 就是斜率
# 如果不知道直线方程,但知道直线上的两个点 (x1 , y1) ,(x2 ,y2)
# 那么斜率 k = (y2 - y1)/(x2 - x1)
# 如果 x1 = x2 ,那么直线斜率不存在

## 第一个斜率应该为

x1 = 2
y1 = 2
x2 = 6
y2 = 10

m = (y2 - y1) / (x2 - x1)
print(m) # 2.0

#11. 计算y的值（y=x^2+6x+9）。尝试使用不同的x值，并找出在什么x值下y会是0。

x = 1
y = x^2 + 6*x + 9
print(y) # y = 16


x1 = 2
y = x1^2 + 6*x1 + 9
print(y) # y = 21 

# 为了求当y=0时，x的值，那么即使(x+3)^2 = 0，那么x=-3
x = -3
y1 = (x + 3)*(x + 3)
print(y1) # y1 = 0

# 12. 比较“python”和“dragon”字符的长度

p = len('python')
d = len('dragon')

if p > d:
    print("python too long!")
elif p == d:
    print("python equal dragon")
else:
    print("dragon too long!")

# 13. 用and运算符检查on是否同时出现在python和dragon中

p1 = "python"
d1 = "dragon"

if 'on' in str(p1) and 'on' in str(d1):
    print("on in python and dragon")
else:
    print("nonono")

# 15. python和dradon中no ‘on’
p1 = "python"
d1 = "dragon"

if 'on' not in str(p1) and 'on' not in str(d1):
    print("on no in python and dragon")
else:
    print("on in python and dragon.")

# 16. 查找文本(python)的长度，并将该值转换为float，然后将其转换为字符串。

length = len("python")
length_f = float(length)
print("浮点数",length_f)
print("字符串：", type(str(length_f)))

# 17. 偶数能被2整除，且余数为零。如何用python检查一个数字是否是偶数？

num = int(input("pls input a number: "))
while True:
    if num % 2 == 0:
        print("这个数字是一个偶数！")
        break
    else:
        print("oh no")
        break

# 18. 检查7除以3的底线是否等于2.7的int转换值。

div_num = 7 / 3
# print(div_num)
num_int = int(2.7)
if div_num == num_int:
    print("相等")
else:
    print("不相等") # 不相等

# 19. 检查'10'的类型是否等同于10的类型，一个字符串一个整数肯定不相等

s1 = '10'
s2 = 10

if s1 == s2:
    print("s1:",s1,"=","s2:",s2)
else:
    print("s1:",s1,"!=","s2:",s2)

# 20. 检查int('9.8')是否等于10

s3 = int(9.8)
s4 = 10

if s3 == s4:
    print("s3:",s3,"=","s4:",s4)
else:
    print("s3:",s3,"!=","s4:",s4)

# 21 工时计算

hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
print("Your weekly earning is ",hours * rate_per_hour)

# 22 写一个脚本，提示用户输入年数。计算一个人可以活多少秒。假设一个人可以活100年

year = int(input('pls input year:'))
print("person live:",year * 12 *30 * 24 * 60 * 60) # input 100 output 3110400000

# 23 编写一个Python脚本，显示以下表格

'''
Write a Python script that displays the following table

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

'''

for i in range(1,6):
    x = 1
    print('{} {} {} {} {}'.format(i, x, i * x, i * (i * x), i * (i * (i * x))))




