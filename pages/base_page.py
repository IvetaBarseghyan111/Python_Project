from selenium.webdriver.support import expected_conditions as EC

# Base class that initializes a new WebDriver and WebDriverWait instance for each test.This class also contains
# common reusable actions
class BasePage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def open_page(self, url):
        self.driver.get(url)

    def scroll_into_view(self, argument):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", argument)

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def element_click(self, locator):
        element = self.wait_until_clickable(locator)
        self.scroll_into_view(element)
        element.click()

    def element_click_with_implicit_wait(self,locator):
        element = self.driver.find_element(*locator)
        self.scroll_into_view(element)
        element.click()
    
    def send_keys(self,by,locator,text):
        element = self.driver.find_element(by,locator)
        element.send_keys(text)
        