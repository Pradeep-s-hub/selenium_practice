from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import  requests as req


service_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
##############CheckBox#################
#1- Select specific checkbox
#//input[@id='sunday']
sun_ele=driver.find_element(By.XPATH,"//input[@id='sunday']")
sun_ele.click()
sun_ele.click()


every_days = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and contains(@id, 'day')]")

for every_day in every_days:
    every_day.click()
sleep(2)

for every_day in every_days:
    every_day.click()
sleep(2)
select_list=['monday','sunday']
for every_day in every_days:
    weak_name=every_day.get_attribute('id')
    if weak_name in select_list:
        every_day.click()
sleep(2)
for every_day in every_days:
    weak_name=every_day.get_attribute('id')
    if weak_name in select_list:
        every_day.click()
#select last 2
n=2
for index in range(-1,-(n+1),-1):
    every_days[index].click()
sleep(2)
for every_day in every_days:
    if every_day.is_selected():
        every_day.click()
sleep(2)
#driver.close()
############links##########
###internal link
###external link
###broken link
links = driver.find_elements(By.TAG_NAME,"a")
####Handeling broken links
count = 0
for link in links:
    url=link.get_attribute("href")
    try:
        res = req.head(url)
        if res.status_code >= "400":
            print(url)
            count += 1
    except:
        None

print("total links in web page: ", len(links))
print("total broken links in web page: ", count)
##finding all links in page
for link in links:
    print(link.text)

driver.get("https://demo.nopcommerce.com/apparel")
link_text = driver.find_element(By.LINK_TEXT,"Digital downloads")
#link_text = driver.find_element(By.PARTIAL_LINK_TEXT,"Digital")
link_text.click()





driver.close()
