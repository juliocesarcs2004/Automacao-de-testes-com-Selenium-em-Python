import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class ProductNotFoundException(Exception):
    pass


class ProductsPage(PageObject):
    # Page Elements
    txt_page_title = 'PRODUCTS'
    class_page_title = 'title'
    id_btn_menu = 'react-burger-menu-btn'
    id_list_products = 'inventory_container'
    class_add_to_cart_btn = 'btn_inventory'
    txt_remove_btn = 'REMOVE'
    class_product_item = 'inventory_item_description'
    class_product_name = 'inventory_item_name'
    class_shopping_cart_badge = 'shopping_cart_badge'
    id_shopping_cart = 'shopping_cart_container'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_products_page(self):
        try:
            # Get element title page
            element_class_title = self.driver.find_element(By.CLASS_NAME, self.class_page_title)
            # Verificar se o menu existe.
            element_menu = self.driver.find_element(By.ID, self.id_btn_menu)
            return element_class_title.text == self.txt_page_title and element_menu
        except NoSuchElementException:
            return False

    def get_products_list(self):
        try:
            return self.driver.find_element(By.ID, self.id_list_products)
        except NoSuchElementException:
            return None

    def add_product_to_cart_by_name(self, product_name):

        all_products = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)

        for product_item in all_products:
            product_item_name = product_item.find_element(By.CLASS_NAME, self.class_product_name).text
            if product_item_name == product_name:
                product_item.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).click()
                if product_item.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).text != self.txt_remove_btn:
                    raise Exception(f'Após clicar no produto o botão não mudou para \'REMOVE\'!')
                break
        else:
            time.sleep(10)
            raise ProductNotFoundException(f'Produto {product_name} não encontrado!')

    def get_shopping_cart_badge(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_badge).text

    def open_shopping_cart(self):
        self.driver.find_element(By.ID, self.id_shopping_cart).click()
