@echo off 
REM 该脚本用于复制语言配置到对应目录
chcp 65001
echo 复制  语言配置  到游戏导出目录，策划测试用?
pause


del /s /Q "..\导出版本\Remnant Afterglow\data\language\data\"
copy ".\语言导出工具\file_name.json" "..\导出版本\Remnant Afterglow\data\language\"
copy ".\语言导出工具\data\*" "..\导出版本\Remnant Afterglow\data\language\data\"
echo 复制语言配置到对应目录成功
pause