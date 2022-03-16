import pytest

from Pages.CartPage import CartPage
from Pages.CheckoutCompletePage import CheckoutCompletePage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
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
        yield product_1
        print(f'Fechar browser')
        self.login_page.close()

    def test_checkout_vazio(self, setup):
        print('Clicar em "CHECKOUT"')
        self.cart_page.click_checkout_btn()
        print('Página "CHECKOUT: YOUR INFORMATION" deve ser exibida.')
        self.checkout_your_info_page = CheckoutYourInformationPage(self.cart_page.driver)
        assert self.checkout_your_info_page.is_checkout_your_information_page(), 'Página não encontrada!'
        print('Preencher os campos: First Name, Last Name e Zip/Postal Code e clicar em "CONTINUE"')
        self.checkout_your_info_page.confirm_your_information('Joao', 'da Silva', '51000210')
        print('A aplicação deve exibir a página de "CHECKOUT: OVERVIEW".')
        self.checkout_overview_page = CheckoutOverviewPage(self.checkout_your_info_page.driver)
        assert self.checkout_overview_page.is_checkout_overview_page(), 'Página "CHECKOUT: OVERVIEW" não encontrada!'
        print('Confirmar os dados do pedido.')
        # The fixture setup returned the name of product_1 variable.
        assert self.checkout_overview_page.is_checkout_products_correct([setup]),\
            "Lista de produtos no CHECKOUT OVERVIEW incorreta!"
        print('Clicar em  "FINISH" para finalizar a compra.')
        self.checkout_overview_page.click_finish_btn()

        print('A aplicação deve exibir a página de "CHECKOUT: COMPLETE!".')
        self.checkout_complete_page = CheckoutCompletePage(self.checkout_overview_page.driver)
        assert self.checkout_complete_page.is_checkout_complete_page(), 'Página "CHECKOUT: COMPLETE!" não encontrada!'

        print('Uma mensagem de agradecimento deve ser exibida.')
        assert self.checkout_complete_page.has_thank_you_for_your_order_message(), \
            'Mensagem de agradecimento não encontrada!'