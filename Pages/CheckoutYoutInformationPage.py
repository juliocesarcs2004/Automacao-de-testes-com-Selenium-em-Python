import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutYourInformationPage(PageObject):
    # Page Elements
    class_title = 'title'
    url = 'https://www.saucedemo.com/checkout-step-one.html'
    id_continue_btn = 'continue'
    txt_page_title = 'CHECKOUT: YOUR INFORMATION'
    id_btn_menu = 'react-burger-menu-btn'
    class_first_name_error = 'error-message-container'
    txt_first_name_error_msg = 'Error: First Name is required'
    id_first_name_field = 'first-name'
    id_last_name_field = 'last-name'
    id_postal_code_field = 'postal-code'

    def __init__(self, driver):
        super(CheckoutYourInformationPage, self).__init__(driver=driver)

    def is_checkout_your_information_page(self):
        # Verify URL page
        is_url_page = self.driver.current_url == self.url
        try:
            # Verificar se o menu existe.
            element_menu = self.driver.find_element(By.ID, self.id_btn_menu)
            # Verificar se o botão CONTINUE existe.
            btn_continue = self.driver.find_element(By.ID, self.id_continue_btn)
            # Verificar título da pagina
            is_title_checkout_page = self.driver.find_element(By.CLASS_NAME, self.class_title).text == self.txt_page_title
            return is_url_page and element_menu and btn_continue and is_title_checkout_page
        except NoSuchElementException:
            return False

    def click_continue_btn(self):
        self.driver.find_element(By.ID, self.id_continue_btn).click()

    def has_first_name_error_msg(self):
        try:
            first_name_error_element = self.driver.find_element(By.CLASS_NAME, self.class_first_name_error).text
            return first_name_error_element == self.txt_first_name_error_msg
        except NoSuchElementException:
            return False

    def confirm_your_information(self, name, last_name, postal_code):
        try:
            # Digitar First Name.
            self.driver.find_element(By.ID, self.id_first_name_field).send_keys(name)
            # Digitar Last Name.
            self.driver.find_element(By.ID, self.id_last_name_field).send_keys(last_name)
            # Digitar Zip/Code.
            self.driver.find_element(By.ID, self.id_postal_code_field).send_keys(postal_code)
            # Click CONTINUE button.
            self.click_continue_btn()
        except NoSuchElementException:
            raise Exception('Não foi possível encontrar os campos para preenchimento correto!')

