# day 23 Virtual Environment



![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210927130528054.png)

---

## 设置虚拟环境

为了启动项目，最好有一个虚拟环境。虚拟环境可以帮助我们创建一个隔离的或独立的环境。这将帮助我们避免项目间的依赖性冲突。如果你在你的终端上写`pip freeze`，你会看到你的电脑上所有安装的软件包。如果我们使用virtualenv，我们将只访问特定于该项目的软件包。打开你的终端，安装virtualenv。

语法：

```python
pip install virtualenv
```

首先创建一个文件夹flask_project。

在安装了virtualenv包后，进入项目文件夹，通过下面的命令创建虚拟环境。

mac/linux：

```python
virtualenv venv
```

windows

```python
python -m venv venv
```

我更喜欢把新的项目称为venv，但也可以自由选择不同的名称。让我们用ls（或windows命令提示符下的dir）来检查venv是否已经创建。

> 激活虚拟环境

mac/linux:

```python
source venv/bin/activate
```

powershell:

```python
venv\Scripts\activate
```

git bash:

```python
venv\Scripts\. activate
```

在你写完激活命令后，你的项目目录将以venv开头。请看下面的例子。

```bash
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

现在，让我们通过写`pip freeze`来检查这个项目中的可用软件包。你将不会看到任何软件包。我们要做一个小型的flask项目，所以让我们在这个项目中安装`flask`包。

```bash
pip install Flask
```

现在，让我们编写 pip freeze 来查看项目中已安装软件包的列表。

```python
$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

当你完成后，你应该用`deactivate`来停用活动项目。

> ⚠️：与flask一起工作的必要模块已经安装。现在，你的项目目录已经为flask项目做好了准备。你应该在你的.gitignore文件中加入venv，而不是把它推送到github。

