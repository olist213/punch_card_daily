#coding: utf-8

a = 3
if a > 0:
    print('A is a positive number')


## if...else...

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
    
# if...elif...else...

a = 3
if a < 0:
    print('A is a negative number')
elif a > 0:
    print('A is a positive number')
else:
    print('A is zero')

## short hand

a = 3
# print('A is a positive') if a > 0 else print('A is a negative') # A is a positive

## 嵌套语句

a = 0
if a > 0:
    if a % 0 == 0:
        print('A is  a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

a = 0
if a > 0 and a % 0 == 0:
    print('A is  a positive and even integer')
    print('A is a positive number')
elif a > 0 and a % 2 != 0:
    print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access Granted!')
else:
    print('Access Denied')