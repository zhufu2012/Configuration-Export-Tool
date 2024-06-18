@echo off 
REM 该脚本用于复制语言配置到对应目录
chcp 65001
echo 复制  基础配置  到游戏开发目录，程序开发用?
pause


del /s /Q "..\Remnant Afterglow\data\config\data\"
copy ".\基础配置工具\file_name.json" "..\Remnant Afterglow\data\config\"
copy ".\基础配置工具\data\*" "..\Remnant Afterglow\data\config\data\"
copy ".\基础配置工具\images\*" "..\Remnant Afterglow\data\config\images\"
echo 复制语言配置到对应目录成功
pause