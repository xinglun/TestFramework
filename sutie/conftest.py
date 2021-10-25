from os import access
import pytest
from util.yaml.yaml_util import YamlUtil

# @pytest.fixture(scope="function/class/module/package/session",params="",autouse ="True/False",ids="",name="")
@pytest.fixture(scope="function")

# login headers
def login():
    headers = YamlUtil().read_config_yaml_item('ediGo-AppKey')
    url = YamlUtil().read_config_yaml_item('baseUrl')
    YamlUtil().clear_config_yaml()
    YamlUtil().write_config_yaml({**headers,**url})
    return
