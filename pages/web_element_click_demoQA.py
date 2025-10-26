from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

# Page for clicking the "Elements" card.
class ElementClick(BasePage):
    ELEMENT_CARD = (By.XPATH, "//h5[text()='Elements']")
    def open_element_page(self):
        self.open_page("https://demoqa.com/")
    def click_element_card(self):
        self.element_click(self.ELEMENT_CARD)

# Page for clicking the "Buttons" section.
class ButtonClick(BasePage):
    BUTTON_CARD = (By.XPATH, "//span[text()='Buttons']")
    def open_button_page(self):
        self.open_page("https://demoqa.com/elements")
    def click_button_card(self):
        self.element_click(self.BUTTON_CARD)

# Page for interacting with the "Click Me" button.
class ClickMeButtonClick(BasePage):
    CLICK_ME_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    VERIFY_TEXT_ELEMENT = (By.CSS_SELECTOR, "#dynamicClickMessage")

    def open_click_me_button_page(self):
        self.open_page("https://demoqa.com/buttons")
    def click_me_button_click(self):
        self.element_click(self.CLICK_ME_BUTTON)
    def button_verify(self):
        return self.wait.until(EC.visibility_of_element_located(self.VERIFY_TEXT_ELEMENT))


# Page for interacting with radio buttons.
class RadioButtonClick(BasePage):
    RADIO_BUTTON = (By.CSS_SELECTOR, "label.custom-control-label[for='impressiveRadio']")
    RADIO_BUTTON_VERIFY = (By.CSS_SELECTOR, "span.text-success")

    def open_radio_button_page(self):
        self.open_page("https://demoqa.com/radio-button")

    def click_radio_button(self):
        self.element_click(self.RADIO_BUTTON)

    def radio_button_verify(self):
        return self.wait.until(EC.visibility_of_element_located(self.RADIO_BUTTON_VERIFY))

# Page for interacting with the "Links" section.
class LinkClick(BasePage):
    LINK_ELEMENT = (By.XPATH, "//span[text()='Links']")
    TEXT_AFTER_LINK = (By.XPATH, '//p/a')
    def open_link_page(self):
        self.open_page("https://demoqa.com/links")

    def click_link(self):
        self.element_click(self.LINK_ELEMENT)
        links = self.driver.find_elements(*self.TEXT_AFTER_LINK)
        for link in links:
            print(link.text)

#Page for implicit wait test
class ImplicitWait(BasePage):
    ENABLE_AFTER = (By.ID, "enableAfter")
    def open_page_dynamic_properties(self):
        self.open_page("https://demoqa.com/dynamic-properties")

    def dynamic_property_click(self):
        self.element_click_with_implicit_wait(self.ENABLE_AFTER)

class NonExistingButton(BasePage):
    NON_EXIST_BUTTON = (By.ID, "ghostButton")

    def open_non_exist_button_page(self):
        self.open_page("https://demoqa.com/automation-practice-form")

    def non_exist_button_click(self):
        self.element_click(self.NON_EXIST_BUTTON)


