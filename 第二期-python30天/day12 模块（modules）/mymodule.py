#coding: utf-8
# mymodule.py文件
def generate_full_name(firstname, lastname):
  	return firstname + ' ' + lastname


def sum_two_nums(num_one, num_two):
    sum = num_one + num_two
    return sum

# def weight_of_object(mass, gravity = 9.81):
#     weight = str(mass * gravity) + ' N'
#     return weight
gravity = 10


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