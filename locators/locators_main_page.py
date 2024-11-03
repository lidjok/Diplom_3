from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    LINK_PERSONAL_CABINET = By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"
    ORDER_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and contains(text(), 'Оформить заказ')]"
    COLLECT_BURGER_BUTTON_HEADER = By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']"
    LIST_OF_ORDER_LINK_HEADER = By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']"

    INGREDIENT_BREAD_R2_D3 = By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains(text(), 'Флюоресцентная булка R2-D3')]"
    fluorescent_bun_for_dropping = By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']"
    TEXT_INGREDIENTS_DETAILS_MODAL_WINDOW = By.CSS_SELECTOR, ".Modal_modal__title_modified__3Hjkd.Modal_modal__title__2L34m.text.text_type_main-large.pl-10"
    BUTTON_EXIT_INGREDIENTS_DETAILS_MODAL_WINDOW = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    COUNTER_BUN_R2_D3 = By.XPATH, "//p[@class='counter_counter__num__3nue1']"

    LINK_COLLECT_BURGER_SAUCER = By.XPATH, "//span[@class='text text_type_main-default' and contains(text(), 'Соусы')]"
    SAUCER_SPICY_X_SAUCER_COLLECT_BURGER = By.XPATH, ".//img[@alt = 'Соус Spicy-X']"
    BASKET_LIST_AREA = By.CSS_SELECTOR, ".BurgerConstructor_basket__29Cd7"
    COUNTER_ELEMENT_SPICY_X_SAUCER_COLLECT_BURGER = By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//p[@class='counter_counter__num__3nue1']"
    MAKE_ORDER_BUTTON = By.XPATH, ".//button[text() = 'Оформить заказ']"
    ORDER_IDENTIFIER_MODAL_WINDOW = By.XPATH, "//p[@class='undefined text text_type_main-medium mb-15' and contains(text(), 'идентификатор заказа')]"
    BUTTON_CLOSE_ORDER_IDENTIFIER_MODAL_WINDOW = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"

    ORDER_NUMBER_IN_IDENTIFIER_MODAL_WINDOW = By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"