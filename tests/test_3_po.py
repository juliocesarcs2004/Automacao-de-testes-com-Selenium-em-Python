import time

import pytest

from Pages.LoginPage import LoginPage
from Pages.MenuPage import MenuPage
from Pages.ProductsPage import ProductsPage


class Test3:
    @pytest.fixture()
    def setup(self):
        print('Abrir página de Login')
        self.login_page = LoginPage(browser='firefox')
        print('Efetuar login')
        self.login_page.execute_login()
        print('Verificar se está na página de "PRODUTOS"')
        self.products_page = ProductsPage(self.login_page.driver)
        assert self.products_page.is_products_page(), "Página de Produtos não encontrada!"
        yield
        print(f'Fechar browser')
        self.login_page.close()

    def test_efetuar_logout(self, setup):
        print(f'Abrir menu')
        self.menu = MenuPage(self.products_page.driver)
        self.menu.open_menu()
        print(f'Verificar que o menu é exibido')
        assert self.menu.is_menu_open(), 'Menu não foi encontrado!'
        print(f'Clicar no item de menu LOGOUT')
        self.menu.click_logout()
        print('Verificar se não está na página de "PRODUTOS"')
        assert not self.products_page.is_products_page(), "Página de Produtos não encontrada!"
        print('Verificar se voltou para página de LOGIN')
        assert self.login_page.is_url_login_page(), "Página Login não encontrada!"
        time.sleep(5)

