from pages.base_page import BasePage
from locators.locators_login_page import LoginPageLocators
from helpers import Person
import allure

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по ссылке "Восстановить пароль"')
    def click_on_link_reset_password(self):
        self.click_on_element(LoginPageLocators.LINK_RESET_PASSWORD)

    @allure.step('Проверка нахождения на странице "Восстановить пароль" по URL c полем "email"')
    def check_by_url_forgot_password_page(self):
        return self.get_current_url()

    @allure.step('Проверка нахождения на странице "Восстановить пароль" по URL с полями "Пароль" и "Код"')
    def check_by_url_reset_password_page(self):
        return self.get_current_url()

    @allure.step('Ввод mail в форме восстановления пароля')
    def fill_email_field_recover_form(self):
        self.person = Person()
        self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL_RECOVERY_FORM).send_keys(self.person.generate_random_email())

    @allure.step('Клик по кнопке "Восстановить"  форме восстановления пароля')
    def click_on_element_recover_button_rf(self):
        self.click_on_element(LoginPageLocators.BUTTON_RECOVER_RECOVERY_FORM)

    @allure.step('ждем поля code')
    def find_element_with_wait_code(self):
        return self.find_element_with_wait(LoginPageLocators.INPUT_CODE_RECOVERY_FORM)

    @allure.step('Клик по иконке-кнопке отображения/скрытия пароля')
    def click_on_eye_element_hide_or_dhow_password(self):
        self.click_on_element(LoginPageLocators.BUTTON_HIDE_OR_SHOW_PASSWORD)

    @allure.step('Форма Авторизации. Заполняем поля Email')
    def fill_email_field_authorization_form(self, email):
        self.find_element_with_wait(LoginPageLocators.INPUT_LOGIN_AUTHORIZATION_FORM).send_keys(email)

    @allure.step('Форма Авторизации. Заполняем поля Password')
    def fill_password_field_authorization_form(self, password):
        self.find_element_with_wait(LoginPageLocators.INPUT_PASSWORD_AUTHORIZATION_FORM).send_keys(password)

    @allure.step('Форма авторизации. Клик по кнопке "Войти"')
    def click_on_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON_AUTHORIZATION_FORM)

    @allure.step('Форма Авторизации. Login пользователя')
    def fill_authorization_form(self, email, password):
        self.fill_email_field_authorization_form(email)
        self.fill_password_field_authorization_form(password)
        self.click_on_login_button()

    @allure.step('Личный кабинет. ждем отображения ссылки "Профиль"' )
    def find_element_with_wait_PROFILE_PERSONAL_ACC(self):
        self.find_element_with_wait(LoginPageLocators.PROFILE_TEXT_PERSONAL_CABINET)

    @allure.step('Личный кабинет. Клик по кнопке "История Заказов"')
    def click_on_order_history_button_PERSONAL_ACC(self):
        self.click_on_element(LoginPageLocators.ORDER_HISTORY_LINK_PERSONAL_CABINET)

    @allure.step('Проверяем url - ручка account/order-history')
    def check_by_url_personal_acc_order_history(self):
        return self.get_current_url()

    @allure.step('Личный кабинет. Клик по кнопке "Выход"')
    def click_on_order_logout_button_PERSONAL_ACC(self):
        self.click_on_element(LoginPageLocators.LOGOUT_BUTTON_PERSONAL_ACC)


    @allure.step('Проверяем url - ручка /login')
    def check_by_url_login_form(self):
        return self.get_current_url()

    @allure.step('Проверка видимости кнопки "Войти" в форме Авторизации')
    def find_element_with_wait_login_authorization_form(self):
        self.find_element_with_wait(LoginPageLocators.LOGIN_BUTTON_AUTHORIZATION_FORM)

    @allure.step('Находим в Истории заказов последний текст и получаем с него номер')
    def find_last_order_in_history_and_get_it_number(self):
        self.click_on_element(LoginPageLocators.last_order)

    @allure.step('Находим в Истории заказов на карточке номер заказа')
    def get_text_from_element_card_of_order_per_acc(self):
        self.get_text_from_element(LoginPageLocators.text_on_card)

    @allure.step('Находим в Истории заказов на карточке номер заказа')
    def click_on_element_element_card_of_order_per_acc(self):
        self.click_on_element(LoginPageLocators.last_order)

    @allure.step('Проверяем текст на странице Кабинет/история заказов')
    def check_order_in_history(self, expected_value):
        return self.check_text_on_page()