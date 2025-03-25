from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para rodar sem interface gráfica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Conectar ao Selenium remoto no container
driver = webdriver.Remote(
    command_executor="http://selenium-hub:4444/wd/hub",
    options=options
)

# Teste de navegação
driver.get("https://www.python.org")
print("Título da página:", driver.title)

# Fechar navegador
driver.quit()
