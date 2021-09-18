# day16 date time

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210917191325391.png)

python用datetime模块来处理日期和时间。

```python
>>> import datetime
>>> print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

使用 dir 或 help 内置命令可以知道某个模块中的可用功能。如您所见，datetime 模块中有很多函数，但我们将重点介绍 date、datetime、time 和 timedelta。让我们一一看看。

## 获取日期时间信息

代码：

```python
from datetime import datetime

now = datetime.now()
print(now) # 2021-09-17 19:17:22.071855

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(day, month, year, hour, minute, second)
print('timestamp:', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
```

timestamp(时间戳)或Unix timestamp(时间戳)是指从1970年1月1日UTC开始经过的秒数。

## 使用strftime对日期输出进行格式化

代码：

```python
from datetime import datetime

new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')
```

使用strftime方法对日期时间进行格式化，相关文档可以在[这里](https://strftime.org/)找到。

代码：

```python
from datetime import datetime

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t) # time: 19:30:03

# mm/dd/YY H:M:S格式
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time_one:", time_one) # time_one: 09/17/2021, 19:30:03

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time_two:", time_two) # time_two: 17/09/2021, 19:30:03
```

这里是我们用来格式化时间的所有strftime符号。本模块所有格式的一个例子。

![strftime](https://raw.githubusercontent.com/olist213/olistimg/master/upic/strftime.png)

## 使用strptime将字符串转换成时间
代码：

```python
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =:", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# output
# date_string =: 5 December, 2019
# date_object = 2019-12-05 00:00:00
```

## date

datetime中的date模块。

代码：

```python
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today()) # Current date: 2021-09-17

today = date.today()
print('Current year:', today.year) # 2021
print('Current month:', today.month) # 9
print('Current day:', today.day) # 17
```

## Time Objects to Represent Time

> Time Objects to Represent Time

代码：

```python
from datetime import time

a = time()
print("a =", a) # a = 00:00:00

b = time(10, 30, 50)
print("b =", b) # b = 10:30:50 

c = time(hour=10, minute=30, second=50)
print("c =", c)

d = time(10, 30, 50, 200555)
print("d =", d)

# output
# a = 00:00:00
# b = 10:30:50
# c = 10:30:50
# d = 10:30:50.200555
```

##  利用两个时间点之间的差异

代码：

```python
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today

# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=20)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=20)
diff = t2 -t1

# Time left for new year:  26 days, 23:01:00
print('Time left for new year: ', diff)
```

## *timedelata*

> timedelata

代码：

```python
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=4, minutes=3, seconds=20)
t3 = t1 - t2
print(t3) # 86 days, 23:57:00
```

# 练习

