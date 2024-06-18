import read_xlsm

export_iamge_path = read_xlsm.read_file("./基础配置工具/项目配置图片路径.txt")

def number_to_column_name(n):
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result

##转换为INT
def TO_INT(file_path, table_name, Col_x, Col_y, variable):
    if isinstance(variable, int):
        return variable
    else:
        try:
            converted_variable = int(variable)
            return converted_variable
        except ValueError:
            print(
                f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为INT 时出现错误！")
            return None


##转换为BOOL
def TO_BOOL(file_path, table_name, Col_x, Col_y, variable):
    if isinstance(variable, bool):
        return variable
    else:
        try:
            if variable.lower() == 'true' or variable.lower() == 'TRUE':
                return True
            elif variable.lower() == 'false'  or variable.lower() == 'FALSE':
                return False
        except ValueError:
            print(
                f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为BOOL 时出现错误！")
            return None


##转换为BYTE
def TO_BYTE(file_path, table_name, Col_x, Col_y, variable):
    if isinstance(variable, bytes):
        return variable
    else:
        try:
            converted_variable = int(variable).to_bytes(1, byteorder='big')
            return converted_variable
        except ValueError:
            print(
                f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为BYTE 时出现错误！")
            return None


def TO_UINT64(file_path, table_name, Col_x, Col_y, variable):
    if isinstance(variable, int):
        return variable
    else:
        try:
            converted_variable = int(variable)
            return converted_variable
        except ValueError:
            print(
                f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为UINT64 时出现错误！")
            return None


def TO_FLOAT(file_path, table_name, Col_x, Col_y, variable):
    try:
        converted_variable = float(variable)
        return converted_variable
    except ValueError:
        print(f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为FLOAT 时出现错误！")
        return None


def TO_STR(file_path, table_name, Col_x, Col_y, variable):
    return str(variable)


def TO_BOOL_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with boolean values separated by '|'
        return [True if (val.strip().lower() == 'true' or val.strip().lower() == 'TRUE') else False for val in str(variable).split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为BOOL列表时出现错误：{e}")
        return None


def TO_BYTE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with byte values separated by '|'
        return [int(val.strip()).to_bytes(1, byteorder='big') for val in str(variable).split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为BYTE列表时出现错误：{e}")
        return None


def TO_INT_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a list of integers represented as strings
        return [int(val.strip()) for val in str(variable).split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为INT列表时出现错误：{e}")
        return None


def TO_SHORT_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a list of integers represented as strings
        return [int(val.strip()) for val in variable.split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为SHORT列表时出现错误：{e}")
        return None


def TO_UINT64_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a list of unsigned integers represented as strings
        return [int(val.strip()) for val in variable.split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为UINT64列表时出现错误：{e}")
        return None


def TO_FLOAT_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a list of floats represented as strings
        return [float(val.strip()) for val in variable.split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为FLOAT列表时出现错误：{e}")
        return None


def TO_STR_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a list of strings
        return [str(val) for val in variable.split('|')]
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为STR列表时出现错误：{e}")
        return None


def TO_BOOL_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of boolean values
        values = variable.strip('()').split(',')
        return tuple(True if (val.strip().lower() == 'true' or val.strip().lower() == 'TRUE') else False for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为BOOL元组时出现错误：{e}")
        return None


def TO_BYTE_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of byte values
        values = variable.strip('()').split(',')
        return tuple(int(val.strip()).to_bytes(1, byteorder='big') for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为BYTE元组时出现错误：{e}")
        return None


def TO_INT_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of byte values
        values = variable.strip('()').split(',')
        return tuple(int(val.strip()) for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为INT元组时出现错误：{e}")
        return None


def TO_UINT64_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of unsigned integers
        values = variable.strip('()').split(',')
        return tuple(int(val.strip()) for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为UINT64元组时出现错误：{e}")
        return None


def TO_FLOAT_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of floats
        values = variable.strip('()').split(',')
        return tuple(float(val.strip()) for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为FLOAT元组时出现错误：{e}")
        return None


def TO_STR_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of strings
        values = variable.strip('()').split(',')
        return tuple(str(val.strip()) for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为STR元组时出现错误：{e}")
        return None


def TO_BOOL_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of boolean values separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            bool_tuple = tuple(True if (val.strip().lower() == 'true' or val.strip().lower() == 'TRUE') else False for val in values)
            result.append(bool_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(BOOL)>列表时出现错误：{e}")
        return None


def TO_BYTE_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of byte values separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            byte_tuple = tuple(int(val.strip()).to_bytes(1, byteorder='big') for val in values)
            result.append(byte_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(BYTE)>列表时出现错误：{e}")
        return None


def TO_INT_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of integers separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            int_tuple = tuple(int(val.strip()) for val in values)
            result.append(int_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(INT)>列表时出现错误：{e}")
        return None


def TO_UINT64_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of unsigned integers separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            uint64_tuple = tuple(int(val.strip()) for val in values)
            result.append(uint64_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(UINT64)>列表时出现错误：{e}")
        return None


def TO_FLOAT_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of floats separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            float_tuple = tuple(float(val.strip()) for val in values)
            result.append(float_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(FLOAT)>列表时出现错误：{e}")
        return None


def TO_STR_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of strings separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            str_tuple = tuple(str(val.strip()) for val in values)
            result.append(str_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(STR)>列表时出现错误：{e}")
        return None


def TO_SHORT(file_path, table_name, Col_x, Col_y, variable):
    if isinstance(variable, int):
        return variable
    else:
        try:
            converted_variable = int(variable)
            return converted_variable
        except ValueError:
            print(
                f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为SHORT时出现错误！")
            return None


def TO_SHORT_TUPLE(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string representing a tuple of short values
        values = variable.strip('()').split(',')
        return tuple(int(val.strip()) for val in values)
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为SHORT元组时出现错误：{e}")
        return None


def TO_SHORT_TUPLE_LIST(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of short values separated by '|'
        tuples = variable.split('|')
        result = []
        for tup in tuples:
            values = tup.strip('()').split(',')
            short_tuple = tuple(int(val.strip()) for val in values)
            result.append(short_tuple)
        return result
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(SHORT)>列表时出现错误：{e}")
        return None

def TO_PNG(file_path, table_name, Col_x, Col_y, variable):
    try:
        # Assuming variable is a string with tuples of short values separated by '|'
        path1 = variable[variable.find("\"")+1:]
        path2 = path1[:path1.find("\"")]
        return export_iamge_path + path2 + ".png"
    except Exception as e:
        print(
            f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据{variable}转换为<(SHORT)>列表时出现错误：{e}")
        return None

BaseType = {
    'BOOL': (TO_BOOL, True,'bool'),
    ##'BYTE': (TO_BYTE, b'\x00','byte'),
    'SHORT': (TO_SHORT, 0,'short'),
    'INT': (TO_INT, 0,'int'),
    'UINT64': (TO_UINT64, 0,'UInt64'),
    'FLOAT': (TO_FLOAT, 0,'float'),
    'STR': (TO_STR, "",'string'),
    '<BOOL>': (TO_BOOL_LIST, [], 'List<bool>'),
    ##'<BYTE>': (TO_BYTE_LIST, [], 'List<byte>'),
    '<SHORT>': (TO_SHORT_LIST, [], 'List<short>'),
    '<INT>': (TO_INT_LIST, [], 'List<int>'),
    '<UINT64>': (TO_UINT64_LIST, [], 'List<UInt64>'),
    '<FLOAT>': (TO_FLOAT_LIST, [], 'List<float>'),
    '<STR>': (TO_STR_LIST, [], 'List<string>'),
    '(BOOL)': (TO_BOOL_TUPLE, (), 'List<bool>'),
    ##'(BYTE)': (TO_BYTE_TUPLE, (), 'List<byte>'),
    '(SHORT)': (TO_SHORT_TUPLE, (), 'List<short>'),
    '(INT)': (TO_INT_TUPLE, (), 'List<int>'),
    '(UINT64)': (TO_UINT64_TUPLE, (), 'List<UInt64>'),
    '(FLOAT)': (TO_FLOAT_TUPLE, (), 'List<float>'),
    '(STR)': (TO_STR_TUPLE, (), 'List<string>'),
    '<(BOOL)>': (TO_BOOL_TUPLE_LIST, [], 'List<List<bool>>'),
    ##'<(BYTE)>': (TO_BYTE_TUPLE_LIST, [], 'List<List<byte>>'),
    '<(SHORT)>': (TO_SHORT_TUPLE_LIST, [], 'List<List<short>>'),
    '<(INT)>': (TO_INT_TUPLE_LIST, [], 'List<List<int>>'),
    '<(UINT64)>': (TO_UINT64_TUPLE_LIST, [], 'List<List<UInt64>>'),
    '<(FLOAT)>': (TO_FLOAT_TUPLE_LIST, [], 'List<List<float>>'),
    '<(STR)>': (TO_STR_TUPLE_LIST, [], 'List<List<string>>'),
    'PNG': (TO_PNG, [], 'Texture2D'),
    'LANG':(TO_STR,"KeyBase","language_id"),##语言id类型
    '<LANG>':(TO_STR_LIST,[],"<language_id>"), ##语言id列表类型
    'POINT' :(TO_FLOAT_TUPLE, (0,0), 'Vector2'),      ##坐标类型
    '<POINT>' :(TO_FLOAT_TUPLE_LIST, [], 'List<Vector2>')  ##坐标列表类型
}



def TO_DATA(file_path, table_name, Col_x, Col_y, Type, Data):
    try:
        function, default_value,NewType = BaseType.get(Type, (lambda file_path, table_name, Col_x, Col_y, variable: "Invalid", None))
        if Data == "#BASEVALUE":
            return default_value
        else:
            NewData = function(file_path, table_name, Col_x, Col_y, Data)
            return NewData
    except Exception as e:
        print(   f"配置文件:{file_path}  子表：{table_name} 第{Col_y}行，第{number_to_column_name(Col_x)}列 ，数据类型错误！不存在类型{Type}")
        return None


def Type_Conversion(export_list,KeyList , TypeList):
    key_dict = {}
    num = 0
    key_dict["KEY_INDEX"] = "string"
    for export in export_list:
        key_dict[KeyList[export-1]] =BaseType[TypeList[export-2]][2]
    return key_dict

# Data = TO_DATA(1, 1, "INT", "1")
# Data2 = TO_DATA(1, 1, 'BYTE', "0")
# Data3 = TO_DATA(2, 2, 'BOOL', "true")
# Data4 = TO_DATA(2, 2, '<INT>', '1|2')
# Data5 = TO_DATA(2, 2, '<INT>', '1')
# Data6 = TO_DATA(2, 2, '<STR>', 'keysasda')
# Data7 = TO_DATA(2, 2, '(STR)', '(asdasd,asdws)')
# Data8 = TO_DATA(2, 2, '<(INT)>', '(1,100)|(2,200)')
# print(Data)
# print(Data2)
# print(Data3)
# print(Data4)
# print(Data5)
# print(Data6)
# print(Data7)
# print(Data8)
