#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :day21_classes_objects.py
@说明    :
@时间    :2021/09/22 11:58:50
@作者    :liangcheng
@版本    :1.0
'''

num = 10
print(type(num))

string = 'string'
print(type(string))

boolean = True
print(type(boolean))

# create class

class Person:
    pass

print(Person) # <class '__main__.Person'>

p = Person()
print(p) # <__main__.Person object at 0x104792c40>

class Person:
    def __init__(self, name):
        self.name = name

p = Person('liangcheng')
print(p.name) # liangcheng
print(p) # <__main__.Person object at 0x100f39f40>

class Person:
    def __init__(self, firstname,lastname,age,country,city) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city 
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'

p = Person('liangcheng', 'xxx', 83, 'china', 'xxx111')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
print(p.person_info()) # liangcheng xxx is 83 years old.

class Person:
    def __init__(self, firstname='liang',lastname='cheng',age=25,country='china',city='xxx') -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city 
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'

p1 = Person()
print(p1.person_info()) # liang cheng is 25 years old.
p2 = Person('liangcheng', 'xxx', 83, 'china', 'xxx111')
print(p2.person_info()) # liangcheng xxx is 83 years old.

class Person:
    def __init__(self, firstname='liang',lastname='cheng',age=25,country='china',city='xxx') -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city 
        self.skills = []
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'
    
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('javascript')

p2 = Person('liang','cheng',230,'china','xxxx')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# liang cheng is 25 years old.
# liang cheng is 230 years old.
# ['HTML', 'CSS', 'javascript']
# []

class Student(Person):
    pass

s1 = Student('zhang','san',22,'china','beijing')
s2 = Student('li','si',32,'china','nanjing')
print(s1.person_info()) # zhang san is 22 years old.

s1.add_skill('nodejs')
s1.add_skill('c++')
s1.add_skill('c#')
print(s1.skills) # ['nodejs', 'c++', 'c#']

print(s2.person_info()) # li si is 32 years old.
s2.add_skill('11111')
s2.add_skill('22222')
s2.add_skill('33333')
print(s2.skills) # ['11111', '22222', '33333']

class Student_one(Person):
    def __init__(self, firstname='liang', lastname='cheng', age=25, country='china', city='xxx', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city) 
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {self.gender} live in {self.country} {self.city}' 
    
s1 = Student_one('zhang','san',22,'china','beijing','female')
s2 = Student_one('li','si',32,'china','nanjing','male')
print(s1.person_info()) # zhang san is 22 years old. female live in china beijing
s1.add_skill('nodejs')
s1.add_skill('c++')
s1.add_skill('c#')
print(s1.skills)

print(s2.person_info()) # li si is 32 years old.
s2.add_skill('11111')
s2.add_skill('22222')
s2.add_skill('33333')
print(s2.skills) # ['11111', '22222', '33333']