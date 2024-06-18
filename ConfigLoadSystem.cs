
using GameLog;
using Godot;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using File = System.IO.File;

namespace Project_Core
{
    public class ConfigDict
    {
        public string file_name { get; set; }
        public string file_path { get; set; }
        public Dictionary<string, string> key_list { get; set; }
    }
	
	//file_name文件中的数据
    public class ConfigFiles
    {
        public List<ConfigDict> cfg_files { get; set; }
        public override string ToString()
        {
            string result = "cinfig Files:\n";
            foreach (var file in cfg_files)
            {
                result += "文件名称: " + file.file_name + ", 文件路径: " +
                file.file_path + "\n";
            }
            return result;
        }
    }

    //配置加载器-加载游戏所有配置数据-注释-改成初始化就创建
    public partial class ConfigLoadSystem : Node
    {
        //配置数据
        public static List<ConfigDict> filedata;
        public static Dictionary<string, Dictionary<string, Dictionary<string, object>>> config_dict
            = new Dictionary<string, Dictionary<string, Dictionary<string, object>>>();
        
		
		static ConfigLoadSystem()
		{
			string jsonText = File.ReadAllText("./data/config/file_name.json");
            ConfigFiles file_data = JsonConvert.DeserializeObject<ConfigFiles>(jsonText);
            filedata = file_data.cfg_files;
            List<ForMatStr> format_str_list = new List<ForMatStr>();
            foreach (var cfgFile in filedata)
            {
                string jsonstr = File.ReadAllText(cfgFile.file_path);
                JArray jsonArray = JArray.Parse(jsonstr);
                Dictionary<string, Dictionary<string, object>> innerDict = new Dictionary<string, Dictionary<string, object>>();
                foreach (JObject obj in jsonArray)
                {
                    string keyIndex = obj["KEY_INDEX"].Value<string>();
                    Dictionary<string, object> dataDict = new Dictionary<string, object>();

                    foreach (var key in cfgFile.key_list.Keys)
                    {
                        if (obj.TryGetValue(key, out JToken value))
                        {
                            string type = cfgFile.key_list[key];
                            object convertedValue = ConvertValue(value, type);
							
                            dataDict[key] = convertedValue;
                        }
                    }

                    innerDict[keyIndex] = dataDict;
                }

                config_dict[cfgFile.file_name] = innerDict;
            }
            Log.PrintDict(GetCfgKey("cfg_Enemy", "1_2"));//测试
            Log.PrintDict(GetCfgKey("cfg_Enemy", "0_1"));//测试
		}


        /// <summary>
        /// 读取某配置 所有
        /// </summary>
        /// <param name="fileName">配置名称</param>
        /// <param name="Key">键</param>
        /// <returns></returns>
        public static Dictionary<string, Dictionary<string, object>> GetCfg(string fileName)
        {
            return config_dict.ContainsKey(fileName) ?
            config_dict[fileName] : null;
        }

        /// <summary>
        /// 读取某配置 某一行的数据
        /// </summary>
        /// <param name="fileName">配置名称</param>
        /// <param name="Key">键</param>
        /// <returns></returns>
        public static Dictionary<string, object> GetCfgKey(string fileName, string Key)
        {
            return config_dict.ContainsKey(fileName) &&
            config_dict[fileName].ContainsKey(Key) ?
            config_dict[fileName][Key] : null;
        }

        /// <summary>
        /// 读取某配置 某一行的数据
        /// </summary>
        /// <param name="fileName">配置名称</param>
        /// <param name="Key">键</param>
        /// <returns></returns>
        public static Dictionary<string, object> GetCfgIndex(string fileName, int Index)
        {
            string index2 = "" + (Index - 1) + "_" + Index;
            return config_dict.ContainsKey(fileName) &&
            config_dict[fileName].ContainsKey(index2) ?
            config_dict[fileName][index2] : null;
        }

        /// <summary>
        /// 读取某配置 某一行的某个字段
        /// </summary>
        /// <param name="fileName"></param>
        /// <param name="Key"></param>
        /// <param name="Field"></param>
        /// <returns></returns>
        public static object GetCfgValue(string fileName, string Key, string Field)
        {
            return config_dict.ContainsKey(fileName) &&
           config_dict[fileName].ContainsKey(Key) &&
           config_dict[fileName][Key].ContainsKey(Field) ?
           config_dict[fileName][Key][Field] :
           null;
        }

        /// <summary>
        /// 将数据按照对应类型转换
        /// </summary>
        /// <param name="value"></param>
        /// <param name="type"></param>
        /// <returns></returns>
        private object ConvertValue(JToken value, string type)
        {
            switch (type)
            {
                case "language_id"://这里是语言id-获取的语言
                    return LanguageLoad.GetText(value.Value<string>());
                case "<language_id>"://这里是语言id列表-获取的语言
                    List<string> list = value.ToObject<List<string>>();
                    for (int i = 0; i < list.Count; i++)
                    {
                        list[i] = LanguageLoad.GetText(list[i]);
                    }
                    return list;
                case "Vector2"://坐标
                    List<float> list2 = value.ToObject<List<float>>();
                    return new Vector2(list2[0], list2[1]);
                case "List<Vector2>"://坐标列表
                    List<List<float>> list3 = value.ToObject<List<List<float>>>();
                    List<Vector2> poslist = new List<Vector2>();
                    for (int i = 0; i < list3.Count; i++)
                    {
                        List<float> list4 = list3[i];
                        poslist.Add(new Vector2(list4[0], list4[1]));
                    }
                    return poslist;
                case "bool":
                    return value.Value<bool>();
                //case "byte":
                //    return value.Value<byte>();
                case "short":
                    return value.Value<short>();
                case "int":
                    return value.Value<int>();
                case "UInt64":
                    return value.Value<UInt32>();
                case "float":
                    return value.Value<float>();
                case "string":
                    return value.Value<string>();
                case "List<bool>":
                    return value.ToObject<List<bool>>();
                //case "List<byte>":
                //    return value.ToObject<List<byte>>();
                case "List<short>":
                    return value.ToObject<List<short>>();
                case "List<int>":
                    return value.ToObject<List<int>>();
                case "List<UInt64>":
                    return value.ToObject<List<UInt64>>();
                case "List<float>":
                    return value.ToObject<List<float>>();
                case "List<string>":
                    return value.ToObject<List<string>>();
                case "List<List<bool>>":
                    return value.ToObject<List<List<bool>>>();
                //case "List<List<byte>>":
                //    return value.ToObject<List<List<byte>>>();
                case "List<List<short>>":
                    return value.ToObject<List<List<short>>>();
                case "List<List<int>>":
                    return value.ToObject<List<List<int>>>();
                case "List<List<UInt64>>":
                    return value.ToObject<List<List<UInt64>>>();
                case "List<List<float>>":
                    return value.ToObject<List<List<float>>>();
                case "List<List<string>>":
                    return value.ToObject<List<List<string>>>();
                // 根据需要添加其他类型转换代码
                default:
                    return value;
            }
        }
		

    }
}