import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.NAME,"user-name").send_keys("problem_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME,"btn_action").click()
driver.find_element(By.LINK_TEXT,"Twitter").click()
handles = driver.window_handles
#driver.back()
driver.switch_to.window(handles[1])
time.sleep(10)
driver.close()
driver.switch_to.window(handles[0])
driver.find_element(By.PARTIAL_LINK_TEXT,"Face").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
time.sleep(10)
driver.close()
driver.switch_to.window(handles[0])
no_of_ele = driver.find_elements(By.CLASS_NAME,"inventory_item")
print("total no of items in page are: ", len(no_of_ele))
each_item=driver.find_elements(By.CSS_SELECTOR,"div.inventory_item_name")

for i in range(len(each_item)):
    print(each_item[i])
    #print(each_item[i].text)
    #print(i)
    if each_item[i].text == "Sauce Labs Backpack":
        each_item[i].click()
        break
time.sleep(10)
driver.close()




