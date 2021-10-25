import os
import yaml

# YamlUtil
class YamlUtil:
# read config.yaml
    # read config_yaml 
    def read_config_yaml(self):
        with open(os.getcwd() + "\\venv\\config.yml",mode="r",encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

    # read config_yaml_item 
    def read_config_yaml_item(self,key):
        with open(os.getcwd() + "\\venv\\config.yml",mode="r",encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            if value.get(key) == None:
                raise Exception("Invalid key", key)
            return {key: value.get(key)}

    # read config_yaml_value
    def read_config_yaml_value(self,key):
        with open(os.getcwd() + "\\venv\\config.yml",mode="r",encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            if value.get(key) == None:
                raise Exception("Invalid key", key)
            return value.get(key)
 
    # write config.yml
    def write_config_yaml(self,data):
        with open(os.getcwd() + "\\venv\\config.yml",mode="a",encoding="utf-8") as f:
            value = yaml.dump(data=data,stream=f,allow_unicode=True)

    # clear config.yml
    def clear_config_yaml(self):
        with open(os.getcwd() + "\\venv\\config.yml",mode="w",encoding="utf-8") as f:
            f.truncate()

# read testcases.yaml
    # read testcases.yml
    def read_testcases_yaml(self,yaml_name):
        with open(os.getcwd() + "\\testcases\\" + yaml_name ,mode="r",encoding="utf-8") as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value

