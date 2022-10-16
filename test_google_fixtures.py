#5
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import time

driver = None

@pytest.fixture(scope='module')
def setup_module():
    global driver
    print("-------------setup-----------")
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

    yield     #code after yield will execute after test cases
    print("-----------tear down------------")
    driver.quit()

    #set up module name can change to init driver

@pytest.mark.usefixtures("setup_module")
def test_google_title():
    assert driver.title == "Google"

@pytest.mark.usefixtures("setup_module")
def test_google_url():
    assert driver.current_url == "https://www.google.com/"