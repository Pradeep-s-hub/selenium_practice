from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import re
serv_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()
#absolutive xpath
driver.find_element(By.XPATH,"html/body/header/div/div/div[2]/div/input").send_keys("iphone")
#relative XPATH
driver.find_element(By.XPATH,"//div[@id = 'search']/span/button").click()
driver.find_element(By.CSS_SELECTOR,"img.img-responsive[title='iPhone'] ").click()
driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
text = driver.find_element(By.XPATH,"")
match = re.search(r"(\d+)\s+item\(s\)", text)
num_items = match.group(1)
if  num_items == 1:
    print("item added:",num_items)
    assert num_items > 1, "MORE THAN ONE ITEM ADDED"
else:
    print("No items found in the text.")
sleep(10)
driver.close()
