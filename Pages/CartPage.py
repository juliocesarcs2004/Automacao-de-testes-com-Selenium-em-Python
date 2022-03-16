import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CartPage(PageObject):
    # Page Elements
    class_page_title = 'title'
    txt_page_title = 'YOUR CART'
    id_btn_menu = 'react-burger-menu-btn'
    id_checkout_btn = 'checkout'
    class_cart_item = 'inventory_item_name'

    def __init__(self, driver):
        super(CartPage, self).__init__(driver=driver)

    def is_cart_page(self):
        try:
            # Get element title page
            element_class_title = self.driver.find_element(By.CLASS_NAME, self.class_page_title)
            # Verificar se o menu existe.
            element_menu = self.driver.find_element(By.ID, self.id_btn_menu)
            # Verificar se o botão CHECKOUT existe.
            btn_checkout = self.driver.find_element(By.ID, self.id_checkout_btn)
            return element_class_title.text == self.txt_page_title and element_menu and btn_checkout
        except NoSuchElementException:
            return False

    def is_product_in_cart_list(self, product_name):
        # Get cart list
        cart_items = self.driver.find_elements(By.CLASS_NAME, self.class_cart_item)
        for cart_item in cart_items:
            if cart_item.text == product_name:
                return True
        else:
            return False

    def click_checkout_btn(self):
        self.driver.find_element(By.ID, self.id_checkout_btn).click()
