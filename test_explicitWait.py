from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']")))
    print("Dynamic content loaded successfully.")


    driver.switch_to.new_window("tab")
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if "dynamic_loading" in driver.current_url :
            driver.close()

    js_alert_button = driver.find_element(By. XPATH, "//button[text()='Click for JS Alert']")
    js_alert_button.click()
    js_alert = wait.until(EC.alert_is_present())
    js_alert.accept()
    result_text = driver.find_element(By.ID, "result")
    print(result_text.text)

    driver.get("https://demoqa.com/automation-practice-form")
    non_existing_element = driver.find_element(By.ID, "ghostButton")
    non_existing_element.click()

except NoSuchElementException:
    print("There is no such element")
finally:
    driver.quit()


