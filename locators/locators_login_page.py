from selenium.webdriver.common.by import By

class LoginPageLocators:
    LINK_RESET_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    FORGOT_PASSWORD_PAGE = By.XPATH, "//h2[text()='Восстановление пароля']"
    INPUT_EMAIL_RECOVERY_FORM = By.XPATH, ".//input[@name = 'name']"
    BUTTON_RECOVER_RECOVERY_FORM = By.XPATH, ".//button[text() = 'Восстановить']"
    INPUT_CODE_RECOVERY_FORM = By.XPATH, "//label[contains(text(), 'Введите код из письма')]"
    BUTTON_HIDE_OR_SHOW_PASSWORD = By.CSS_SELECTOR, 'div.input__icon.input__icon-action'
    INPUT_PASS_RESET_FORM = By.CSS_SELECTOR, ".input.input_status_active"
    INPUT_LOGIN_AUTHORIZATION_FORM = By.XPATH, "//input[@name='name']"
    INPUT_PASSWORD_AUTHORIZATION_FORM = By.XPATH, "//input[@name='Пароль']"
    LOGIN_BUTTON_AUTHORIZATION_FORM = By.XPATH,"//button[contains(text(), 'Войти')]"

    PROFILE_TEXT_PERSONAL_CABINET = By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and contains(text(), 'Профиль')]"
    ORDER_HISTORY_LINK_PERSONAL_CABINET = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive' and contains(text(), 'История заказов')]")
    last_order = By.XPATH, "(//ul[contains(@class, 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB')]/li)[last()]"
    LOGOUT_BUTTON_PERSONAL_ACC = By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']"
    NUMBER_OF_ORDER_IN_HISTORY_PACC = By.XPATH, "//p[@class='text text_type_digits-default' and contains(text()='#0')]"
    text_on_card = By.CSS_SELECTOR, "p.text.text_type_digits-default.mb-10.mt-5"