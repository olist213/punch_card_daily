# day24 统计学（statistics）

![30DaysOfPython](https://raw.githubusercontent.com/olist213/olistimg/master/upic/30DaysOfPython_banner3@2x-20210928091459177.png)

----

## 用于统计学的python

### 统计学

统计学是研究数据的收集、组织、显示、分析、解释和表述的学科。统计学是数学的一个分支，被推荐为数据科学和机器学习的先决条件。

统计学是一个非常广泛的领域，但我们将在本节中只关注最相关的部分。

### 数据

**什么是数据？**数据是为某种目的（通常是分析）而收集和翻译的任何字符集。它可以是任何字符，包括文字和数字、图片、声音或视频。如果不把数据放在一个背景中，它对人类或计算机来说就没有任何意义。为了从数据中获得意义，我们需要使用不同的工具来处理数据。

数据分析、数据科学或机器学习的工作流程从数据开始。数据可以由一些数据源提供，也可以由其创建。有结构化和非结构化的数据。

数据可以以小格式或大格式出现。我们将得到的大部分数据类型在**文件处理部分**已经涉及。

## statistics模块

Python statistics模块提供了计算数值数据的数学统计的函数。该模块并不打算成为第三方库（如NumPy、SciPy）或针对专业统计人员的专有全功能统计包（如Minitab、SAS和Matlab）的竞争对手。

它针对的是图形和科学计算器的水平。

## NumPy

在第一节中，我们将Python定义为一种伟大的通用编程语言，但在其他流行的库（numpy, scipy, matplotlib, pandas等）的帮助下，它成为一个强大的科学计算环境。

NumPy是Python中科学计算的核心库。它提供了一个高性能的多维数组对象，以及处理数组的工具。

到目前为止，我们一直在使用vscode，但从现在开始，我建议使用Jupyter笔记本。为了访问jupyter笔记本，让我们安装[anaconda](https://www.anaconda.com/)。如果你使用anaconda，大部分常用的软件包都包括在内，如果你安装了anaconda，你就不需要安装软件包。

语法：

```python
pip install numpy
```

## import NumPy

