import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#Fixture of webdriver create with different browsers and options
@pytest.fixture (params = ["google", "firefox", "safari"])
def driver(request):
    browser =  request.param
    if browser == "google":
        options = ChromeOptions()
        #options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options = options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options = options)
    elif browser == "safari":
        options = SafariOptions()
        driver = webdriver.Safari(options = options)
    else:
        raise ValueError("Unsupported browser name")

    #driver.implicitly_wait()
    yield driver
    driver.quit()

#Fixture of wait object
@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)

