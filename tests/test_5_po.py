import pytest

from Pages.CartPage import CartPage
from Pages.CheckoutYoutInformationPage import CheckoutYourInformationPage
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


class Test5:
    @pytest.fixture()
    def setup(self, browser):
        print('Abrir página de Login')
        self.login_page = LoginPage(browser=browser)
        print('Efetuar login')
        self.login_page.execute_login()
        print('Verificar se está na página de "PRODUTOS"')
        self.products_page = ProductsPage(self.login_page.driver)
        product_1 = 'Sauce Labs Fleece Jacket'
        print(f'Escolher um produto em clicar em "ADD TO CART"')
        self.products_page.add_product_to_cart_by_name(product_1)
        print('Abrir o carrinho de compras')
        self.products_page.open_shopping_cart()
        print('O produto selecionado deve ser exibido com item de compra')
        self.cart_page = CartPage(self.products_page.driver)
        assert self.cart_page.is_product_in_cart_list(product_1), 'Produto não encontrado na lista!'
        yield
        print(f'Fechar browser')
        self.login_page.close()

    def test_checkout_vazio(self, setup):
        print('Clicar em "CHECKOUT"')
        self.cart_page.click_checkout_btn()
        print('Página "CHECKOUT: YOUR INFORMATION" deve ser exibida.')
        self.checkout_your_info_page = CheckoutYourInformationPage(self.cart_page.driver)
        assert self.checkout_your_info_page.is_checkout_your_information_page(), 'Página não encontrada!'
        print('Clicar em "CONTINUE')
        self.checkout_your_info_page.click_continue_btn()
        print('A aplicação deve permanecer na mesma página')
        assert self.checkout_your_info_page.is_checkout_your_information_page(), 'A aplicação mudou de página!'
        print('A mensagem de erro deve ser exibida: "Error: First Name is required"')
        assert self.checkout_your_info_page.has_first_name_error_msg(), 'Mensagem de erro não encontrada!'


