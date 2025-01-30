from selenium import webdriver
from selenium.webdriver.chrome.service import Service

opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
service_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj,options=opt)
driver.implicitly_wait(10)


driver.get("https://whatmylocation.com/")
driver.maximize_window()
driver.close()