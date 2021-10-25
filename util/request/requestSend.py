
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
        headers = {**headers,**accessToken}
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

