import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"


class Test1:
    @pytest.fixture()
    def setup(self):
        print('Abrir browser')
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        print(f'Abrir URL: {URL}')
        self.driver.get(URL)
        yield
        print(f'Fechar browser: {URL}')
        self.driver.quit()

    def test_click_login_btn(self, setup):
        print('Procurar e clicar no botão "login"')
        self.driver.find_element(By.ID, 'login-button').click()
        print('Verificar que a aplicação permanece na mesma página')
        assert self.driver.current_url == URL, \
            "Página requerida não encontrada!"
        print('Verificar mensagem de erro exibida')
        error_message = self.driver.find_element(
            By.CLASS_NAME, 'error-message-container').text
        assert error_message == 'Epic sadface: Username is required',\
            "Mensagem de erro incorreta!"

