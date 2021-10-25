import pytest
import requests
from util.yaml.yaml_util import YamlUtil

# @pytest.fixture(scope="function/class/module/package/session",params="",autouse ="True/False",ids="",name="")
@pytest.fixture(scope="function")

# login headers
def Init_login():
    headers = YamlUtil().read_config_yaml_item('ediGo-AppKey')
    url = YamlUtil().read_config_yaml_item('baseUrl')
    YamlUtil().clear_config_yaml()
    YamlUtil().write_config_yaml({**headers,**url})
    return

# @pytest.fixture(scope="function")
# def login(account):
#     headers = YamlUtil().read_config_yaml_item('ediGo-AppKey')
#     url = YamlUtil().read_config_yaml_item('baseUrl')
#     YamlUtil().clear_config_yaml()
#     YamlUtil().write_config_yaml({**headers,**url})
#     if account != None:
#         data = {
#             'mail': account['mail'],
#             'password': str(account['password']),
#             'publisherId': account['publisherId']
#         }
#     else:
#         data = YamlUtil().read_testcases_yaml("get_token.yml")
#         data = {
#             'mail': data['params']['mail'],
#             'password': data['params']['password'],
#             'publisherId': data['params']['publisherId']
#         }

#     rep = requests.request(method = post,url = url, headers = headers, json = data)
#     config = {
#                 "userId":rep.json()['data']['userId'],
#                 "firmId":rep.json()['data']['firmId'],
#                 "publisherId":rep.json()['data']['publisherId'],
#                 "accessToken":'Bearer ' + rep.json()['data']['access_token'],
#                 "refreshToken":rep.json()['data']['refresh_token'],
#                 "roleId":rep.json()['data']['roleId'],
#                 "userName":rep.json()['data']['userName']
#             }
#     YamlUtil().write_config_yaml(config)
#     return 
