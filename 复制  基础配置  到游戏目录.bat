@echo off 
REM 该脚本用于复制语言配置到对应目录
chcp 65001
echo 复制   基础配置   到游戏目录?
pause


del /s /Q "..\Remnant Afterglow\data\config\data\"
copy ".\基础配置工具\file_name.json" "..\Remnant Afterglow\data\config\"
copy ".\基础配置工具\data\*" "..\Remnant Afterglow\data\config\data\"
echo 复制语言配置到对应目录成功
pause