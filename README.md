# Gud-Poop

An automating agent for Studybay, focussed on optimized movements and speedy interactions to bid, confirm assignments, confirm 50% and schedule withdrawals. Advanced features include: tracking rating, offer tips on how to increase the rating, Request for review from client, withdraw to crypto [binance], Account Analytics.


## Basic Outline 

Python libraries:
    * selenium for browser automation
    * BeautifulSoup for web scraping

### Prerequisites
    * Python installed on your machine.
    * Seleninum library installed, use `pip install selenium`
    * BeautifulSoup library installed, use `pip install beautifulsoup4`
    * WebDriver for your browser, eg. ChromeDriver for Google chrome.


#### Imports

1. Selenium's webdriver
2. ChromeDriver, a separate executable that Selenium WebDriver uses to control Chrome. [ downloaded separately]
3. `service` from ChromeDriver.
4. `ChromeDriverManager`
5. WebDriver's `By`
6. WebDriver's common `Keys`
7. `WebDriverWait`
8. WebDriver's `expected_conditions`
9. Common Selenium exceptions

### Installing Selenium

### Beautiful Soup

`apt-get install python3-bs4` : Install Beautiful Soup
One can install using pip or easy_install, package name is `beautifulsoup4` 
    `pip3 install beautifulsoup4`
    `easy_install beautifulsoup4`

Installing a parser:
    Beautiful Soup supports a number of parsers, including the HTML parser in Python's standard library. Different parsers have their pros and cons.

    1. Python's html.parser : Batteries included. Decent speed > Not that fast. Less lenient
    2. lxml's HTML parser : Very fast > External C dependency
    3. lxml's XML parser: Very fast. Only supported XML parser atm. > External C dependency.

    `pip install lxml` 



### Studybay Page

Studybay is an online assignment help service where authors provide their services in writing. This could be in Engineering, Nursing, or any other field.
The platform aims to help ambitious students balance their workload and avoid stress.

Key Features
* Verified Experts: Studybay engages alumni of top universities and colleges to become experts on the platform. Each one of them being carefully checked for their academic and professional background.
* Studybay's system is AI based, to analyze the quality of each expert's performance and form a rating based on the data collected and reviews from clients.
* Studybay encrypts all personal data to ensure security and privacy of users is withheld.
* The platform emphasizes cooperation between students and experts, allowing for personal attention & suggestions for corrections.

Process Flow
This is a detailed, step by step procedure on how to navigate through studybay website.
    1. Once you go to Studybay's website, one is prompted to either sign in or sign up.

    https://studybay.com/

    https://studybay.com/login/ : Login Page

    https://studybay.com/order/search : Auction page.
