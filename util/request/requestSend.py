
import logging

import allure
import requests
import json
from util.common import readParams,checkAssert



def send_request(data,**kwargs):

    logging.info("="*100)
    headers = readParams.read_param(data['request']['headers'])
    url = readParams.read_param(data['request']['baseUrl'])['baseUrl'] + data['request']['router']
    if data['request'].get("accessToken") != None:
        accessToken = readParams.read_param(data['request']['accessToken'])
        headers = {**headers,**{'Authorization':accessToken['accessToken']}}
    if data['request'].get("firmId") != None:
        firmId = readParams.read_param(data['request']['firmId'])
        headers = {**headers,**firmId}   
    if data['request'].get("publisherId") != None:
        publisherId = readParams.read_param(data['request']['publisherId'])
        headers = {**headers,**publisherId}      
    if data['request'].get("refreshToken") != None:
        refreshToken = readParams.read_param(data['request']['refreshToken'])
        headers = {**headers,**refreshToken}
    if data['request'].get("roleId") != None:
        roleId = readParams.read_param(data['request']['roleId'])
        headers = {**headers,**roleId}
    if data['request'].get("userId") != None:
        userId = readParams.read_param(data['request']['userId'])
        headers = {**headers,**userId} 
    if data['request'].get("userName") != None:
        userName = readParams.read_param(data['request']['userName'])
        headers = {**headers,**userName}             
    method = data['request']['method']
    logging.debug("headers：  %s" % str(headers))
    logging.debug("url：  %s" % str(url))
    logging.debug("method：  %s" % str(method))
    logging.info("headers：  %s" % str(headers))
    logging.info("url：  %s" % str(url))
    logging.info("method：  %s" % str(method))
    logging.info("test case：%s" % str(data["name"]))
    if method.lower() == 'post':
        body = json.dumps(data["params"])
        with allure.step("POST"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("POST")
        result = requests.request(method = method,url = url, headers = headers, data = body,**kwargs)
    elif method.lower() == 'get':
        with allure.step("GET"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("GET")
        result = requests.request(method = method,url = url, headers = headers, data = data["params"],**kwargs)
    elif method.lower() == 'put':
        body = json.dumps(data["params"])
        with allure.step("PUT"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("PUT")
        result = requests.request(method = method,url = url, headers = headers, data = body,**kwargs)
    elif method.lower() == "delete":
        with allure.step("DELETE"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("DELETE")
        result = requests.request(method = method,url = url, headers = headers, data = data["params"],**kwargs)
    else:
        result = {"code": False, "data": False}
    logging.info("result：\n %s" % str(result))
    check = checkAssert.check_assert(result.json(),data["validate"])
    return result,check

