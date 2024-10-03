# Handles Initialization of WebDriver

# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def driver_init(custom_user_agent):
    # Chrome-Options with custom user-agent, disabled blink features, headless browsing.
    options = Options()
    
    options.add_argument(f"user-agent={custom_user_agent}")
    options.add_argument("--disable-blink-features=Automation Controlled")
    # options.headless = True 
    
    # Initialization.
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

driver_init()
print("Success!")