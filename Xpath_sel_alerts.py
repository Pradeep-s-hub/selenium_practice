from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
service_obj = Service("D:\driver\chromedriver.exe")
driver = webdriver.Chrome(service = service_obj,options=opt)
driver.implicitly_wait(10)
wait_obj=WebDriverWait(driver,10,poll_frequency=2)
driver.get("https://demoqa.com/")
driver.maximize_window()

frames = driver.find_elements(By.TAG_NAME, 'iframe') + driver.find_elements(By.TAG_NAME, 'frame')

# Print the number of frames and their details
print(f"Total frames found: {len(frames)}")
for index, frame in enumerate(frames):
    print(f"Frame {index + 1}: {frame.get_attribute('id') or 'No ID'}, {frame.get_attribute('name') or 'No Name'}")
#//h5[normalize-space()='Alerts, Frame & Windows']

driver.find_element(By.XPATH,"//h5[normalize-space()='Alerts, Frame & Windows']").click()

driver.close()

driver.get("https://whatmylocation.com/")
driver.maximize_window()
