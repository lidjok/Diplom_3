from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self):
        self.driver.get(self.BASE_URL)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_into_view(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def find_element_with_wait(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def find_to_be_clickable_element_with_wait(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))


    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    def get_current_url(self):
        return self.driver.current_url

        # Проверка отображения элемента ('элемент не виден)
    def check_element_is_not_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def drug_and_drop_element(self, element_one, element_two):
        source_element = self.driver.find_element(*element_one)
        target_element = self.driver.find_element(*element_two)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def check_text_on_page(self):
        return self.driver.page_source

    def get_order_numbers(self, locator, default_value):
        WebDriverWait(self.driver, 25).until(
            lambda driver: driver.find_element(*locator).text != default_value
        )
        return self.driver.find_element(*locator).text

    def get_orders_in_work(self, locator, expected_value):
        WebDriverWait(self.driver, 25).until(
            lambda driver: driver.find_element(*locator).text == f'0{expected_value}'
        )
