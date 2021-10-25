
import pytest
import allure
from util.yaml.yaml_util import YamlUtil
from util.request.requestSend import send_request


class TestLogin:

    @allure.description("login test")
    @allure.severity("normal") # blocker > critical > normal > minor > trivial
    @allure.feature("common")
    @allure.story("login")
    # @allure.issure() bug number
    @allure.testcase("正常ログインテスト")
    # @pytest.mark.run(order=1)
    # @pytest.mark mark
    @pytest.mark.parametrize("testcases",YamlUtil().read_testcases_yaml("get_token.yml"))
    def test_get_token(self,login,testcases):
        login
        # send 
        rep,check = send_request(testcases)
        config = {
                    "userId":rep.json()['data']['userId'],
                    "firmId":rep.json()['data']['firmId'],
                    "publisherId":rep.json()['data']['publisherId'],
                    "access_token":'Bearer ' + rep.json()['data']['access_token'],
                    "refresh_token":rep.json()['data']['refresh_token'],
                    "roleId":rep.json()['data']['roleId'],
                    "userName":rep.json()['data']['userName']
                }
        YamlUtil().write_config_yaml(config)
        assert check == True


    @allure.description("login test")
    @allure.severity("normal") # blocker > critical > normal > minor > trivial
    @allure.feature("common")
    @allure.story("login")
    # @allure.issure() bug number
    @allure.testcase("入力情報不足テスト + 無効アカウントテスト ")
    # @pytest.mark.run(order=1)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("testcases",YamlUtil().read_testcases_yaml("login.yml"))
    def test_login(self,testcases):
        # send post
        rep,check = send_request(testcases)
        assert check == True
        
        




