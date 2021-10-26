import pytest
import os
from util.common.configLogs import LogConfig
import shutil 


PATH = os.path.split(os.path.realpath(__file__))[0]
if __name__ == '__main__':
    # clear logs
    if os.path.exists('./logs'):
        shutil.rmtree('./logs')

    if os.path.exists('./reports'):
        shutil.rmtree('./reports')

    os.mkdir('./logs')
    # add environment & config
    shutil.copy('./venv/environment.properties','./logs')
    shutil.copy('./venv/config.yml','./logs')
    # open console logs
    LogConfig(PATH)
    pytest.main()
    os.system('allure generate logs -o reports --clean')
