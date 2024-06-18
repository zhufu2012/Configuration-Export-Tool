@echo off 
REM 该脚本用于复制语言配置到对应目录
chcp 65001
echo 复制  基础配置  到游戏导出目录，策划测试用?
pause


del /s /Q "..\导出版本\Remnant Afterglow\data\config\data\"
copy ".\基础配置工具\file_name.json" "..\导出版本\Remnant Afterglow\data\config\"
copy ".\基础配置工具\data\*" "..\导出版本\Remnant Afterglow\data\config\data\"
copy ".\基础配置工具\images\*" "..\导出版本\Remnant Afterglow\data\config\images\"
echo 复制语言配置到对应目录成功
pause