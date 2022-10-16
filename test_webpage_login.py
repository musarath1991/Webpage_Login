#3
from selenium import webdriver

def test_google():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook - log in or sign up"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com/")
    assert driver.title == "Gmail"
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Hp\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.rediff.com/")
    assert driver.title == "Rediff.com News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()

    #for executing 5 browsers at same time/parallelly, pip install pytest-xdist
    # "py.test test_webpage_login.py -n 5"