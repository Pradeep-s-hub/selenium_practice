import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from time import sleep
from time import sleep
#import pyautogui
from pynput.keyboard import Controller,Key
import schedule

class TestResumeUpload:
    @pytest.fixture()
    def setup(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # opt=webdriver.ChromeOptions()
        # opt.add_argument("--disable-notifications")
        service_obj = Service("D:\driver\chromedriver.exe")
        print("hhhhhhhhhhhhhhh")
        self.driver = webdriver.Chrome(options=options, service=service_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        yield
        self.driver.close()
    def test_nakuri(self,setup):
        self.driver.get("https://www.naukri.com/")
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        sleep(2)
        # //input[@type='text' and contains(@placeholder,'Email')]
        self.driver.find_element(By.XPATH, "//input[@type='text' and contains(@placeholder,'Email')]").send_keys(
            "sompradeep.p@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Pradeep@4163.")
        # driver.find_element()
        self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Login']").click()

        self.driver.find_element(By.XPATH, "//div[@class='view-profile-wrapper']/a").click()

        # //input[@type='button' and contains(@value,'Update resume')]
        self.driver.find_element(By.XPATH, "//input[@type='button' and contains(@value,'Update resume')]").click()
        # pyautogui.write(r"D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        # pyautogui.press("enter")
        # ctrl+ shift + p
        sleep(5)
        keyboard = Controller()

        keyboard.type("D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        #sleep(5)
        # ***** setTimeout(function(){debugger;},10000);
        #    ##sucess_msg_ele = driver.find_element(By.XPATH, "//div[@class ='cnt']/p[2]")
        try:
            sucess_msg_ele = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class ='cnt']/p[2]")))
        except Exception as exp:
            print(exp)
        # if sucess_msg_ele.text == "Resume has been successfully uploaded.":
        #    print("resume uloaded sucessfully.....")
        # else:
        #    raise Exception

        # assert True if(sucess_msg_ele.text == "Resume has been successfully uploaded.") else False, "resume not uploaded"

        raise Exception("resume not uploaded") if (
                    sucess_msg_ele.text != "Resume has been successfully uploaded.") else print(
            "file uploaded sucessfully...")

        driver.close()
    def test_foundit(self,setup):
        self.driver.get("https://www.foundit.in/")
        self.driver.find_element(By.XPATH, "//div[@class='flex gap-4']/button[1]").click()
        self.driver.find_element(By.CLASS_NAME, "loginWith").click()
        # driver.find_element(By.XPATH,"//div[@class ='loginWith']").click()
        self.driver.find_element(By.XPATH, "//input[@id='signInName']").send_keys("sompradeep.p@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Pradeep@4163.")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//img[@class='rounded-full']").click()
        self.driver.find_element(By.LINK_TEXT, "View Profile").click()
        # driver.find_element(By.LINK_TEXT,"Delete").click()
        # driver.find_element(By.XPATH,"//div[@class='confirm-btn']/button").click()
        # //input[@id='inline-resume']
        # driver.find_element(By.XPATH, "//div[@class='uploadImg']/img").click()
        self.driver.find_element(By.XPATH, "//div[@class='uploadedBtn']/button/div/input").send_keys(
            "D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        # driver.find_element(By.XPATH, "//input[@id='inline-resume']").send_keys("D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        # sucess_msg_ele=driver.find_element(By.XPATH,"div[@id='notificationHolder' and @data-fromat='format-tipsy-full-delete']/div/div/p[@class='fs-18']")

        # raise Exception("resume not uploaded") if(sucess_msg_ele.text != "Simple body text this will replace with orginal content") else print("file uploaded sucessfully...")

        # keyboard = Controller()
        # keyboard.type("D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        # sleep(5)
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)
        #driver.close()