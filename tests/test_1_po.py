class Test1:

    def test_click_login_btn(self, login_page_open):
        print('Procurar e clicar no botão "login"')
        login_page_open.click_btn_login()
        print('Verificar que a aplicação permanece na mesma página')
        assert login_page_open.is_url_login_page(), \
            "Página Login não encontrada!"
        print('Verificar mensagem de erro exibida')
        assert login_page_open.has_login_msg_error(), \
            "Mensagem de erro incorreta!"

