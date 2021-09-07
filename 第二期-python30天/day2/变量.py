# coding: utf-8

first_name = 'liang'
last_name = 'cheng'
country = 'china'
age = 120
is_married = False
skills = ['pentest','ctf','redtem']
person_info = {
    'firstname':'liang',
    'lastname':'cheng',
    'country':'china',
    'aget':12
}

print('first_name',first_name)
print('last_name',last_name)
print('country',country)
print('age',age)
print('is_married',is_married)
print('skills',skills)
print('person_info',person_info)

# 多行变量

first_name, last_name, country, age, is_married = 'liang', 'cheng', 'china', 123, False

print(first_name, last_name, country, age, is_married)

print('first_name',first_name)
print('last_name',last_name)
print('country',country)
print('age',age)
print('is_married',is_married)

# input 变量
first_name = input('pls input first name:')
age = input('pls input age:')

print(first_name)
print(age)