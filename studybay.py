# Imports

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
from time import sleep
from DrissionPage import ChromiumPage




# Setting up Chrome's driver's service & using it to initialize the web driver.

service = Service(executable_path="chromedriver.exe")  
driver = webdriver.Chrome(service=service)


# Initialize variables

email = "billyodhiambo888@gmail.com"
password = "123456789"
login_URL = "https://studybay.com/login/" # https://studybay.com/login/

'''
    p = ChromiumPage()
    p.get("https://nowsecure.nl/")
    i = p.get_frame("@src^https://challenges.cloudflare.com/cdn-cqi")
    e = i(".mark")
    sleep(3)
'''


driver.get(login_URL)  # Get the browser's page.

driver.maximize_window() # Maximizing the web page.


# Studybay Login-Page Elements
'''
    * XPATH for Email input field = //input[@placeholder='Email']
    * XPATH for Password input field = //input[@placeholder='Password']
    * XPATH for Login button = //button[@type='submit']
'''


# Fetching data from Studybay Login-Page

email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']" )
password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']" )
login_Btn = driver.find_element(By.XPATH, "//button[@type='submit']")


# Adding values && Logging in.

email_field.send_keys(email)
password_field.send_keys(password)
login_Btn.click()




