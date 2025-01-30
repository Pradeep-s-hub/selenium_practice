import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from time import sleep
from pynput.keyboard import Controller,Key

class TestResumeUpload:
    @pytest.mark.nakuri
    # pytest -v -s test_pytest_file_upload_fixtures_modules.py -m nakuri
    # @pytest.mark.run(order=1)
    @pytest.mark.second
    @pytest.mark.parametrize('email,password',[("sompradeep.p@gmail.com","Pradeep@4163.")])
    def test_nakuri(self,setup,email,password):
        self.driver= setup
        self.driver.get("https://www.naukri.com/")
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='text' and contains(@placeholder,'Email')]").send_keys(
            email)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Login']").click()
        self.driver.find_element(By.XPATH, "//div[@class='view-profile-wrapper']/a").click()
        self.driver.find_element(By.XPATH, "//input[@type='button' and contains(@value,'Update resume')]").click()
        sleep(5)
        keyboard = Controller()

        keyboard.type("D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(5)
        # ***** setTimeout(function(){debugger;},10000);
        #    ##sucess_msg_ele = driver.find_element(By.XPATH, "//div[@class ='cnt']/p[2]")
        try:
            sucess_msg_ele = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class ='cnt']/p[2]")))
            assert sucess_msg_ele.text == "Resume has been successfully uploaded.", "Resume not uploaded"
            print("File uploaded successfully...")
        except Exception as exp:
            print(exp)
        sleep(2)
        self.driver.close()



    @pytest.mark.foundit
    # pytest -v -s test_pytest_file_upload_fixtures_modules.py -m foundit
    @pytest.mark.first
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize('email,password', [("sompradeep.p@gmail.com", "Pradeep@4163.")])
    def test_foundit(self,setup,email,password):
        self.driver = setup
        self.driver.get("https://www.foundit.in/")
        self.driver.find_element(By.XPATH, "//div[@class='flex gap-4']/button[1]").click()
        self.driver.find_element(By.CLASS_NAME, "loginWith").click()
        self.driver.find_element(By.XPATH, "//input[@id='signInName']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//img[@class='rounded-full']").click()
        self.driver.find_element(By.LINK_TEXT, "View Profile").click()
        self.driver.find_element(By.XPATH, "//div[@class='uploadedBtn']/button/div/input").send_keys(
            "D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")
        self.driver.close()