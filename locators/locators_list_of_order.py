from selenium.webdriver.common.by import By


class ListOfOrderLocators:

    TEXT_LIST_OF_ORDER = By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-5']"
    IMAGE_ON_CARD_OF_ORDER_IN_LIST_OF_ORDER = By.XPATH, "//img[@alt='Флюоресцентный бургер']"
    ORDER_NUMBER_IN_CARD_OF_ORDER = By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5' and contains(text(), '#')]"
    BUTTON_EXIT_ORDER_DETAILS_MODAL_WINDOW = By.XPATH, "//button[@type='button' and contains(@class, 'Modal_modal__close')]"
    CREATED_ORDERS_FOL_ALL_TIME = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    CREATED_ORDERS_FOR_TODAY = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    ORDERS_IN_WORK = [By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"]