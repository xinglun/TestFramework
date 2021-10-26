import logging
import pytest
import requests
from util.yaml.yaml_util import YamlUtil

def login(account):
    # base header & base url
    headers = YamlUtil().read_config_yaml_item('ediGo-AppKey')
    baseUrl = YamlUtil().read_config_yaml_item('baseUrl')
    url = baseUrl['baseUrl'] + '/login'
    YamlUtil().clear_config_yaml()
    YamlUtil().write_config_yaml({**headers,**baseUrl})
    # with account info
    if account != None:
        data = {
            'mail': account['mail'],
            'password': str(account['password']),
            'publisherId': account['publisherId']
        }
    # get defalut account
    else:
        data = YamlUtil().read_testcases_yaml("get_token.yml")[0]
        data = {
            'mail': data['params']['mail'],
            'password': data['params']['password'],
            'publisherId': data['params']['publisherId']
        }
    # login
    rep = requests.request(method = 'post',url = url, headers = headers, json = data)
    # login success
    if rep.json()['code'] == 1:
        config = {
                    "userId":str(rep.json()['data']['userId']),
                    "firmId":str(rep.json()['data']['firmId']),
                    "publisherId":str(rep.json()['data']['publisherId']),
                    "accessToken":'Bearer ' + str(rep.json()['data']['access_token']),
                    "refreshToken":str(rep.json()['data']['refresh_token']),
                    "roleId":str(rep.json()['data']['roleId']),
                    "userName":str(rep.json()['data']['userName'])
                }
        YamlUtil().write_config_yaml(config)
    # console logs
    logging.debug("account：  %s" % str(rep))
    logging.info("account：  %s" % str(rep))
    return rep