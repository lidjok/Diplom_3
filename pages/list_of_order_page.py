from pages.base_page import BasePage
from locators.locators_list_of_order import ListOfOrderLocators


import allure

class ListOfOrder(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка отображения заголовка "Лента Заказов"')
    def find_element_with_wait_text_list_of_order(self):
        return self.find_element_with_wait(ListOfOrderLocators.TEXT_LIST_OF_ORDER)

    @allure.step('Клик по карточке оформленного заказа в списке заказов')
    def click_on_card_of_order_in_list(self):
        self.click_on_element(ListOfOrderLocators.IMAGE_ON_CARD_OF_ORDER_IN_LIST_OF_ORDER)

    @allure.step('Проверка отображения номера заказа при открытии карточки заказа в Списке заказов')
    def find_element_with_wait_text_list_of_order(self):
        return self.find_element_with_wait(ListOfOrderLocators.ORDER_NUMBER_IN_CARD_OF_ORDER)

    @allure.step('Забираем из карточки заказа в Списке заказов номер заказа')
    def get_text_number_of_order_from_card(self):
        return self.get_text_from_element(ListOfOrderLocators.ORDER_NUMBER_IN_CARD_OF_ORDER)

    @allure.step('Закрываем карточку заказа в Списке заказов')
    def click_on_card_of_order_close(self):
        self.click_on_element(ListOfOrderLocators.BUTTON_EXIT_ORDER_DETAILS_MODAL_WINDOW)

    allure.step('Находим элемент - число заказов за все время на странице Список заказов')
    def find_element_with_wait_text_number_off_orders_all(self):
        return self.find_element_with_wait(ListOfOrderLocators.CREATED_ORDERS_FOL_ALL_TIME)

    def find_element_with_wait_text_number_off_orders_for_today(self):
        return self.find_element_with_wait(ListOfOrderLocators.CREATED_ORDERS_FOR_TODAY)

    @allure.step('Получаем номер заказа который в статусе "В работе"')
    def get_order_in_work(self, expected_value):
        return self.get_orders_in_work(locator=ListOfOrderLocators.ORDERS_IN_WORK, expected_value=expected_value)

    @allure.step('Проверяем текст на странице Список заказов')
    def check_order_number_in_order_list(self, expected_value):
        return self.check_text_on_page()