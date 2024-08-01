""" toolkit_config.\

Project configuration file
"""
import os

PRJDIR = r'C:\Users\Admin\Desktop\project2 ZU'
DATADIR = os.path.join(PRJDIR, 'data')

"""在实际项目中，为了方便管理项目的文件和目录，有时会定义一个变量来存储项目的根目录路径，通常命名为 prjdir 或者 project_dir 等。通过使用这样的变量，可以使得代码更加清晰易读，并且便于在需要时进行修改。

例如，在一个 Flask Web 应用项目中，可以定义一个 prjdir 变量来存储项目的根目录路径：

python
Copy code
import os

prjdir = os.path.abspath(os.path.dirname(__file__))
在这个例子中，prjdir 被赋值为当前脚本文件所在的目录的绝对路径，作为项目的根目录。这样，在项目的其他地方可以使用 prjdir 来引用项目根目录，从而更方便地进行文件和目录的操作"""
