使用wps的xlsx表格，方便的配置游戏数据，
在一定格式下，使用这个工具可以很方便的导出为json文件！

通过看 工具帮助文档 应该能让你大致了解这个工具，
基础配置文件夹中也有一些模板，可以康康大致是咋配的。

ConfigLoadSystem.cs是一个在godot中使用的（你也可以改成Unity的，看你），用于读取json数据的类
使用了Newtonsoft.Json，所以你的项目还得下载它

读取首先读取的是基础配置工具目录下的file_name.json文件，
file_name的json中每个表都有三个字段file_name,file_path,key_list

其中file_path应该是在你的项目中使用的路径，因此这个路径需要你修改！
修改基础配置工具路径下的path.txt文件即可

注意导出类型啥的都是可以拓展的
当然,需要你有一点点python知识,
仿照TypeConversion.py这个文件中的BaseType字典，加上自己想要加上的类型，
写上转换的函数即可，记得这边拓展了，读取的地方也得拓展哈！

目前可以导出的类型包括：
常规类型
INT  BOOL  SHORT  UINT64 FLOAT STR  
<INT>  <BOOL>  <SHORT>  <UINT64> <FLOAT> <STR>  
(INT)  (BOOL)  (SHORT)  (UINT64) (FLOAT) (STR)  
<(INT>  <(BOOL)>  <(SHORT)>  <(UINT64)> <(FLOAT)> <(STR)>  
特殊类型：
POINT   一个坐标  转换为godot中的Vector2
LANG   语言id   看你如何使用，可以作为语言配置的id，这个我这边就不给使用方式了
PNG   新增的导出数据类型（在数据中表现是一个图片的相对路径字符串），必须是wps的xlsx文件中的单元格图片（浮动图片读取简单但是没法和格子匹配）
图片导出时，会将wps的xlsx文件中的单元格图片导出，放置在 基础配置工具/images文件夹下