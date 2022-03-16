import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"


class Test2:
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

    def test_efetuar_login(self, setup):
        print('Inserir username e password')
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        print('Procurar e clicar no botão "login"')
        self.driver.find_element(By.ID, 'login-button').click()

        print('Verificar que a aplicação muda de página')
        assert self.driver.current_url != URL, "A aplicação não mudou de página!"
        print('Verificar o título da página "PRODUTOS"')
        element_class_title = self.driver.find_element(By.CLASS_NAME, 'title')
        assert element_class_title.text == 'PRODUCTS'
        print('Verificar se o menu existe')
        try:
            self.driver.find_element(By.ID, 'react-burger-menu-btn')
        except NoSuchElementException:
            pytest.fail("Menu não foi encontrado!")

        print('Verificar lista de produtos')
        try:
            self.driver.find_element(By.ID, 'inventory_container')
        except NoSuchElementException:
            pytest.fail("Lista de produtos não foi encontrada!")

