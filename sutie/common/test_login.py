
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
    @allure.testcase("正常ログインテスト + 入力情報不足テスト + 無効アカウントテスト ")
    # @pytest.mark.run(order=1)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("testcases",YamlUtil().read_testcases_yaml("login.yml"))
    def test_login(self,testcases):
        # send post and check results
        rep,check = send_request(testcases)
        assert check == True
        
        




