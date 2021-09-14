# coding:utf-8

## 创建空字典

empty_dict = {}

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct)

### example:

person = {
    'first_name':'liang',
    'last_name':'cheng',
    'age':130,
    'country':'finland',
    'is_married':False,
    'skills':['php', 'python', 'bash', 'mysql'],
    'address':{
        'street':'space street',
        'zipcode':'02909'
    }
}

### len

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

print(len(person)) # 7

### 访问字典里的值

print(person['first_name']) # liang
print(person['country']) # finland
print(person['skills'][0]) # php
print(person['address']['street']) # space street

### add items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
print(dct) # {'key3': 'value3', 'key2': 'value2', 'key1': 'value1', 'key5': 'value5', 'key4': 'value4'}



### modify dict values

person['first_name'] = 'qing'
person['age'] = 222
print(person) # {'first_name': 'qing', 'last_name': 'cheng', 'skills': ['php', 'python', 'bash', 'mysql'], 'country': 'finland', 'age': 222, 'address': {'street': 'space street', 'zipcode': '02909'}, 'is_married': False}

### remove item

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1')
print(dct) # {'key3': 'value3', 'key2': 'value2', 'key4': 'value4'}

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.popitem()) # ('key3', 'value3')
print(dct) # {'key2': 'value2', 'key1': 'value1', 'key4': 'value4'}

del dct['key2']
print(dct) # {'key1': 'value1', 'key4': 'value4'}

print(person)

print(person.pop('first_name')) # qing
print(person.popitem()) # ('last_name', 'cheng')
del person['is_married']
print(person) # {'skills': ['php', 'python', 'bash', 'mysql'], 'country': 'finland', 'age': 222, 'address': {'street': 'space street', 'zipcode': '02909'}


# items

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # [('key3', 'value3'), ('key2', 'value2'), ('key1', 'value1'), ('key4', 'value4')]

# keys

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_keys = dct.keys()
print(dct_keys) # ['key3', 'key2', 'key1', 'key4']

# values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_values = dct.values()
print(dct_values) # ['value3', 'value2', 'value1', 'value4']

# 练习

