import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Url
import pytest


class TestLoginForm:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль» ')
    def test_click_recover_password_button(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_login_button()
        self.login_page.click_on_link_reset_password()
        current_url = self.login_page.check_by_url_forgot_password_page()
        assert current_url == Url.FORGOT_PASSWORD_URL


    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить» ')
    def test_input_email_and_click_recover(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_login_button()
        self.login_page.click_on_link_reset_password()
        self.login_page.fill_email_field_recover_form()
        self.login_page.click_on_element_recover_button_rf()
        self.login_page.find_element_with_wait_code()
        current_url = self.login_page.check_by_url_reset_password_page()
        assert current_url == Url.RESET_PASSWORD_URL

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_click_eye_button_hide_or_show_password(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page.open_url()
        self.main_page.click_on_login_button()
        self.login_page.click_on_link_reset_password()
        self.login_page.fill_email_field_recover_form()
        self.login_page.click_on_element_recover_button_rf()
        self.login_page.find_element_with_wait_code()
        self.login_page.click_on_eye_element_hide_or_dhow_password()
        assert self.login_page.find_element_with_wait_code()



