# coding: utf-8

import json
from typing import DefaultDict

# json
# 字典
person_dct = {
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}

## json
# person_json = "{'name':'liangcheng', 'country':'china', 'city':'xxx', 'skills':['js','python','go']}"

# person_json = '''{
#     'name':'liangcheng', 
#     'country':'china', 
#     'city':'xxx', 
#     'skills':['js','python','go']
# }'''

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

person_dct = {
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}

with open('./file/json_123.json','w',encoding='utf-8') as f:
    json.dump(person_json, f, ensure_ascii=False,indent=4)


## csv

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

# xml

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