from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

service_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.implicitly_wait(10)
wait_obj=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
#//div[@class='example']/ul/li[3]
driver.find_element(By.XPATH,"//div[@class='example']/ul/li[3]/button").click()
#wait_obj.until(EC.presence_of_element_located((By.XPATH,"//div[@class='example']/ul/li[3]"))).click()
alert_window = driver.switch_to.alert
print(alert_window.text) # get the text inside alert box
alert_window.send_keys("pradeep") # send the text to the alert box
alert_window.accept() # click ok
#alert_window.dismiss() # click cancel


driver.find_element(By.XPATH,"//div[@class='example']/ul/li[2]/button").click()
#wait_obj.until(EC.presence_of_element_located((By.XPATH,"//div[@class='example']/ul/li[3]"))).click()
alert_window = driver.switch_to.alert
print(alert_window.text) # get the text inside alert box
alert_window.dismiss()


driver.find_element(By.XPATH,"//div[@class='example']/ul/li[1]/button").click()
#wait_obj.until(EC.presence_of_element_located((By.XPATH,"//div[@class='example']/ul/li[3]"))).click()
alert_window = driver.switch_to.alert
print(alert_window.text) # get the text inside alert box
alert_window.accept()


driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
sleep(10)
driver.close()


