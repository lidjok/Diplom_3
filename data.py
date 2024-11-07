
class Url:
    FORGOT_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    RESET_PASSWORD_URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    ORDER_HISTORY_PA_URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
    LOGIN_FORM_URL = 'https://stellarburgers.nomoreparties.site/login'
    LIST_OF_ORDER_URL = 'https://stellarburgers.nomoreparties.site/feed'

class UrlApi:
    URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{URL}/api/auth/register'
    DELETE_USER = f'{URL}/api/auth/user'

default_order_value = '9999'