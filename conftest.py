import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def setup():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # opt=webdriver.ChromeOptions()
    # opt.add_argument("--disable-notifications")
    service_obj = Service("D:\driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver

