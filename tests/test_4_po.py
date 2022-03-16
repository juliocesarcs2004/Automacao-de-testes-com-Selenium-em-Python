import pytest

from Pages.CartPage import CartPage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class Test4:
    @pytest.fixture()
    def setup(self, browser):
        print('Abrir página de Login')
        self.login_page = LoginPage(browser=browser)
        print('Efetuar login')
        self.login_page.execute_login()
        print('Verificar se está na página de "PRODUTOS"')
        self.products_page = ProductsPage(self.login_page.driver)
        assert self.products_page.is_products_page(), "Página de Produtos não encontrada!"
        yield
        print(f'Fechar browser')
        self.login_page.close()

    def test_adicionar_produto_no_carrinho_de_compras(self, setup):
        product_1 = 'Sauce Labs Fleece Jacket'
        print(f'Escolher um produto em clicar em "ADD TO CART"')
        self.products_page.add_product_to_cart_by_name(product_1)
        print('O ícone do carrinho deve aparecer com a numeração "1"')
        assert self.products_page.get_shopping_cart_badge() == '1', 'Numeração 1 não aparece no carrinho de compras!'
        print('Abrir o carrinho de compras')
        self.products_page.open_shopping_cart()
        print('Página de carrinho de compras deve ser exibida')
        self.cart_page = CartPage(self.products_page.driver)
        assert self.cart_page.is_cart_page(), 'Página de carrinho de compras não encontrada!'
        print('O produto selecionado deve ser exibido com item de compra')
        assert self.cart_page.is_product_in_cart_list(product_1), 'Produto não encontrado na lista!'


