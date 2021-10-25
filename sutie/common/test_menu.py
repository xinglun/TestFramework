import pytest
import allure
from util.common.login import login
from util.yaml.yaml_util import YamlUtil
from util.request.requestSend import send_request
class TestMenu:
    @allure.description("menu test")
    @allure.severity("normal") # blocker > critical > normal > minor > trivial
    @allure.feature("common")
    @allure.story("login")
    # @allure.issure() bug number
    @allure.testcase("正常ログインテスト ")
    # @pytest.mark.run(order=1)
    # @pytest.mark.smoke
    @pytest.mark.parametrize("testcases",YamlUtil().read_testcases_yaml("menu.yml"))
    def test_menu(self,testcases): 
        account_rep = login(testcases['account'])
        # send post
        _,check = send_request(testcases)
        assert check == True
