# day22 web scraping

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210926192335391.png)

---

## 什么是web scraping？

互联网上有大量的数据，可用于不同的目的，为了收集这些数据，我们需要知道如何从一个网站上爬取数据。

网页爬取是从网站上提取和收集数据并存储在本地机器或着数据库的过程中。

在本节中，我们将使用beautifulsoup和request包来爬取数据。所使用的包的版本是beautifulsoup4。

要爬取数据，你需要requests、beautifoulSoup4和一个网站。

语法：

```python
pip installl  requests
pip install beautifulsoup4
```

要从网站上爬取数据，需要对HTML标签和CSS选择器有基本了解。我们使用HTML标签、class、ID来定位网站的内容。让我们导入requets和BeautifulSoup模块。

代码：

```python
import requests
from bs4 import BeautifulSoup
```

让我们为要抓取的网站声明`url`变量。

代码：

```python
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

status = response.status_code
print(status) # 200
```

使用beautifulSoup解析页面内容。

代码：

```python
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, 'html.parser')

print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpading':'3'})

table = tables[0]

for td in table.find('tf').find_all('td')
    print(td.text)
```

如果你运行这段代码，你可以看到提取工作已经完成了一半。你可以继续做下去，因为它是练习一的一部分。作为参考，请查看[beautifulsoup文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)。













