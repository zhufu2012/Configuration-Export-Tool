@echo off 
REM 该脚本用于复制语言配置到对应目录
chcp 65001
echo 复制  语言配置  到游戏开发目录，程序开发用?
pause


del /s /Q "..\Remnant Afterglow\data\language\data\"
copy ".\语言导出工具\file_name.json" "..\Remnant Afterglow\data\language\"
copy ".\语言导出工具\data\*" "..\Remnant Afterglow\data\language\data\"
echo 复制语言配置到对应目录成功
pause