from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import time
d = Service("C:/Webdriverselenium/chromedriver_win32 (3)/chromedriver.exe")
driver = webdriver.Chrome(service=d)
driver.get("http://p1qa.castindia.in/employer/dashboard")
driver.maximize_window()