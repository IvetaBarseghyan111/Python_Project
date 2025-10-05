from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()

    #First point
    first_frame = driver.find_element(By.CSS_SELECTOR, "iframe#frame1")
    driver.switch_to.frame(first_frame)
    text_first_frame = wait.until(EC.visibility_of_element_located((By.ID,"sampleHeading")))
    print(text_first_frame.text)

    driver.switch_to.default_content()
    driver.get("https://demoqa.com/alerts")
    time_alert_button = driver.find_element(By.CSS_SELECTOR, "button#timerAlertButton")
    time_alert_button.click()
    time_alert = wait.until(EC.alert_is_present())
    time_alert.accept()

    #Second_point
    driver.get("https://demoqa.com/browser_windows")
    driver.maximize_window()

    main = driver.current_window_handle
    driver.switch_to.new_window("tab")
    driver.get("https://demoqa.com/alerts")
    info_alert_button = driver.find_element(By.ID, "alertButton")
    info_alert_button.click()
    info_alert = wait.until(EC.alert_is_present())
    info_alert.accept()
    driver.switch_to.window(main)
    print(driver.window_handles)

    #Third point
    driver.get("https://demoqa.com/browser-windows")
    driver.maximize_window()
    main_window = driver.current_window_handle

    new_window_button = wait.until(EC.element_to_be_clickable((By.ID, "windowButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", new_window_button)
    new_window_button.click()
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break
    sample_text = wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading")))
    print(sample_text.text)

    driver.switch_to.window(main_window)
    print(driver.title)

    #Fourth point
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()

    frame_first = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "iframe#frame1")))
    driver.switch_to.frame(frame_first)
    frame_first_text = wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading")))
    print(frame_first_text.text)
    driver.switch_to.default_content()

    frame_second = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "iframe#frame2")))
    driver.switch_to.frame(frame_second)
    frame_second_text = wait.until(EC.visibility_of_element_located((By.ID, "sampleHeading")))
    print(frame_second_text.text)
    driver.switch_to.default_content()

    print("Iframe task completed")

    #Fifth point - Checks of alert is not done yet, should be added later
    driver.get("https://demoqa.com/alerts")
    driver.maximize_window()

    first_alert_button = wait.until(EC.visibility_of_element_located((By.ID, "timerAlertButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", first_alert_button)
    first_alert_button.click()
    first_alert = wait.until(EC.alert_is_present())
    first_alert.accept()

    second_alert_button = wait.until(EC.visibility_of_element_located((By.ID, "confirmButton")))
    second_alert_button.click()
    second_alert = wait.until(EC.alert_is_present())
    second_alert.dismiss()

    third_alert_button = wait.until(EC.visibility_of_element_located((By.ID, "promtButton")))
    third_alert_button.click()
    third_alert = wait.until(EC.alert_is_present())
    third_alert.send_keys("Test")

finally:
    driver.quit()