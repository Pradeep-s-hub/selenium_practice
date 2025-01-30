from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
title = driver.title
#print("correct title" if title.lower() == "Live Cricket Score, Schedule, Latest News, Stats & Videos | Cricbuzz.com".lower() else "incorrect title")
driver.find_element(By.NAME,"user-name").send_keys("problem_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME,"btn_action").click()
time.sleep(10)
driver.close()