from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def remove_func():
        remove = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
        remove.click()
        remove_check = wait.until(EC.visibility_of_element_located((By.XPATH,"//form[@id='checkbox-example']/p["
                                                                  "@id='message']")))

        assert remove_check.text == "It's gone!"
        print("Remove button was clicked")

    checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[label='blah']")))
    checkbox.click()
    assert checkbox.is_selected()
    print("Checkbox was clicked")

    remove_func()

    add = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
    add.click()
    add_check = wait.until(EC.visibility_of_element_located((By.XPATH,"//form[@id='checkbox-example']/p["
                                                                  "@id='message']")))

    assert add_check.text == "It's back!"
    print("Add button was clicked")

    remove_func()

    #Does not finish yet
    # enable = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Enable']")))
    # enable_verify =wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@id='input-example']/p["
    #                                                                       "@id='message'")))
    #
    # assert enable_verify.text == "It's enabled"
    # print("Enable button was clicked")

    time.sleep(3)


finally:
    driver.quit()