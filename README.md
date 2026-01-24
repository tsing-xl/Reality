# Reality

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-BSD-yellow.svg)](https://opensource.org/licenses/BSD)

Reality 是一个基于 pyglet, 用于构建简单桌面应用的库。

不要将其用于大型项目中。

# Quick start

Reality 的语法很简单，如下：

```
from Reality import *

inter = Interface()

def hello():
    print('Hello, Reality!')

button = Button(inter, x=450, y=5, width=200, height=30, text='Hello World', command=hello)

inter.runApplication()
```

如果对于 Tkinter 很熟悉的话上手此项目应该会很快。

顺带一提我们使用xy坐标来放置和定位组件，网格什么的实现起来太麻烦了。

目前还需要做的有很多，如优化逻辑，统一接口，修复问题，添加新的功能等等，我暂时只能够做到这些。

# API Reference
```
Reality.interface
Reality.widgets
Reality.composer.widgetcomposer
Reality.handler.widgethandler
Reality.font
Reality.background
```

# Installation

目前还没有上架 PyPI，需要手动下载src中的文件使用。
