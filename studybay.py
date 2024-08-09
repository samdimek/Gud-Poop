 # Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# User Credentials
mail = "billyodhiambo888@gmail.com"
keyword = "123456789"

# A function to Initialize webdriver with WebDriver Manager
def driver_init():
    
    # Setting custom User-Agent
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={custom_user_agent}")
    options.add_argument("--disable-blink-features=Automation Controlled") # Evades detection
        
    # Setting up Chrome's driver's service & using it to initialize the web driver.
    # service = Service(executable_path="chromedriver.exe")  
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) # Automatically managing c hrome Driver version with webdriver_manager
    return driver

# Login function
def account_login(driver):
    driver.get("https://www.studybay.com/login/")
    
    # Finding Email and Password fields
    mail_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']" )
    keyword_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']" )
    
    mail_field.send_keys(mail)
    keyword_field.send_keys(keyword)
    
    keyword_field.send_keys(Keys.RETURN)
    
    # Wait for login to complete && Adjust the selector to match the one on Studybay
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "")))
    
def place_bid(driver, bid_choice="manual", bid_amount="minimum"):
    try:
        driver.get("https://www.studybay.com/auction/")
        
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
                elif bid_choice == "manual" and custom_bid_amount:
                    bid_amount = custom_bid_amount
                else:
                    print("Invalid bid choice or missing custom bid amount.")
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




# email = "email"
# login_URL = "https://studybay.com/login/" # https://studybay.com/login/

# '''
#     p = ChromiumPage()
#     p.get("https://nowsecure.nl/")
#     i = p.get_frame("@src^https://challenges.cloudflare.com/cdn-cqi")
#     e = i(".mark")
#     sleep(3)
# '''

# # Getting da browser's page && maximizing it.

# driver.get(login_URL)
# driver.maximize_window()

# # Ensure navigation to login-page.
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(By.NAME, email)
# )


# # Studybay Login-Page Elements
# '''
#     * XPATH for Email input field = //input[@placeholder='Email']
#     * XPATH for Password input field = //input[@placeholder='Password']
#     * XPATH for Login button = //button[@type='submit']
# '''


# # Fetching data from Studybay Login-Page


# login_Btn = driver.find_element(By.XPATH, "//button[@type='submit']")


# # Adding values && Logging in.

# mail_field.send_keys(mail)
# keyword_field.send_keys(keyword)
# login_Btn.click()