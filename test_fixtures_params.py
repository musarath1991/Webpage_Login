#7
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import time

#instead of initializing drivers multiple times, we can optimize code like this.
@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    if request.param == "firefox":
        web_driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    request.cls.driver = web_driver

    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.current_url == "https://www.google.com/"

#parallel execution is possible here same as old
#there are 4 test cases, two in chrome and one in ff

