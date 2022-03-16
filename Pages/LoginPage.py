import time

from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class LoginPage(PageObject):
    URL_LOGIN = "https://www.saucedemo.com/"
    # Page Elements
    id_btn_login = 'login-button'
    class_error_login_msg = 'error-message-container'
    txt_msg_login_error = 'Epic sadface: Username is required'
    txt_standard_user = 'standard_user'
    txt_password_all_users = 'secret_sauce'

    def __init__(self, browser):
        # Abrir browser
        super(LoginPage, self).__init__(browser=browser)
        # Abrir URL de login
        self.open_login_url()

    def open_login_url(self):
        # Abrir URL login
        self.driver.get(self.URL_LOGIN)

    def click_btn_login(self):
        # Procurar e clicar no botão "login"
        self.driver.find_element(By.ID, self.id_btn_login).click()

    def is_url_login_page(self):
        return self.driver.current_url == self.URL_LOGIN

    def has_login_msg_error(self):
        error_message = self.driver.find_element(By.CLASS_NAME, self.class_error_login_msg).text
        return error_message == self.txt_msg_login_error, "Mensagem de erro incorreta!"

    def execute_login(self, username=None, password=None):
        # Se username ou password forem 'None' usar username e password padrão para login.
        if not username:
            username = self.txt_standard_user
        if not password:
            password = self.txt_password_all_users
        # Inserir username e password
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        # Procurar e clicar no botão "login"
        self.click_btn_login()

