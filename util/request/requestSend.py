
import logging
import re

import allure
import requests
import json
from util.common import login, readParams,checkAssert,readHeaders



def send_request(data,**kwargs):

    logging.info("="*100)   
    account_rep = login.login(data['account'])
    if account_rep.json()["code"] != 1:
        logging.debug("invalid account：  %s" % str(data['account']))
        logging.info("invalid account：  %s" % str(data['account']))
    # read headers
    headers = readHeaders.read_headers(data)
    # read url
    url = readParams.read_param(data['request']['baseUrl'])['baseUrl'] + data['request']['router'] 
    # read method
    method = data['request']['method']
    # console logs
    logging.debug("headers：  %s" % str(headers))
    logging.debug("url：  %s" % str(url))
    logging.debug("method：  %s" % str(method))
    logging.info("headers：  %s" % str(headers))
    logging.info("url：  %s" % str(url))
    logging.info("method：  %s" % str(method))
    logging.info("test case：%s" % str(data["name"]))
    # send request
    # post
    if method.lower() == 'post':
        body = json.dumps(data["params"])
        with allure.step("POST"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("POST")
        result = requests.request(method = method,url = url, headers = headers, data = body,**kwargs)
    # get
    elif method.lower() == 'get':
        with allure.step("GET"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("GET")
        result = requests.request(method = method,url = url, headers = headers, data = data["params"],**kwargs)
    # put
    elif method.lower() == 'put':
        body = json.dumps(data["params"])
        with allure.step("PUT"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("PUT")
        result = requests.request(method = method,url = url, headers = headers, data = body,**kwargs)
    # delete
    elif method.lower() == "delete":
        with allure.step("DELETE"):
            allure.attach("test case：", str(data["name"]))
            allure.attach("url", str(url))
            allure.attach("headers", str(headers))
            allure.attach("params", str(data["params"]))
        logging.info("DELETE")
        result = requests.request(method = method,url = url, headers = headers, data = data["params"],**kwargs)
    # error
    else:
        result = {"code": False, "data": False}
    logging.info("result：\n %s" % str(result))
    check = checkAssert.check_assert(result.json(),data["validate"])
    return result,check

