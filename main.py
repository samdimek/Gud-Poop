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

driver.get("https://studybay.com")
driver.maximize_window()

WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.ID, "login-link"))
)

# Brightdata is a company that solves the captcha issues

input_element = driver.find_element(By.ID, "login-link")
input_element.click() # Clicked to log in.
driver.maximize_window() 

WebDriverWait(driver, 7).until(
    # EC.presence_of_element() # Ensure navigation to login page. 
)


# LOGIN-PAGE

email = "billyodhiambo888@gmail.com"
password = "123456789"


# Fetching data from Studybay Login-Page

email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']" )
password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']" )
login_Btn = driver.find_element(By.XPATH, "//button[@type='submit']")


# Adding values && Logging in.

email_field.clear()
email_field.send_keys(email)
password_field.clear()
password_field.send_keys(password)
login_Btn.click()

# input_element.clear() # Clears the input spaces to make room for more inputs.
# input_element.send_keys("Studybay.com" + Keys.ENTER) # Sends inputs to the browser and presses Enter to search

WebDriverWait(driver, 7).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Studybay.com"))
)

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Studybay.com")
# link.click()

time.sleep(10)


driver.quit
