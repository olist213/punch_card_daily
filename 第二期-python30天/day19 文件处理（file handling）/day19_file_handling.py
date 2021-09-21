# coding: utf-8

f = open('./file/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./file/reading_file_example.txt' mode='r' encoding='UTF-8'>

# f = open('./file/reading_file_example.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()


# f = open('./file/reading_file_example.txt')
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# readline
f = open('./file/reading_file_example.txt')
txt = f.readline()
print(type(txt))
print(txt)
f.close()

# readlines()
f = open('./file/reading_file_example.txt')
txt = f.readlines()
print(type(txt))
print(txt)
f.close()

# splitlines

f = open('./file/reading_file_example.txt')
txt = f.read().splitlines()
print(type(txt))
print(txt)
f.close()

# with

with open('./file/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# 打开文件进行写入和更新

with open('./file/reading_file_example.txt','a') as f:
    f.write("hahahahahah")

with open('./file/writing_file_example.txt','w') as f:
    f.write("hahahahahah")

# json
# 字典
person_dct = {
    "name":"liangcheng",
    "country":"china",
    "city":"xxx",
    "skills":["js","python","go"]
}

## json
person_json = "{'name':'liangcheng', 'country':'china', 'city':'xxx', 'skills':['js','python','go']}"

person_json = '''{
    'name':'liangcheng', 
    'country':'china', 
    'city':'xxx', 
    'skills':['js','python','go']
}'''

