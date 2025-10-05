from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()

    #First point.Finds input via child axis, as current node is parent div
    full_name_field = driver.find_element(By.XPATH, "//div[@class='col-md-9 col-sm-12']/child::input[@placeholder="
                                                    "'Full Name']")
    full_name_field.send_keys("John Smith")
    div_parent = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']/parent::div")
    print(div_parent.get_attribute("class"))

    #Second point
    driver.get("https://demoqa.com/radio-button")
    driver.maximize_window()

    label = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='yesRadio']/"
                                                                        "following-sibling::label[@for='yesRadio']")))
    print(label.text)

    #Third point
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()

    home_checkbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, "rct-checkbox")))
    home_checkbox.click()
    find_elements = driver.find_elements(By.XPATH,"//span[@class='rct-title']/following::span")
    print(len(find_elements))

finally:
    driver.quit()

