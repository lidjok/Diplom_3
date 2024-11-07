from pages.base_page import BasePage
from locators.locators_main_page import MainPageLocators
from data import default_order_value

import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Клик по кнопке "Личный кабинет0" в хэдере')
    def click_on_personal_account_link_header(self):
        self.click_on_element(MainPageLocators.LINK_PERSONAL_CABINET)

    @allure.step('Проверка отображения кнопки "Заказать" на главной странице сайта')
    def find_element_with_wait_oder_button(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON)

    @allure.step('Клик по кнопке "Конструктор" в хэдере')
    def click_on_collect_burger_button_header(self):
        self.click_on_element(MainPageLocators.COLLECT_BURGER_BUTTON_HEADER)

    @allure.step('Проверка отображения кнопки "Войти в аккаунт" на главной странице сайта')
    def find_element_with_wait_login_button(self):
        return self.find_element_with_wait(MainPageLocators.BUTTON_LOGIN)

    @allure.step('Клик по ссылке "Лента Заказов" в хэдере')
    def click_on_list_of_order_link_header(self):
        self.click_on_element(MainPageLocators.LIST_OF_ORDER_LINK_HEADER)

    @allure.step('Клик по нгридиенту Флюоресцентная булка R2-D3')
    def click_on_ingridient_bread_R2_D3(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BREAD_R2_D3)

    @allure.step('Проверка отображения текста Детали ингридиента в модальном окне')
    def find_element_with_wait_text_ingredients_details_modal_window(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_INGREDIENTS_DETAILS_MODAL_WINDOW)

    @allure.step('Проверка невидимости элемнта Модальное окно "Детали ингридиента"')
    def check_invisible_ingredient_detail_window(self):
        return self.check_element_is_not_visible(MainPageLocators.TEXT_INGREDIENTS_DETAILS_MODAL_WINDOW)

    @allure.step('Проверка отображения текста Детали ингридиента в модальном окне')
    def find_element_with_wait_text_ingredients_details_modal_window(self):
        return self.find_element_with_wait(MainPageLocators.TEXT_INGREDIENTS_DETAILS_MODAL_WINDOW)

    @allure.step('Клик по конке-крестик в модальном окне "Детали ингридиента"')
    def click_on_exit_button_ingredient_detail_window(self):
        self.click_on_element(MainPageLocators.BUTTON_EXIT_INGREDIENTS_DETAILS_MODAL_WINDOW)

    @allure.step('Переход в раздел "Соусы" в конструкторе бургеров')
    def click_on_link_saucer_burger_constructor(self):
        self.click_on_element(MainPageLocators.LINK_COLLECT_BURGER_SAUCER)

    @allure.step('Drug and drop лемента соус spicy x в корзину')
    def drug_and_drop_element_spicy_x_saucer_in_basket_list(self):
        self.drug_and_drop_element(MainPageLocators.SAUCER_SPICY_X_SAUCER_COLLECT_BURGER, MainPageLocators.BASKET_LIST_AREA)


    @allure.step('Находим элемент Счетчик ингридиента SPICY_X_SAUCER')
    def find_element_with_wait_counter_SPICY_X_SAUCER(self):
        return self.find_element_with_wait(MainPageLocators.COUNTER_ELEMENT_SPICY_X_SAUCER_COLLECT_BURGER)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_make_order_button(self):
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверка появление окна "идентификатор заказа"')
    def find_element_with_wait_identifier_of_order(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_IDENTIFIER_MODAL_WINDOW)

    @allure.step('Клик по кнопке закрытия модального окна "идентификатор заказа"')
    def click_on_close_button_identifier_modal_window(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_ORDER_IDENTIFIER_MODAL_WINDOW)


    @allure.step('Drug and drop лемента булочка x в корзину')
    def drug_and_drop_element_bread_R2_D3_in_basket_list(self):
        self.drug_and_drop_element(MainPageLocators.fluorescent_bun_for_dropping, MainPageLocators.BASKET_LIST_AREA)

    @allure.step('Ждем и забираем номер заказа с главной страницы')
    def wait_to_get_actual_order_number(self):
        return self.get_order_numbers(
            locator=MainPageLocators.ORDER_NUMBER_IN_IDENTIFIER_MODAL_WINDOW,
            default_value=default_order_value
        )

    @allure.step('Проверка нахождения на странице "История заказов" по URL')
    def check_by_url_order_history_page(self):
        return self.get_current_url()

    @allure.step('Находим элемент Счетчик ингридиента улочка R2 D3')
    def find_element_with_wait_counter_bun_r2_d3(self):
        return self.find_element_with_wait(MainPageLocators.COUNTER_BUN_R2_D3)

