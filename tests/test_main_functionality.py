import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.list_of_order_page import ListOfOrder
import pytest
from data import Url


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на «Конструктор» в хэдере')
    def test_click_on_constructor_link_header(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_personal_account_link_header()
        self.main_page.click_on_collect_burger_button_header()
        assert self.main_page.find_element_with_wait_login_button()

    @allure.title('Проверка перехода по клику на ссылку «Лента заказов»  в хэдере')
    def test_click_on_list_of_order_link_header(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_list_of_order_link_header()
        current_url = self.main_page.check_by_url_order_history_page()
        assert current_url == Url.LIST_OF_ORDER_URL

    @allure.title('Проверка- при клике на ингредиент, появится модальное окно с деталями ингридиента')
    def test_click_on_ingredient(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_collect_burger_button_header()
        self.main_page.find_element_with_wait_login_button()
        self.main_page.click_on_ingridient_bread_R2_D3()
        assert self.main_page.find_element_with_wait_text_ingredients_details_modal_window()

    @allure.title('Проверка- модальное окно "Детали ингридиента" закрывается закрывается кликом по крестику')
    def test_click_on_exit_button_detail_ingredient_detail_modal_window(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_collect_burger_button_header()
        self.main_page.find_element_with_wait_login_button()
        self.main_page.click_on_ingridient_bread_R2_D3()
        self.main_page.find_element_with_wait_text_ingredients_details_modal_window()
        self.main_page.click_on_exit_button_ingredient_detail_window()
        assert self.main_page.check_invisible_ingredient_detail_window()

    @allure.title('Проверка- при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_click_on_ingredient_counter_increase(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.open_url()
        counter_element = self.main_page.find_element_with_wait_counter_bun_r2_d3()
        initial_counter_value = int(counter_element.text)
        self.main_page.drug_and_drop_element_bread_R2_D3_in_basket_list()
        updated_counter_value = self.main_page.find_element_with_wait_counter_bun_r2_d3()
        initial_counter_value_update = int(updated_counter_value.text)
        assert initial_counter_value < initial_counter_value_update

    @allure.title('Проверка- залогиненный пользователь может оформить заказ')
    def test_make_order_by_authorized_user_success(self, driver, create_new_user, login_user):
        self.main_page = MainPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_make_order_button()
        assert self.main_page.find_element_with_wait_identifier_of_order()