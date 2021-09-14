#coding: utf-8

count = 0
while count < 5:
    print(count)
    count = count + 1

# while...else...
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# continue
count = 0
while count < 5:
    if count == 3:
        count = count +  1
        continue

    print(count)
    count = count + 1

# for with list

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

# for with string

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# for with tuple

tpl = (0,1,2,3,4,5)
for number in tpl:
    print(number)

# for with dict

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

# ('first_name', 'Asabeneh')
# ('last_name', 'Yetayeh')
# ('skills', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'])
# ('country', 'Finland')
# ('age', 250)
# ('address', {'street': 'Space street', 'zipcode': '02210'})
# ('is_marred', True)

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

    if number == 3:
        break

# continue

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

    if number == 3:
        continue

    # print('Next number should be ', number + 1) if number != 5 else print('loop end')
print('outside the loop')

# 0
# Next number should be  1
# 1
# Next number should be  2
# 2
# Next number should be  3
# 3
# 4
# Next number should be  5
# 5
# loop end
# outside the loop

# range

lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = list(range(1,11))
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]

st = set(range(0,11,2))
print(st) # set([0, 2, 4, 6, 8, 10])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# output
# JavaScript
# React
# Node
# MongoDB
# Python

# for...esle...

for number in range(11):
    print(number)
else:
    print('The loop stops at:', number) # ('The loop stops at:', 10)

print('练习')

# 练习
# 1、使用 for 循环迭代 0 到 10，使用 while 循环执行相同的操作。

## for

for number in range(11):
    print(number)

## while
number = 0
while number <= 10:
    print(number)
    number = number + 1

## 2、使用for循环遍历10到0，使用while循环做同样的事情。
### for
for number in range(10, 0, -1):
    print(number)

### while
number = 10
while number <= 10:
    print('while:',number)
    number = number -1

    if number < 0:
        break

# 3、写一个循环，对print()进行7次调用，因此我们在输出端得到以下三角形。

for i in range(7):
    if i == 1:
        print("#")
    if i == 2:
        print("##")
    if i == 3:
        print("###")
    if i == 4:
        print("####")
    if i == 5:
        print("#####")
    if i == 6:
        print("######")
    if i == 7:
        print("#######")

# 4、使用嵌套循环建立下面的内容：

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #


for x in range(0, 9):
    for y in range(0, 9):
        print("# ", end="")
    print()


# 5、打印如下内容：
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for x in range(0,11):
    for y in range(0,11):
        if x != y:
            continue
        print(x,'x',y,'=',x*y)

## 使用for循环遍历列表中的['Python', 'Numpy', 'Pandas', 'Django', 'Flask']并打印出项目。

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for s in lst:
    print(s)

## 7、使用for循环从0到100进行迭代，只打印偶数。

for i in range(0,100):
    if i % 2 == 0:
        print(i)

## 8、使用 for 循环从 0 到 100 迭代，只打印奇数

for i in range(0,100):
    if i % 2 != 0:
        print(i)
    
# level2

## 1、使用for循环，从0到100进行迭代，并打印所有数字的总和。
sum = 0
for i in range(0,101):
    sum = sum + i
print(sum)

## 2、使用for循环从0到100进行迭代，并打印所有偶数和所有奇数的总和。

evens_sum = 0
odds_sum = 0

for i in range(0,101):
    if i % 2 == 0:
        evens_sum = evens_sum + i
    
    if i % 2 != 0:
        odds_sum = odds_sum + i

print(evens_sum) # 2550
print(odds_sum) # 2500
