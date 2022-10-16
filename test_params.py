#12
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import time

#driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):
    @pytest.mark.parametrize("username, password", [("admin@gmail.com","admin123"),("musarath@gmail.com","musarath123")])

    def test_login(self, username, password):
        #this is used to login the application
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID,"username").send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(5)







