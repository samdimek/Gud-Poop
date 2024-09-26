# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Imports:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
import time
from bs4 import BeautifulSoup

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Testing_Credentials:
"""
    MAIL: ********odhiambo***@gmail.com
    PW: ***789
    BID_AMOUNT: Minimum
"""


# Initializing_webDriver
def driver_init():
    
    # custom_User-Agent
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    
    # Options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={custom_user_agent}")
    #/
    options.add_argument("--disable-blink-features=Automation Controlled") # Evades detection
    # Headless browsing: without opening the browser window
    # options.headless = True

    # Chrome_driver's_service && initializing the webDriver.
    service = Service(executable_path=ChromeDriverManager().install())
    
    # Automatically managing chrome Driver version with webdriver_manager
    driver = webdriver.Chrome(service=service, options=options) 
    return driver # chkd.

def access_shadow_dom_element(driver):
    driver.get('https://challenges.cloudflare.com/cdn-cgi/challenge-platform/h/g')
    time.sleep(5)
    
    # Access the shadow root
    shadow_host = driver.find_element(By.CSS_SELECTOR, "html > body > div") # Modify with actual data
    shadow_root = driver.execute_script("return arguments[0].ShadowRoot", shadow_host)
    
    # Find the checkbox
    checkbox = shadow_root.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    
    # Check if the checkbox is clickable and click it.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(checkbox))
    checkbox.click()
    print("Checkbox is clicked.") 

# Login_function
def account_login(driver):
    # STUDYBAY LOGIN_URL
    login_url = "https://www.studybay.com/login/"
    wait = WebDriverWait(driver, 200)
    
    mail = "********odhiambo***@gmail.com"
    keyword = "***78"
    
    driver.get(login_url)
    time.sleep(4)
    driver.maximize_window() # maximizing window
    
    # Solving the Captcha : Manual Intervention
    print("Please complete the captcha verification")
    
    # Polling to check if CAPTCHA box is clicked, looping until it is ticked.
    while True:
        try:
            # Find the CAPTCHA checkbox
            captcha_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
            if captcha_checkbox.is_selected():
                print("CAPTCHA checkbox has been ticked. ")
                break
        except NoSuchElementException:
            pass
        time.sleep(3)
    
    # input("Press Enter after completing CAPTCHA")
    # checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
    
    # Parse the page source using BeautifulSoup for verification (optional step)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    captcha_status = soup.find("input", {"type": "checkbox"})
    
    if captcha_status is None:
        print("CAPTCHA is solved. Proceeding with login...")
    else:
        print("CAPTCHA not solved. Please retry.")
        driver.quit()
        return
    
    # Click the checkbox
    # checkbox.click()
    # driver.execute_script("document.getElementsByClassName('cb-i')[0].click();") and wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input[name='email']")))
    
    # Finding Email and Password fields: Using CSS_SELECTOR. Try using web waits with EC.
    mail_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input[name='email']")))
    keyword_field = driver.find_element(By.CSS_SELECTOR, ".input[name='password']")
    
    # Sending user_details
    mail_field.send_keys(mail)
    time.sleep(3)
    keyword_field.send_keys(keyword)
    time.sleep(4)
    
    # Submitting the Login form
    keyword_field.send_keys(Keys.ENTER)
    
    try:
        # Wait for login to complete && Adjust the selector to match the one on Studybay's Home page.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".userInfo__main-avatar"))) 
        print("Login Successful!")
    except TimeoutException:
        print("Login Failed. Please")
        
    
# MAIN FUNCTION TO RUN BOT
def run_bot():
    driver = driver_init()
    account_login(driver)
    access_shadow_dom_element(driver)
    # place_bid(driver, bid_choice="min")
    driver.quit()
    
if __name__ == "__main__":
    run_bot()
