
from Pages.ProductsPage import ProductsPage


class Test2:
    def test_efetuar_login(self, login_page_open):
        print('Efetuar login')
        login_page_open.execute_login()

        print('Verificar se a aplicação muda de página')
        assert not login_page_open.is_url_login_page(), "Página de Login permanece a mesma!"

        print('Verificar se está na página de "PRODUTOS"')
        products_page = ProductsPage(login_page_open.driver)
        assert products_page.is_products_page(), "Página de Produtos não encontrada!"

        print('Verificar lista de produtos')
        assert products_page.get_products_list(), "Lista de produtos não foi encontrada!"
