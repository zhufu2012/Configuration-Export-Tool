import json
import read_xlsm
import os
import TypeConversion


##检测字典的键中，是否有对应target_key
def check_key_exist(dict_list, target_key):
    for dictionary in dict_list:
        if target_key in dictionary:
            return True
    return False


##删除对应文件夹下所有文件
def del_file(path):
    if not os.listdir(path):
        print('目录已为空！')
    else:
        for i in os.listdir(path):
            path_file = os.path.join(path, i)  # 取文件绝对路径
            print("删除基础配置：" + path_file)
            if os.path.isfile(path_file):
                os.remove(path_file)
            else:
                del_file(path_file)
                shutil.rmtree(path_file)


def number_to_column_name(n):
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result

def data_conver(pathlist):
    data_dict = {}  ##所有配置表的数据
    data_key_dict = {}  ##所有配置表的字段数据
    for file_path in pathlist:  ##对每一个配置文件进行处理
        if file_path.startswith("~$"):
            continue
        if file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            pass
        else:
            continue
        dicts = read_xlsm.read_text_all(Define_path + r"./基础配置/" + file_path)
        for table_name, item_list in dicts.items():  ##配置文件的一个子表
            if not table_name.startswith("cfg_"):
                continue
            sub_table_name = table_name
            if table_name.find("_") != table_name.rfind("_"):
                sub_table_name = table_name[:table_name.rfind("_")]
            if check_key_exist(data_dict, sub_table_name):
                print(f"导出失败！   有出现重复的子表，请确保子表名称不会重复！ 该表暂不导出 表名:{table_name}，错误码:5")
                return None
            key_list = ["KEY_INDEX"]  ##键列表
            if (1 in item_list[0][2:]) or ("1" in item_list[0][2:]):
                pass
            else:  ##没有主键
                print(
                    f"导出失败！   配置文件:{file_path}  子表：{table_name}  没有主键，，请增加一个导出类型1的主键字段，错误码:1")
                return None

            if (3 in item_list[0][2:]) or ("3" in item_list[0][2:]):
                pass
            else:  ##没有最后字段
                print(
                    f"导出失败！   配置文件:{file_path}  子表：{table_name}  没有最后导出字段，请增加一个导出类型3的最后字段，错误码:2")
                return None

            export_list = []  ##导出哪些行
            export_key_list = []  ##导出哪些主键行
            col = 2  ##键的数量
            for is_export in item_list[0][2:]:
                if str(is_export) == "0" or str(is_export) == "0.0":
                    col = col + 1
                    continue
                if str(is_export) == "1":
                    export_list.append(col)
                    export_key_list.append(col)
                    col = col + 1
                    continue
                if str(is_export) == "2":
                    export_list.append(col)
                    col = col + 1
                    continue
                if str(is_export) == "3":
                    export_list.append(col)
                    col = col - 1
                    break
                print(
                    f"导出失败！   配置文件:{file_path}  子表：{table_name}  第{number_to_column_name(col)}列 值为{is_export} 导出类型输入错误，导出类型只有1，2，3三种类型！，错误码:3")
                return None
            for key in item_list[1][2:]:  ##遍历主键
                if key in key_list:  ##在里面
                    print(
                        f"导出失败！   配置文件:{file_path}  子表：{table_name} 键：{key}  出现重复，相关数据{key_list}，错误码:4")
                    return None
                else:  ##不在里面
                    key_list.append(key)
            num = 5
            data_list = []
            for item in item_list[3:]:
                is_end, key_dict_list = row_conver(file_path, table_name, num, item, item_list[2], export_key_list,
                                                   export_list,
                                                   key_list)
                if key_dict_list is None:
                    print(
                        f"导出失败！   ")
                    return None
                num += 1
                if key_dict_list is not None:
                    # print(key_dict_list)
                    data_list.append(key_dict_list)
                if is_end:  # 是否遇到2了
                    break
            # print(data_list)
            json_text = json.dumps(data_list, indent=4, ensure_ascii=False)
            data_dict[sub_table_name] = json_text
            key_dict = TypeConversion.Type_Conversion(export_list, key_list, item_list[2][2:])
            data_key_dict[sub_table_name] = TypeConversion.Type_Conversion(export_list, key_list, item_list[2][2:])
    if data_dict is None:
        print(f"导出失败！   没有配置可导出！错误码:6")
        return None
    else:
        return (data_dict, data_key_dict)


# 对一行数据进行组装
def row_conver(file_path, table_name, num, item, type_list, export_key_list, export_list, key_list):
    key_index = "" + str(num - 5)
    key_dict = {}
    if str(item[1]) == "1" or str(item[1]) == "2":
        pass
    else:
        print(
            f"导出失败！   配置文件:{file_path}  子表：{table_name} 第{num}行,没有导出类型 或者 导出类型不为1或者2!错误码:7")
        return False, None
    for export_val1 in export_key_list:
        key_index = key_index + "_" + str(item[export_val1])
    key_dict["KEY_INDEX"] = key_index
    for export_val2 in export_list:
        Data = TypeConversion.TO_DATA(file_path, table_name, export_val2, num, type_list[export_val2],
                                      item[export_val2])
        if Data is not None:
            key_dict[key_list[export_val2 - 1]] = Data
        else:
            print("导出失败！错误码：8")
            return False, None
    return str(item[1]) == "2", key_dict

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

##Define_path = r"."
Define_path = r""
export_path = read_file("./基础配置工具/path.txt")
pathlist = os.listdir(Define_path + r"./基础配置")
json_dict = data_conver(pathlist)
if json_dict is not None and json_dict != ({}, {}):
    (jsondata_dict, keydata_dict) = json_dict
    languages_table_name = []
    del_file(Define_path + "./基础配置工具/data/")  ##删除原基础配置
    for table_name, jsonstr in jsondata_dict.items():
        # 打开文件进行写入，如果文件不存在则创建文件
        with open(Define_path + "./基础配置工具/data/" + table_name + '.json', 'w', encoding='utf-8') as file:
            file.write(jsonstr)
        languages_table_name.append({"file_name": table_name,
                                     "file_path": export_path + table_name + '.json',
                                     "key_list": keydata_dict[table_name]})
        print(table_name + " 已重新导出！")

    ##生成基础配置文件
    languages_table_name_text = json.dumps({"cfg_files": languages_table_name}, indent=4, ensure_ascii=False)
    with open(Define_path + "./基础配置工具/file_name.json", 'w', encoding='utf-8') as file:
        file.write(languages_table_name_text)
else:
    print("导出失败！   ")
