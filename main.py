from selenium import webdriver
import time

def main_test(driver):
    driver.get("https://www.armstqb.org/")
    driver.maximize_window()
    time.sleep(2)

    chrome_title = driver.title
    assert chrome_title == "ArmSTQB"
    print("Test of title verify is passed")

    driver.switch_to.new_window("tab")
    driver.get("https://www.armstqb.org/partners")
    time.sleep(2)

    url = driver.current_url
    assert url == "https://www.armstqb.org/partners"
    print("Test of URL verify is passed")
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.minimize_window()
    time.sleep(2)

    driver.quit()

print("Test with Chrome browser")
chrome_driver = webdriver.Chrome()
main_test(chrome_driver)

print("Test with Firefox browser")
firefox_driver = webdriver.Firefox()
main_test(firefox_driver)

print("Test with Safari browser")
safari_driver = webdriver.Safari()
main_test(safari_driver)