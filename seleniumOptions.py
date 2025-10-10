from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def option_selecting(browser): #Function of test browser select
    browser = browser.lower()
    if browser =="google":
        options = ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        #options.add_argument("--user-data-dir=/Users/ivetabarseghyan/ChromeProfiles/AutomationProfile")
        #options.add_argument("--profile-directory=Default")
        return options
    elif browser == "firefox":
       options = FirefoxOptions()
       options.add_argument("--private")
       options.add_argument("--headless")
       return options
    elif browser == "safari":
        options = SafariOptions()
        return options
    else:
        raise ValueError("Unsupported browser name")

def get_browser(browser): #Functio of driver installing depends on function calling by selected browser
    if browser.lower()=="google":
        return webdriver.Chrome(options = option_selecting(browser))
    elif browser.lower()=="firefox":
        return webdriver.Firefox(options = option_selecting(browser))
    elif browser.lower()=="safari":
        return webdriver.Safari(options = option_selecting(browser))

try:
    driver = get_browser("firefox")
    driver.get("https://demoqa.com/")
    assert driver.title == "DEMOQA"
    print("Success")
finally:
    driver.quit()