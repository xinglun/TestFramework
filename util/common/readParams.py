import re
from util.yaml.yaml_util import YamlUtil
from util.randomData import choiceData,getTime,randomInt,randomFloat,randomString


def read_param(value):
    # re
    int_list = re.findall('\\$randomInt\\(([0-9]*,[0-9]*?)\\)\\$', value)
    string_list = re.findall('\\$randomString\\(([0-9]*?)\\)\\$', value)
    float_list = re.findall("\\$randomFloat\\(([0-9]*,[0-9]*,[0-9]*)\\)\\$", value)
    time_list = re.findall("\\$getTime\\(time_type=(.*?),layout=(.*?),unit=([0-9],[0-9],[0-9],[0-9],[0-9])\\)\\$", value)
    choice_list = re.findall("\\$choiceData\\(((?!\\$Choice\\().*?)\\)\\$", value)
    config_list = re.findall("\\$getConfigData\\((.*?)\\)\\$", value)
    # init var
    if len(int_list):
        for i in int_list:
            pattern = re.compile('\\$randomInt\\(' + i + '\\)\\$')  
            k = str(randomInt.random_int(i))
            value = re.sub(pattern, k, value, count=1)
        value = read_param(value)
    elif len(string_list):
        # 获取字符串替换
        for j in string_list:
            pattern = re.compile('\\$RandomString\\(' + j + '\\)\\$') 
            k = randomString.random_string(j)
            value = re.sub(pattern, k, value, count=1)
        value = read_param(value)
    elif len(float_list):
        # 获取浮点数
        for n in float_list:
            if len(n.split(",")) == 3:
                pattern = re.compile('\\$RandomFloat\\(' + n + '\\)\\$')
                k = str(randomFloat.random_float(n))
                value = re.sub(pattern, k, value, count=1)
        value = read_param(value)
    elif len(time_list):
        # 获取时间替换
        for n in time_list:
            if len(n[0]) and len(n[1]):
                pattern = re.compile('\\$GetTime\\(time_type='+n[0]+',layout='+n[1]+',unit='+n[2]+'\\)\\$') 
                k = str(getTime.get_time(n[0], n[1], n[2]))
                value = re.sub(pattern, k, value, count=1)
        value = read_param(value)
    elif len(choice_list):
        # 调用choice方法
        for n in choice_list:
            pattern = re.compile('\\$choiceData\\(' + n + '\\)list\\$') 
            k = str(choiceData.choice_data(n))
            value = re.sub(pattern, k, value, count=1)
        value = read_param(value)
    else:
        for n in config_list:
            pattern = re.compile('\\$getConfigData\\(' + n + '\\)\\$') 
            k = YamlUtil().read_config_yaml_item(n)
            print(k)
        value = k

    return value


