import pytest
import os
from util.common.configLogs import LogConfig
import shutil 


PATH = os.path.split(os.path.realpath(__file__))[0]
failureException = AssertionError
if __name__ == '__main__':
    # shutil.rmtree('.\logs')
    # os.mkdir('.\logs')
    LogConfig(PATH)
    pytest.main()
    os.system('allure generate logs -o reports --clean')
