from pages import web_element_click_page
import time

# Test for opening the main page and clicking the "Elements" card.
def test_element_click (driver, wait):
    test_element_click_func = web_element_click_page.ElementClick(driver, wait)
    test_element_click_func.open_element_page()
    test_element_click_func.click_element_card()
    assert "elements" in driver.current_url

# Test for navigating to and clicking the "Buttons" section.
def test_button_click(driver, wait):
    test_button_click_func = web_element_click_page.ButtonClick(driver, wait)
    test_button_click_func.open_button_page()
    test_button_click_func.click_button_card()
    assert "buttons" in driver.current_url

# Test for clicking the "Click Me" button and verifying the result message.
def test_click_me_button_click(driver, wait):
    click_me_button_func = web_element_click_page.ClickMeButtonClick(driver, wait)
    click_me_button_func.open_click_me_button_page()
    click_me_button_func.click_me_button_click()
    assert click_me_button_func.button_verify().is_displayed(), print("Click me button was clicked")

# Test for clicking the "Impressive" radio button and verifying the result.
def test_radio_button_click(driver,wait):
    radio_button_click_func = web_element_click_page.RadioButtonClick(driver, wait)
    radio_button_click_func.open_radio_button_page()
    radio_button_click_func.click_radio_button()

    assert radio_button_click_func.radio_button_verify().text == "Impressive", print("Radio Button was clicked")

# Test for opening the "Links" page and printing all available links.
def test_link_click(driver,wait):
    link_click_func = web_element_click_page.LinkClick(driver, wait)
    link_click_func.open_link_page()
    link_click_func.click_link()

# Test for implicit wait, assertion is done by changing implicit wait value in conftest.py.But as the problem of webpage
# it does not matter used wait or not button is clickable
def test_click_implicit_wait(driver, wait):
    click_implicit_wait_func = web_element_click_page.ImplicitWait(driver, wait)
    click_implicit_wait_func.open_page_dynamic_properties()
    click_implicit_wait_func.dynamic_property_click()
    time.sleep(3)

def test_non_exist_button_click(driver,wait):
    non_exist_button_func = web_element_click_page.NonExistingButton(driver, wait)
    non_exist_button_func.open_non_exist_button_page()
    non_exist_button_func.non_exist_button_click()


