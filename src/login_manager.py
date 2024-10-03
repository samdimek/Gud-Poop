# Handles the logging into Studybay

# Imports
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeOutException 
import time

def account_login(driver, mail, password, login_link):
    wait = WebDriverWait(driver, 27) # Waits for 27 seconds
    
    driver.get(login_link)
    time.sleep(7)
    driver.maximize_window()
    
    # Solving CAPTCHA
    
    # Wait for CAPTCHA to be solved and proceed to login page. *Polling to check if solved.
    
    # Find input-fields and populate them with data and submit form.
    wait.until(EC.presence_of_element(By.CSS_SELECTOR, " ")) # Check presence of page-title
    
    # Locating email-input field
    
    email_input_field = driver.find_element(By.CSS_SELECTOR, " ")
    password_input_field = driver.find_element(By.CSS_SELECTOR, " ")
    
    # Sending input values
    email_input_field.send_keys(mail)
    password_input_field.send_keys(password)
    
    # Try code blocks to catch errors
    try:
        wait.until(EC.presence_of_element(By.CSS_SELECTOR, " "))
        print('Login successful')
    except TimeOutException:
        print('Login Failed')
        driver.quit()