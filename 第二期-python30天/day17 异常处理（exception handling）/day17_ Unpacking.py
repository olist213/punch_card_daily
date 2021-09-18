# coding: utf-8

def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]

# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# print(sum_of_five_nums(lst))

def sum_of_five_nums(a,b,c,d,e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst)) # 15

numbers = range(2, 7)
print(list(numbers)) # [2, 3, 4, 5, 6]

args = [2, 7]
numbers = range(*args)
print(list(numbers)) # [2, 3, 4, 5, 6]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest) # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1,2,3,4,5,6,7]
one, *middle, last = numbers
print(one, middle, last) # 1 [2, 3, 4, 5, 6] 7

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. he is {age} year old.'

dct = {'name':'liang', 'country':'china', 'city':'beijing', 'age':28}
print(unpacking_person_info(**dct)) # liang lives in china, beijing. he is 28 year old.

# packing list

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1,2,3)) # 6
print(sum_all(1,2,3,4,5,6,7)) # 28

def packing_person_info(**kwargs):

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

# {'name': 'liang', 'country': 'china', 'city': 'shanghai', 'age': 18}
print(packing_person_info(name='liang',country='china',city='shanghai',age=18))

# Spreading in Python

lst_one = [1,2,3]
lst_two = [4,5,6]
lst = [0, *lst_one, *lst_two]
print(lst) # [0, 1, 2, 3, 4, 5, 6]

country_lst_one = ['Finland', 'sweden', 'norway']
country_lst_two= ['denmak', 'icelang', 'china']
nordic_country = [*country_lst_one, * country_lst_two]
# ['Finland', 'sweden', 'norway', 'denmak', 'icelang', 'china']
print(nordic_country)

# enumerate

for index, item in enumerate([20, 30, 40]):
    print(index, item)

# 0 20
# 1 30
# 2 40

for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'the country {i} has been found at index {index}')

# zip
fruits = ['banana', 'orange', 'mango', 'lemon','lime']
vegetables = ['tomato','potato', 'cabbage', 'onion','carrot']
fruits_and_vegetables = []
for f,v in zip(fruits, vegetables):
    fruits_and_vegetables.append({'fruit':f, 'veg':v})

# [{'fruit': 'banana', 'veg': 'tomato'}, {'fruit': 'orange', 'veg': 'potato'}, {'fruit': 'mango', 'veg': 'cabbage'}, {'fruit': 'lemon', 'veg': 'onion'}, {'fruit': 'lime', 'veg': 'carrot'}]
print(fruits_and_vegetables)


