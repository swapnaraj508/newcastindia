from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium. webdriver. common. keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
d = Service("C:/Webdriverselenium/chromedriver_win32 (3)/chromedriver.exe")
driver = webdriver.Chrome(service=d)
class Register1:
    def registerone(self):
        driver.get("http://p1qa.castindia.in/home")
        driver.maximize_window()

        driver.find_element(By.LINK_TEXT, "Sign In / Sign Up").click()
        driver.find_element(By.LINK_TEXT, "Employer").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//html/body/app-root/app-landing/app-login/div/div/div/div[2]/div/div/div[1]/div[2]/app-mobile-verification/form/div/input[1]").send_keys(Keys.ENTER)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-landing/app-login/div/div/div/div[2]/div/div/div[1]/div[2]/app-mobile-verification/form/button")))
        driver.find_element(By.XPATH, "/html/body/app-root/app-landing/app-login/div/div/div/div[2]/div/div/div[1]/div[2]/app-mobile-verification/form/button").click()
       # driver.find_element(By.ID, "otpOne").send_keys(Keys.ENTER)
        time.sleep(10)
        #driver.find_element(By.ID, "otpTwo").send_keys(Keys.ENTER)
        time.sleep(4)
        #driver.find_element(By.ID, "otpThree").send_keys(Keys.ENTER)
        time.sleep(4)
        #driver.find_element(By.ID, "otpFour").send_keys(Keys.ENTER)

        Parent_handle = driver.current_window_handle
        print(Parent_handle)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-danger mt-2']")))
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger mt-2']").click()
        all_handles = driver.window_handles
        print(all_handles)
        """for handle in all_handles:
            if (handle != Parent_handle):
                driver.switch_to.window(handle)"""

r= Register1()
r.registerone()




