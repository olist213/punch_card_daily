#coding: utf-8

## 练习、level 1

### 2、Write a python comment saying 'Day 2: 30 Days of python programming'

print('Day 2:30 Days of python programming!')

### 3、Declare a first name variable and assign a value to it

first_name = "liang"
print(first_name)

### 4、Declare a last name variable and assign a value to it
last_name = "cheng"
print(last_name)

### 5、Declare a full name variable and assign a value to it


### 6、Declare a country variable and assign a value to it
country = "china"
print(country)

### 7、Declare a city variable and assign a value to it
city = 'beidai'
print(city)

### 8、Declare an age variable and assign a value to it
age = 123
print(age)

### 9、Declare a year variable and assign a value to it
year = 1992
print(year)

### 10、Declare a variable is_married and assign a value to it
is_married = False
print(is_married)

### 11、Declare a variable is_true and assign a value to it
is_true = True
print(is_true)

### 12、Declare a variable is_light_on and assign a value to it
is_light_on = "no"
print(is_light_on)

### 13、Declare multiple variable on one line

first_name, last_name, country, age = "liang", "cheng", "china", 120
print(first_name,last_name,country,age)

# 练习 level 2

##Check the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

## Using the len() built-in function, find the length of your first name

my_name = "liangcheng"
print(len(my_name))

if len(first_name) > len(last_name):
    print("first name to long")
else:
    print(len(first_name))
    print(len(last_name))
    print("last name to long")

## Declare 5 as num_one and 4 as num_two
### Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4

total = num_one + num_two
print(total)

### Subtract num_two from num_one and assign the value to a variable diff 
diff = num_two - num_one
print(diff)

### Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

### Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

### Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

### Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

### Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

## The radius of a circle is 30 meters(一个圆的半径是30米)
### Calculate the area of a circle and assign the value to a variable name of area_of_circle(计算一个圆的面积，并将该值分配给一个名为 area_of_circle 的变量。)
### S=πr²

area_of_circle = 3.14 * (30 ** 2)
print(area_of_circle)

### Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle(计算一个圆的周长，并将该值赋给一个名为circum_of_circle的变量。)
circum_of_circle = 3.14 * 30 * 2
print(circum_of_circle)


### Take radius as user input and calculate the area.(将半径作为用户输入，并计算出面积。)

r = input("pls input r:")
print(3.14 * int(r) ** 2)

### Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names(使用内置的输入函数从用户那里获得名字、姓氏、国家和年龄，并将其值存储到相应的变量名中。)

first_name = input("pls input you first name:")
print(first_name)

last_name = input("pls input you last name:")
print(last_name)

country = input("pls input you country:")
print(country)

age = input("pls input you age:")
print(age)

### Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

'''
>>> help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
'''

