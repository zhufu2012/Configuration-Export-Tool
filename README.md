使用excel表格方便的配置游戏数据，一定格式下，使用这个工具可以很方便的导出为json文件

看工具帮助文档能让你大致了解这个工具，
基础配置文件夹中也有一些模板，可以康康大致是咋配的。

ConfigLoadSystem.cs是一个在godot中使用的，用于读取json数据的类
读取首先读取的是基础配置工具目录下的file_name.json文件，
file_name的json中每个表都有三个字段file_name,file_path,key_list

其中file_path应该是在你的项目中使用的路径，因此这个路径需要你修改！
修改基础配置工具路径下的path.txt文件即可

注意导出类型啥的都是可以拓展的
当然,需要你有一点点python知识,
仿照TypeConversion.py这个文件中的BaseType字典，加上自己想要加上的类型，
写上转换的函数即可，记得这边拓展了，读取的地方也得拓展哈！
