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
        element = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-landing/app-login/div/div/div/div[2]/div/div/div[1]/div[2]/app-mobile-verification/form/button")))
        driver.find_element(By.XPATH, "/html/body/app-root/app-landing/app-login/div/div/div/div[2]/div/div/div[1]/div[2]/app-mobile-verification/form/button").click()
        Parent_handle = driver.current_window_handle
        print(Parent_handle)
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-danger mt-2']")))
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger mt-2']").click()
        all_handles = driver.window_handles
        print(all_handles)
        #driver.get("http://p1qa.castindia.in/employer/standard-form")
        driver.find_element(By.XPATH, "//input[@ID = 'first_name']").send_keys("test")
        driver.find_element(By.ID, "last_name").send_keys("test")
        driver.save_screenshot("rer2form.png")

r= Register1()
r.registerone()