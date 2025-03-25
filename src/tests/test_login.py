import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage



@pytest.fixture
def driver():
    options = Options()
    hub_url = "http://localhost:4444/wd/hub"  # ou o IP do seu servidor

    #options.add_argument("--headless")  # Rodar sem interface gráfica
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options  # Passando as opções diretamente
    )
    
    yield driver  # A fixture vai retornar o driver para os testes
    driver.quit()  # Após os testes, o driver será fechado

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url