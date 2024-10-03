# Handles the captcha : cloudflare captcha

# Imports:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# Logic:
def access_shadow_dom_element(driver):
    try:
        driver.get("https://challenges.cloudflare.com/cdn-cgi/challenge-platform/h/g")
        time.sleep(7)
        
        shadow_host = driver.find_element(By.CSS_SELECTOR, "")
        shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        
        # Find and click the captcha checkbox
        checkbox = shadow_root.find_element(By.CSS_SELECTOR, " ")
        WebDriverWait(driver, 23).until(EC.element_to_be_clickable(checkbox))
        checkbox.click()
        
        print("CAPTCHA verified.")
    except TimeoutException:
        print("CAPTCHA not Verified.")    
