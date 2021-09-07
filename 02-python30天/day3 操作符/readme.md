# 0x01 布尔值（boolean）

boolean数据类型只有两个值，分别为True和False，首字母需要大写。

```python
print(True)
print(False)
```

# 0x02 操作符（Operators）

## 赋值运算符

赋值运算符是用来给变量进行赋值的，用`=`号进行赋值，

下面这种图是常用的一些赋值运算符。![Assignment Operators](https://raw.githubusercontent.com/olist213/olistimg/master/upic/assignment_operators.png)

## 算数运算符

- 加法：a+b
- 减法：a-b
- 乘法：a*b
- 除法：a/b
- 取模：a%b
- Floor division：a//b
- 求幂：a**b

![Arithmetic Operators](https://raw.githubusercontent.com/olist213/olistimg/master/upic/arithmetic_operators.png)

> 算数运算符

代码：（整数）

```python
print("加法：",3 + 2) #5
print("减法：",3 - 2) #1
print("乘法：",3 * 2) #6
print("除法：",3 / 2) #1
print("除法：",7 / 2) #3
print("不含余数：",7 // 2) #3
print("不含余数：",7 // 3) #2
print("取余：",7 % 3) #1
print("求幂：",2 ** 3) #8
```

代码：（浮点数）

```python
print("浮点数：PI", 3.14)
print("浮点数：gravity", 9.81)
```

代码：（复数）

```python
print("复数：", 1 + 2j)
print("复数相乘：", (1 + 2j) * (1 + 1j)) # (-1+3j)
```

继续来点实例，声明一个变量并赋值，然后将算数运算的结果赋给另一个变量，最后打印出来。

```python
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
```

实例：（数学公式计算）

```python
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
```

## 比较运算符

在编程中，我们比较数值，检查一个值是否大于或小于或等于其他值。

![Comparison Operators](https://raw.githubusercontent.com/olist213/olistimg/master/upic/comparison_operators.png)

> 实例：(比较运算符)

```python
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
```

除了上述运算符之外，还可以使用下面的运算符：

- is：如果两个变量是同一个对象，则返回真，反之。（x is y）
- is not：如果两个变量不是同一个对象，则返回真，反之。（x is not y）
- in：如果查询列表包含某个项目，（x in y），则返回真，反之。
- not in：如果查询的列表中没有包含某个项目，（x not in y），返回真，反之。

代码：

```python
print('1 is 1', 1 is 1) # True
print('1 is not 2', 1 is not 2) # True
print('A in Asabeneh', 'A' in 'Asabeneh') # True
print('B in Asabeneh', 'B' in 'Asabeneh') # False
print('coding' in 'coding for all') # True
print('a in an','a' in 'an') # True
print('4 is 2 ** 2:', 4 is 2 ** 2) # True
```

## 逻辑运算符

- and：逻辑与，有一个为假则为假。
- or：逻辑或，有一个为真则为真。
- not：逻辑反。

![Logical Operators](https://raw.githubusercontent.com/olist213/olistimg/master/upic/logical_operators.png)

代码：

```python
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
```

---

# 0x03 第三天的练习

