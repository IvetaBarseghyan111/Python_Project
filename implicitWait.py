from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) #As button state changes to enabled after 5sec, by implicit wait it checks button state
    # every time until set time
    driver.get("https://demoqa.com/dynamic-properties")
    element = driver.find_element(By.ID, "enableAfter")
    element.click()
finally:
    driver.quit()

