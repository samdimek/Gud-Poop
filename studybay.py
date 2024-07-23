# Imports

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
from DrissionPage import ChromiumPage




# Setting up Chrome's driver's service & using it to initialize the web driver.

service = Service(executable_path="chromedriver.exe")  
driver = webdriver.Chrome(service=service) # Changing the driver with undetectable driver.


# Initialize variables

email = "email"
mail = "billyodhiambo888@gmail.com"
keyword = "123456789"
login_URL = "https://studybay.com/login/" # https://studybay.com/login/

'''
    p = ChromiumPage()
    p.get("https://nowsecure.nl/")
    i = p.get_frame("@src^https://challenges.cloudflare.com/cdn-cqi")
    e = i(".mark")
    sleep(3)
'''

# Getting da browser's page && maximizing it.

driver.get(login_URL)
driver.maximize_window()

# Ensure navigation to login-page.
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(By.NAME, email)
)


# Studybay Login-Page Elements
'''
    * XPATH for Email input field = //input[@placeholder='Email']
    * XPATH for Password input field = //input[@placeholder='Password']
    * XPATH for Login button = //button[@type='submit']
'''


# Fetching data from Studybay Login-Page

mail_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']" )
keyword_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']" )
login_Btn = driver.find_element(By.XPATH, "//button[@type='submit']")


# Adding values && Logging in.

mail_field.send_keys(mail)
keyword_field.send_keys(keyword)
login_Btn.click()




