# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
import time

# Project Plan
"""
    1. Imports: Libraries
        
    2. Project Plan
    3. Studybay Elements
    4. Variables: (Name all variables >> decide which ones are global and which ones local.)
        a. User Credentials (Inputs: Prompt users and store it )
        b. mail_field && keyword_field (html elements on Studybay)
        c. Login's page identifier, used with expected conditions: Email: '.input__Field-sc-hqbtr5-1.kbzBxw' bY. CSS SELECTOR
        d. 
    5. A function to initialize the WebDriver.
    6. A function to automate the login process.
        a. Use `driver.get(URL)` to navigate to the webpage. Maximize the page.
        b. use `WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-link"))
            )   * Remember this is found on /studybay.com/login/
        c. Locate input fields and then populate them with user's values. ie. mail_field=driver.find_element(By.CSS_SELECTOR, ' ') && mail_field.send_keys(mail)
        d. Click the Login button, wait until EC [An html element to confirm one has logged in]
    7. A function to navigate to the Auction/Project page and place bids.
        a. Navigate to the Projects page
        b. Locate a new project with less than 3 bids at that time, not have a bid on before, then navigate to that project and bid on it.
        c. Find the minimum, average and maximum bid amounts on a particular project and place your bids according to the user's settings.
        d. Navigate back to the project's page to check on another new project.
        e. REPEAT
    8. Database management: 
        a. Setup a database
        b. Add multiple accounts
        c. Integrate Database with Selenium script
    9. Tests
    
"""

# Studybay Elements
""" 
    # Studybay Login-Page Elements
        * XPATH for Email input field = //input[@placeholder='Email']
        * XPATH for Password input field = //input[@placeholder='Password']
        * XPATH for Login button = //button[@type='submit']
        Since, XPaths can be complex and require more processing to traverse the DOM tree, I will use CSS_SELECTOR
            " element = driver.find_element(By.CSS_SELECTOR, '.class_name') "
            
        CSS_SELECTORS
            1. Heading: heading__Heading-sc-1xvnhi1-0 dyrkwh
            2. Bid Button: 
        
        # Locate the input fields using the CSS-SELECTOR
            username_field = driver.find_element(By.CSS_SELECTOR, '.CLASS_NAME')
            password_field = driver.find_element(By.CSS_SELECTOR, '.CLASS_NAME')

        # Populate the fields with your credentials
            username_field.send_keys('your_username')
            password_field.send_keys('your_password')

        # Submit the form
            password_field.send_keys(Keys.RETURN)
        * data-hidden id="login-link" : Always remember the syntax. '[data-hidden id="login-link"]'
        * 
        *
        *

"""

# GLOBAL_VARIABLES

# User Credentials
mail = "billyodhiambo888@gmail.com"
keyword = "123456789"
bid_amount = ""


# Initializing_webDriver
def driver_init():
    
    # custom_User-Agent
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    
    # Options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={custom_user_agent}")
    #/
    options.add_argument("--disable-blink-features=Automation Controlled") # Evades detection

    # Chrome_driver's_service && initializing the webDriver.
    service = Service(executable_path=ChromeDriverManager().install())
    
    # Automatically managing chrome Driver version with webdriver_manager
    driver = webdriver.Chrome(service=service, options=options) 
    return driver # chkd.


# Login_function
def account_login(driver):
    # STUDYBAY LOGIN_URL
    login_url = "https://www.studybay.com/login/"
    wait = WebDriverWait(driver, 200)
    
    driver.get(login_url)
    time.sleep(4)
    driver.maximize_window()
    # Write code to check that the website is maximized here.
    
    # Solving the Captcha
    # checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
    
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
    
    # Wait for login to complete && Adjust the selector to match the one on Studybay's Home page.
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".userInfo__main-avatar"))) 
    

def place_bid(driver, bid_choice="manual", bid_amount="minimum"):
    #STUDYBAY AUCTION_URL
    auction_url = "https://studybay.com/order/search"
    
    try:
        driver.get(auction_url)
        
        #Locate the first 3 projects and bid on them.
        for i in range(3):
            project_list = driver.find_elements(By.CSS_SELECTOR, "") # Adjust selector as needed.
            if len(project_list) > i:
                project_list[i].click() # Click on the project to open it
                
                # Wait for the projects bidding button is seen
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, ""))) # Adjust with correct selector
                
                #Get the MINIMUM, AVERAGE && MAXIMUM Bid values
                min_bid_element = driver.find_element(By.CLASS_NAME, "") # Adjust the selector with correct values from studybay
                max_bid_element = driver.find_element(By.CLASS_NAME, "") # Adjust the selector with correct values from studybay
                average_bid_element = driver.find_element(By.CLASS_NAME, "") # Adjust the selector with correct values from studybay
                
                min_bid = float(min_bid_element.text.strip())
                max_bid = float(max_bid_element.text.strip())
                average_bid = float(average_bid_element.text.strip())
                
                # Get the bid place and pass in the minimum value/ custom number
                bid_input = driver.find_element(By.ID, "") # Adjust accordingly
                
                # Decide Bid price based on user's choice.
                if bid_choice == "min":
                    bid_amount = min_bid
                elif bid_choice == "average":
                    bid_amount = average_bid
                elif bid_choice == "max":
                    bid_amount = max_bid
                # elif bid_choice == "manual" and custom_bid_amount:
                #     bid_amount = custom_bid_amount
                else:
                    print("Invalid bid choice or missing bid amount.")
                    return
                
                bid_input.clear()
                bid_input.send_keys(str(bid_amount))
                
                # Finding the Bid Button
                submit_bid_button = driver.find_element(By.ID, "") # Adjust selector and values accordingly
                submit_bid_button.click() # Placing the bid
                
                time.sleep(4) # Wait for bid to be placed
                
        driver.get("https://www.studybay.com/auction/")
    
    except NoSuchElementException as e:
        print(f"Element not found: {e}") 
    except TimeoutException as e:
        print(f"Operation timed out: {e}")


# MAIN FUNCTION TO RUN BOT
def run_bot():
    driver = driver_init()
    account_login(driver)
    place_bid(driver, bid_choice="min")
    driver.quit()
    
if __name__ == "__main__":
    run_bot()