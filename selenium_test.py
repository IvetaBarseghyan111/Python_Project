from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://demoqa.com/")
    driver.maximize_window()

    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[text()='Elements']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    time.sleep(2)

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Buttons']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    button.click()

    click_me_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click Me']")))
    driver.execute_script("arguments[0].scrollIntoView(true);",click_me_button)
    click_me_button.click()
    time.sleep(2)

    click_me_button_verify = driver.find_element(By.CSS_SELECTOR,"#dynamicClickMessage")
    assert click_me_button_verify.is_displayed()
    print("Click me button was clicked")

    driver.switch_to.new_window("tab")
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)

    radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label.custom-control-label["
                                                                   "for='impressiveRadio']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    find_radio_button_verify = driver.find_element(By.CSS_SELECTOR, "span.text-success")
    assert find_radio_button_verify.text == "Impressive"
    print("Radio Button was clicked")
    time.sleep(2)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://demoqa.com/buttons")

    links = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Links']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", links)
    links.click()

    links_text = driver.find_elements(By.XPATH, '//p/a')

    for link in links_text:
        print(link.text)
finally:
    driver.quit()
