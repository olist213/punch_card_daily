# day19 文件处理

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210921160301747.png)

---

到目前为止，我们已经看到了不同的 Python 数据类型。我们通常用不同的文件格式来存储我们的数据。除了处理文件，我们还将在本节中看到不同的文件格式(.txt, .json, .xml, .csv, .tsv, .excel) 。首先，让我们熟悉一下用常见的文件格式（.txt）处理文件。

文件处理是编程的一个重要部分，它允许我们创建、读取、更新和删除文件。在Python中，我们使用open()内置函数来处理数据。

语法：

```python
open('filename', mode) # mode(r,a,w,x,t,b)
```

- r:read - 默认值，打开一个文件以便阅读，如果文件不存在，则返回错误。
- a:append - 打开一个文件进行内容追加，如果不存在，则创建文件。
- w:write - 打开一个文件以便写入，如果不存在，则创建文件。
- x:create - 创建文件，如果文件存在则返回错误。
- t:text - 默认值，文本模式。
- b:binary - 二进制模式（如：图片等）

## 打开文件以便阅读

打开的默认模式是读取，所以就不需要指定r或者rt。在此文件的file目录下，有相关的样例文件。

语法：

```python
f = open('./file/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./file/reading_file_example.txt' mode='r' encoding='UTF-8'>
# 返回一个IO句柄
```

上述案例中，将打开的文件赋给f，打印出f，f也就是返回的IO句柄，代表了当前打开的文件。文件打开后，还需要使用read()、readline()、readlines()等方法去读取文件中的内容。打开的文件也需要使用close()去关闭。

代码：

```python
f = open('./file/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

不要打印所有的文本，让我们打印文本文件的前10个字符。

代码：

```python
f = open('./file/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# output

<class 'str'>






<!DO
```

- readline():只读取第一行

代码：

```python
f = open('./file/reading_file_example.txt')
txt = f.readline()
print(type(txt))
print(txt)
f.close()

# output
# <class 'str'>
# <!DOCTYPE html>
```

- readlines():逐行读取所有的文本，并返回一个行的列表

代码：

```python
f = open('./file/reading_file_example.txt')
txt = f.readlines()
print(type(txt))
print(txt)
f.close()

# # output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

另一种方法是使用splitlines()来获得所有行的列表。

代码：

```python
f = open('./file/reading_file_example.txt')
txt = f.read().splitlines()
print(type(txt))
print(txt)
f.close()

# # output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

在打开文件后，应该记得关闭它，有一种新的打开文件的方法，使用with，自己关闭文件。

代码：

```python
with open('./file/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

## 打开文件进行写入和更新

要写到一个现有的文件，我们必须向open()函数添加一个模式作为参数。

- a - append - 将追加到文件的末尾，如果文件没有追加，则创建一个新文件。
- w - write - 将覆盖任何现有的内容，如果文件不存在，它将创建。

让我们把一些文本附加到我们所读的文件中。

代码：

```python
with open('./file/reading_file_example.txt','a') as f:
    f.write("hahahahahah")
```

下面的代码则会覆盖原文件的内容，如果文件不存在，则创建新文件：

代码：

```python
with open('./file/writing_file_example.txt','w') as f:
    f.write("hahahahahah")
```

## 删除文件

我们在上一节中已经看到了如何使用os模块创建和删除一个目录。现在，如果我们想删除一个文件，我们也要使用os模块。

代码：

```python
import os

os.remove('./file/examples.txt')
```

如果想删除的文件不存在，那么remove将报错，最好配合下面的方法使用：

代码：

```python
import os 

if os.path.exists('./file/example.txt'):
  	os.remove('./file/example.txt')
else:
  	print('该文件不存在！')
```

## 文件类型

### txt文件扩展名

常见的文本文件格式，用来处理文本文件。

### json文件扩展名

JSON是JavaScript Object Notation的缩写。实际上，它是一个字符串化的JavaScript对象或Python字典。

代码：

```python
# 字典
person_dct = {
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}

## json
person_json = "{'name':'liangcheng', 'country':'china', 'city':'xxx', 'skills':['js','python','go']}"

## 多行格式
person_json= '''{
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}'''
```

### 将json格式转成字典

需要导入json模块，然后使用loads方法。

代码：

```python
person_json= '''{
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_json)
print(person_dct['name'])

# output

<type 'dict'>
{
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}
liangcheng
```

### 将字典转成python

使用json模块的dumps方法。

代码：

```python
person_dct = {
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}

person_json = json.dumps(person_dct)
print(type(person_json))
print(person_json)

# <class 'str'>
# {"name": "liangcheng", "country": "china", "city": "xxx", "skills": ["js", "python", "go"]}
```

### 保存为json文件

也可以将数据保存为json文件，使用json.dump()方法，接收的参数可以是字典、输出文件、ensure_ascii和锁进。

代码：

```python
person_dct = {
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}

with open('./file/json_123.json','w',encoding='utf-8') as f:
    json.dump(person_json, f, ensure_ascii=False,indent=4)
```

在上面的代码中，我们使用了编码和缩进。缩进使json文件易于阅读。

### csv扩展名的文件

CSV是逗号分隔值的意思（comma separated values）。CSV是一种简单的文件格式，用于存储表格数据，如电子表格或数据库。CSV是数据科学中一种非常常见的数据格式。

语法：

```python
"name","country","city","skills"
"liangcheng","china","xxx","python"
```

代码：

```python
import csv

with open('./file/222.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1

    print(f'Number of lines: {line_count}')

# Column names are :name, country, city, skills
# 	liangcheng is a teachers. He lives in china, xxx.
# Number of lines: 2
```

### xlsx后缀

为了读取excel文件，我们需要安装xlrd包。

```bash
pip3 install xlrd
```

语法：

```python
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(execl_book.sheet_names)
```



### xml后缀

XML是另一种结构化数据格式，看起来像HTML。在XML中，标签没有被预先定义。第一行是一个XML声明。person标签是XML的根，这个person有一个性别属性。

代码：

```python
import xml.etree.ElementTree as ET
tree = ET.parse('./file/xml_example.xml')
root = tree.getroot()
print('root tag:',root.tag)
print('attribute:',root.attrib)

for child in root:
    print('field', child.tag)

# root tag: person
# attribute: {'gender': 'male'}
# field name
# field country
# field city
# field skills
```

# 练习

