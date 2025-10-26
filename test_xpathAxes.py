from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_parent_child_axes(driver, wait):
    #First point.Finds input via child axis, as current node is parent div
    driver.get("https://demoqa.com/text-box")
    full_name_field = driver.find_element(By.XPATH, "//div[@class='col-md-9 col-sm-12']/child::input[@placeholder="
                                                    "'Full Name']")
    full_name_field.send_keys("John Smith")
    div_parent = driver.find_element(By.XPATH, "//input[@placeholder='Full Name']/parent::div")
    print(div_parent.get_attribute("class"))

def test_sibling_axes(driver, wait):
    driver.get("https://demoqa.com/radio-button")
    label = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='yesRadio']/""following-sibling::label"
                                                                   "[@for='yesRadio']")))
    print(label.text)

def test_following_axes(driver,wait):
    driver.get("https://demoqa.com/checkbox")
    home_checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "rct-checkbox")))
    home_checkbox.click()
    find_elements = driver.find_elements(By.XPATH,"//span[@class='rct-title']/following::span")
    print(len(find_elements))

