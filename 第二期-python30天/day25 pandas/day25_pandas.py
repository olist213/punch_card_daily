#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :day25_pandas.py
@说明    :
@时间    :2021/09/28 14:42:14
@作者    :liangcheng
@版本    :1.0
'''

import pandas as pd
import numpy as np

nums = [1,2,3,4,5]
s = pd.Series(nums)
print(s)

# 从字典创建 Pandas 系列

dct = {'name':'liang','country':'china','city':'xxx'}

s = pd.Series(dct)
print(s)

# 使用 Linspace 创建 Pandas 系列

s = pd.Series(np.linspace(5, 20, 10))
print(s)




