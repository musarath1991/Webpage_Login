#4
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import time

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "https://www.google.com/"

# if we want more output  pytest -v -s test_google_test.py

#for generating html report  pip install pytest-html
# pytest test_google_test.py -v -s --html=google_test_report.html