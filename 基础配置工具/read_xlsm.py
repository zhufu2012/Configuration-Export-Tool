import pandas as pd
import openpyxl
import zipfile
import os
import xml.etree.ElementTree as ET
import openpyxl

output_directory = './基础配置工具/images'  # 保存的图片目录
##读取txt文件内数据
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

##读取xlsx文件的所有数据,包括图片数据
def read_text_all(path):
    xls = pd.ExcelFile(path)
    table_names = xls.sheet_names  # 获取所有表名
    result_dict = {}
    image_path_list = []
    for table_name in table_names:
        ds = pd.read_excel(xls, sheet_name=table_name)  # 逐个读取表格
        result_list = []
        for index, row_list in ds.iterrows():  # 遍历每一行数据
            result = []
            result.append(index)
            for i, row in enumerate(row_list):
                if index == 2 and row == "PNG":  ##导出项是特殊的，单元格中图片
                    export_type = result_list[0][i + 1]
                    if str(export_type) == "1" or str(export_type) == "1.0" or str(export_type) == "2" or str(
                            export_type) == "2.0" or str(export_type) == "3" or str(export_type) == "3.0":  ##确保是可导出的行
                        image_path_list.append(path)
                result.append(row)
            result_list.append(result)
        result_dict[table_name] = result_list
    xls.close()
    return result_dict, image_path_list


def read_excel_data(filename_path):
    # 加载 Excel 文件
    workbook = openpyxl.load_workbook(filename_path, data_only=False)
    sheet = workbook.active
    image_list = []
    # 遍历数据和公式
    data = []  # data就是文本信息
    for row in sheet.iter_rows(min_row=1, values_only=False):
        row_data = []
        for cell in row:
            if cell.value and isinstance(cell.value, str) and '=_xlfn.DISPIMG(' in cell.value:
                # 提取嵌入的图片 ID
                formula = cell.value
                start = formula.find('"') + 1
                end = formula.find('"', start)
                image_id = formula[start:end]
                row_data.append(f"{image_id}")
                image_list.append(image_id)
                # print(image_id)
            else:
                # 其他数据直接添加
                row_data.append(cell.value)
        data.append(row_data)
    return data, image_list


def get_xml_id_image_map(xlsx_file_path):
    # 打开 XLSX 文件
    with zipfile.ZipFile(xlsx_file_path, 'r') as zfile:
        # 直接读取 XML 文件内容
        with zfile.open('xl/cellimages.xml') as file:
            xml_content = file.read()
        with zfile.open('xl/_rels/cellimages.xml.rels') as file:
            relxml_content = file.read()

    # 将读取的内容转换为 XML 树
    root = ET.fromstring(xml_content)

    # 初始化映射字典
    name_to_embed_map = {}

    # 命名空间
    namespaces = {
        'xdr': 'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }

    # 遍历所有 pic 元素
    for pic in root.findall('.//xdr:pic', namespaces=namespaces):
        name = pic.find('.//xdr:cNvPr', namespaces=namespaces).attrib['name']
        embed = pic.find('.//a:blip', namespaces=namespaces).attrib[
            '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed']
        name_to_embed_map[name] = embed

    # 打印结果
    # print(name_to_embed_map)

    root1 = ET.fromstring(relxml_content)

    # 命名空间字典，根据 XML 中定义的命名空间进行设置
    namespaces = {'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}

    # 创建 ID 和 Target 的映射
    id_target_map = {child.attrib['Id']: child.attrib.get('Target', 'No Target Found') for child in
                     root1.findall('.//r:Relationship', namespaces=namespaces)}

    # print(id_target_map)

    # 使用字典推导构建新的映射表
    name_to_target_map = {name: id_target_map[embed] for name, embed in name_to_embed_map.items() if
                          embed in id_target_map}
    return name_to_target_map


##
def output_id_image(xlsx_file_path):
    print(f"路径{xlsx_file_path} ,包含单元格图片，导出中！")
    data, image_list = read_excel_data(xlsx_file_path)
    name_to_target_map = get_xml_id_image_map(xlsx_file_path)
    # 构建id_image_对
    new_map = {key: name_to_target_map.get(key) for key in image_list if key in name_to_target_map}
    # 打开xlsx文件（即Zip文件）
    with zipfile.ZipFile(xlsx_file_path, 'r') as zfile:
        for key, image_path in new_map.items():
            # 构建实际的图片路径
            actual_image_path = f'xl/{image_path}'  # 假设图片在'xl/media/'目录下
            if actual_image_path in zfile.namelist():
                # 读取图片内容
                with zfile.open(actual_image_path) as image_file:
                    image_content = image_file.read()
                    # 保存图片到新的文件夹下面，使用key作为文件名
                    new_file_path = os.path.join(output_directory, f"{key}.png")
                    with open(new_file_path, 'wb') as new_file:
                        new_file.write(image_content)
            else:
                print(f"xlsx内部路径： {actual_image_path} 没找到，未导出图片{image_path} ,相关数据{key} ")
