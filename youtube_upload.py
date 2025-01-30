import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# import pyautogui
from pynput.keyboard import Controller, Key
import schedule
#import pyautogui
from pynput.keyboard import Controller,Key
import schedule



def youtube_upload():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    service_obj = Service("D:\driver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.youtube.com/")
    driver.find_element(By.LINK_TEXT,"Sign in").click()
    driver.find_element(By.XPATH,"//input[@type='email']").send_keys("jobless.ninja007@gmail.com")
    driver.find_element(By.XPATH,"//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']").click()
    #send_keys("Pradep@4163.")
    sleep(100)

    driver.close()
youtube_upload()