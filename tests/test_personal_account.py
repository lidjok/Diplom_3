import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest
from data import Url


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет» ')
    def test_login_personal_account(self, driver, create_new_user, login_user):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page.click_on_personal_account_link_header()
        assert self.login_page.find_element_with_wait_PROFILE_PERSONAL_ACC


    @allure.title('Проверка перехода в раздел «История заказов» ')
    def test_click_button_order_history(self, driver, create_new_user, login_user):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page.click_on_personal_account_link_header()
        self.login_page.find_element_with_wait_PROFILE_PERSONAL_ACC()
        self.login_page.click_on_order_history_button_PERSONAL_ACC()
        current_url = self.login_page.check_by_url_personal_acc_order_history()
        assert current_url == Url.ORDER_HISTORY_PA_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_logout_personal_account(self, driver, create_new_user, login_user):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page.click_on_personal_account_link_header()
        self.login_page.find_element_with_wait_PROFILE_PERSONAL_ACC()
        self.login_page.click_on_order_logout_button_PERSONAL_ACC()
        self.login_page.find_element_with_wait_login_authorization_form()
        current_url = self.login_page.check_by_url_login_form()
        assert current_url == Url.LOGIN_FORM_URL