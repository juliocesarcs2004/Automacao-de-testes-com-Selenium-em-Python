from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):
    # Page Elements
    class_title = 'title'
    url = 'https://www.saucedemo.com/checkout-complete.html'
    txt_page_title = 'CHECKOUT: COMPLETE!'
    id_btn_menu = 'react-burger-menu-btn'
    id_back_to_home_btn = 'back-to-products'
    class_thank_you_for_your_order_msg = 'complete-header'

    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver=driver)

    def is_checkout_complete_page(self):
        # Verify URL page
        is_url_page = self.driver.current_url == self.url
        try:
            # Verificar se o menu existe.
            element_menu = self.driver.find_element(By.ID, self.id_btn_menu)
            # Verificar se o botão BACK HOME existe.
            btn_back_to_home = self.driver.find_element(By.ID, self.id_back_to_home_btn)
            # Verificar título da pagina
            is_title_checkout_complete_page = \
                self.driver.find_element(By.CLASS_NAME, self.class_title).text == self.txt_page_title
            return is_url_page and element_menu and btn_back_to_home and is_title_checkout_complete_page
        except NoSuchElementException:
            return False

    def has_thank_you_for_your_order_message(self):
        try:
            # Verificar mensagem de agradecimento.
            self.driver.find_element(By.CLASS_NAME, self.class_thank_you_for_your_order_msg)
            return True
        except NoSuchElementException:
            return False
