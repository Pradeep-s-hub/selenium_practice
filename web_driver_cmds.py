from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re


serv_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
####applicatiuon cmds
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #oening the application URL
driver.maximize_window()

print(driver.title) # to capture the title of website
print(driver.current_url) #to capture the current url of website
print(driver.page_source) #to capture the page source of website
####conditionl cmds
user_box= driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active'] and //input[@placeholder='Username']")
print(user_box.is_enabled())
print(user_box.is_displayed())
user_box.send_keys("Admin")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
sleep(10)
driver.close()
driver.quit()