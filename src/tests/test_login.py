import pytest
from pages.login_page import LoginPage
from utils.navigation import Navigation
from utils.user_data import USER_DATA

def test_login(driver):
    nav = Navigation(driver)
    nav.go_to("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login(USER_DATA["username"], USER_DATA["password"])

    assert "inventory" in driver.current_url
