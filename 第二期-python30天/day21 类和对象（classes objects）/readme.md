# day21 classes and objects

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210922160956156.png)

---

python是一门面向对象的编程语言，在python中，所有的东西都是一个对象，有其属性和方法。程序中使用的数字、字符串、列表、字典、元组、集合等都是响应内置类的对象，通过创建类来创建对象，一个类就像一个对象构造器，或者创建对象的“蓝图”，类定义了对象的属性和行为，而对象则代表类。

从这个挑战开始，就在不知不觉中与类和对象打交道，python中的每一个元素都是一个类的对象。让我们检查下是否所有元素都是一个类。

代码：

```python
❯ python3
Python 3.9.5 (default, May  3 2021, 19:12:05) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

## 创建类

要创建一个类，我们需要在关键字class后面加上名称和冒号，类的名称为CamelCase。

语法：

```python
class ClassName:
    code goes here
```

代码：

```python
class Person:
    pass

print(Person) # <class '__main__.Person'>
```

## 创建对象

我们可以通过调用该类来创建一个对象。

代码：

```python
p = Person()
print(p) # <__main__.Person object at 0x104792c40>
```

## 类构造器

在上面的例子中，我们已经从Person类中创建了一个对象，然而，一个没有构造函数的类在实际应用中并不真正有用，让我们使用构造函数来使我们的类更加有用。像`Java`或`JavaScript`中的构造函数一样，`Python`也有一个内置的 `init()`构造函数。`init`构造函数有一个`self`参数，它是对类的当前实例的引用。

代码：

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person('liangcheng')
print(p.name) # liangcheng
print(p) # <__main__.Person object at 0x100f39f40>
```

让我们向构造函数添加更多参数。

代码：

```python
class Person:
    def __init__(self, firstname,lastname,age,country,city) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city 

p = Person('liangcheng', 'xxx', 83, 'china', 'xxx111')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

## 对象方法

对象可以有方法。这些方法是属于对象的函数。

代码：

```python
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
```

## 对象默认方法

有时，你可能想为你的对象方法设置一个默认值，如果我们在构造函数中给出参数的默认值，我们就可以避免在调用或者实例化类时没有参数出现错误的问题，让我们来看看它的样子。

代码：

```python
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
```

## 修改类的默认值的方法

在下面的例子中，人物类，所有的构造函数参数都有默认值。除此之外，我们还有技能参数，我们可以用一个方法来访问它。让我们创建add_skill方法来向技能列表中添加技能。

代码：

```python
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
```

## 继承

使用继承，可以重复使用父类的代码，继承允许我们定义一个继承了父类所有方法和属性的类，父类、超类、基类是一个提供所有方法和属性的类。子类是继承自另一个或父类的类，让我们通过继承人物类来创建一个学生类。

语法：

```python
class Student(Person):
    pass
```

代码：

```python
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
```

我们没有在子类中调用init()构造函数。如果我们没有调用它，那么我们仍然可以访问父类的所有属性。但如果我们调用了构造函数，就可以通过调用super来访问父类的属性。

我们可以为子类添加一个新的方法，也可以通过在子类中创建相同的方法名来覆盖父类的方法。当我们添加init()函数时，子类将不再继承父类的init()函数。

代码：

```python
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
```

我们可以使用super()内置函数或父名称Person来自动继承其父方法和属性。在上面的例子中，我们覆盖了父方法。子方法有一个不同的特点，它可以识别性别是男性还是女性，并分配适当的代词（He/She）。