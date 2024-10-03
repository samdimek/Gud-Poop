# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

# https://sites.google.com/chromium.org/driver/

# Setting up Chrome's driver service && Using that to initialize the webdriver
# A webdriver is an automation tool that controls Google chrome or Brave. 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Brightdata is a company that solves the captcha issues

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")  # Finds the element on the website by its classname. 
input_element.clear() # Clears the input spaces to make room for more inputs.
input_element.send_keys("Studybay.com" + Keys.ENTER) # Sends inputs to the browser and presses Enter to search

WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Studybay.com"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Studybay.com")
link.click()

time.sleep(10)


driver.quit
