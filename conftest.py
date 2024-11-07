import pytest
from selenium import webdriver
from helpers import generation_new_data_user
from data import UrlApi
from pages.main_page import MainPage
from pages.login_page import LoginPage
import requests

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        ValueError("Can't create instance for this browser param")
    driver.set_window_size(1240, 756)
    yield driver

    driver.quit()

@pytest.fixture
def create_new_user():
    payload = generation_new_data_user()
    response = requests.post(f"{UrlApi.CREATE_USER}", data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(UrlApi.DELETE_USER, headers={"Authorization": token})


@pytest.fixture
def login_user(driver, create_new_user):
        create_user_data = create_new_user[0]
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        main_page.open_url()
        main_page.click_on_personal_account_link_header()
        login_page.fill_authorization_form(create_user_data["email"], create_user_data["password"])
        main_page = MainPage(driver)


@pytest.fixture
def make_order(driver, create_new_user, login_user):
    main_page = MainPage(driver)
    main_page.open_url()
    main_page.drug_and_drop_element_bread_R2_D3_in_basket_list()
    main_page.click_on_make_order_button()
