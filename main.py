# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time

# https://sites.google.com/chromium.org/driver/

# Setting up Chrome's driver service && Using that to initialize the webdriver
# A webdriver is an automation tool that controls Google chrome or Brave.
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://studybay.com/login/")

input_element = driver.find_element(By.CLASS_NAME, "input__Field-sc-hqbtr5-1 kbzBxw")
input_element.clear()
input_element.send_keys("billyodhiambo888@gmail.com" + Keys.ENTER)


time.sleep(10)

driver.quit
