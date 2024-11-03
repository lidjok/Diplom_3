import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.list_of_order_page import ListOfOrder
import pytest


class TestListOfOrder:
    @pytest.fixture(autouse=True)
    def setup(self, driver):

        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.list_of_order_page = ListOfOrder(driver)
        self.main_page.open_url()

    @allure.title('Проверка - при клике на заказ, откроется всплывающее окно с деталями')
    def test_make_order_authorized_user(self, driver, make_order):
        self.main_page.wait_to_get_actual_order_number()
        self.main_page.click_on_close_button_identifier_modal_window()
        self.main_page.click_on_list_of_order_link_header()
        self.list_of_order_page.click_on_card_of_order_in_list()
        assert self.list_of_order_page.find_element_with_wait_text_list_of_order()

    @allure.title('Проверка - заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов». роверяем сравнением значений через полученнный номер нового заказа')
    def test_orders_number_in_iw_similar_in_order_history(self, driver, make_order):
        get_number_of_new_order = self.main_page.wait_to_get_actual_order_number()
        self.main_page.click_on_close_button_identifier_modal_window()
        self.main_page.click_on_personal_account_link_header()
        self.login_page.click_on_order_history_button_PERSONAL_ACC()
        self.login_page.check_order_in_history(get_number_of_new_order)
        self.main_page.click_on_list_of_order_link_header()
        assert self.list_of_order_page.check_order_number_in_order_list(get_number_of_new_order)


    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_make_order_counter_of_all_orders_increase(self, driver, create_new_user, login_user):
        self.main_page.click_on_list_of_order_link_header()
        counter_element_before_order = self.list_of_order_page.find_element_with_wait_text_number_off_orders_all()
        initial_counter_value = int(counter_element_before_order.text)
        self.main_page.click_on_collect_burger_button_header()
        self.main_page.drug_and_drop_element_bread_R2_D3_in_basket_list()
        self.main_page.click_on_make_order_button()
        self.main_page.wait_to_get_actual_order_number()
        self.main_page.click_on_close_button_identifier_modal_window()
        self.main_page.click_on_list_of_order_link_header()
        counter_element_after_order = self.list_of_order_page.find_element_with_wait_text_number_off_orders_all()
        initial_counter_value_2 = int(counter_element_after_order.text)
        assert initial_counter_value < initial_counter_value_2

    @allure.title('роверка - при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_make_order_counter_of_today_orders_increase(self, driver, create_new_user, login_user):
        self.main_page.open_url()
        self.main_page.click_on_list_of_order_link_header()
        counter_element_before_order = self.list_of_order_page.find_element_with_wait_text_number_off_orders_for_today()
        initial_counter_value = int(counter_element_before_order.text)
        self.main_page.click_on_collect_burger_button_header()
        self.main_page.drug_and_drop_element_bread_R2_D3_in_basket_list()
        self.main_page.click_on_make_order_button()
        self.main_page.wait_to_get_actual_order_number()
        self.main_page.click_on_close_button_identifier_modal_window()
        self.main_page.click_on_list_of_order_link_header()
        counter_element_after_order = self.list_of_order_page.find_element_with_wait_text_number_off_orders_for_today()
        initial_counter_value_2 = int(counter_element_after_order.text)
        assert initial_counter_value < initial_counter_value_2

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_make_order_number_in_list_in_status_at_work(self, driver, create_new_user, login_user):
        self.main_page.drug_and_drop_element_bread_R2_D3_in_basket_list()
        self.main_page.click_on_make_order_button()
        expected_value = self.main_page.wait_to_get_actual_order_number()
        self.main_page.click_on_close_button_identifier_modal_window()
        self.main_page.click_on_list_of_order_link_header()
        self.list_of_order_page.get_order_in_work(expected_value)

