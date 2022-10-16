#6
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import time

@pytest.fixture(scope='class')
def init_Chrome_driver(request):
    ch_driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    request.cls.driver = ch_driver  #cls = class label

    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    request.cls.driver = ff_driver  # firefox driver. as we dont have ff driver, so same code for chrome

    yield
    ff_driver.close()

@pytest.mark.usefixtures("init_Chrome_driver")
class Base_Chrome_Test():
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures("init_ff_driver")
class Base_ff_Test():
    pass

class Test_Ff_Chrome(Base_ff_Test):
    def test_google_title_ff(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"






