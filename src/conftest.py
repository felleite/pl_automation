import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    hub_url = "http://localhost:4444/wd/hub"  # Alterar se necessário

    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )
    
    yield driver  # Retorna o driver para os testes
    driver.quit()  # Fecha o driver após os testes
