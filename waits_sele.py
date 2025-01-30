from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re




serv_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
exp_wait = WebDriverWait(driver,10)
####applicatiuon cmds
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #oening the application URL
driver.maximize_window()
sleep(10)

#user_box= driver.find_element(By.XPATH,"//input[@placeholder='Username']")
user_box = exp_wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']")))
user_box.send_keys("Admin")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
submit = exp_wait.until(EC.presence_of_element_located((By.XPATH,"//button[@type='submit']")))
submit.click()
driver.quit()
