from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):
    # Page Elements
    class_title = 'title'
    url = 'https://www.saucedemo.com/checkout-step-two.html'
    txt_page_title = 'CHECKOUT: OVERVIEW'
    id_btn_menu = 'react-burger-menu-btn'
    id_finish_btn = 'finish'
    class_cart_list = 'cart_list'
    class_product_item_name = 'inventory_item_name'

    def __init__(self, driver):
        super(CheckoutOverviewPage, self).__init__(driver=driver)

    def is_checkout_overview_page(self):
        # Verify URL page
        is_url_page = self.driver.current_url == self.url
        try:
            # Verificar se o menu existe.
            element_menu = self.driver.find_element(By.ID, self.id_btn_menu)
            # Verificar se o botão FINISH existe.
            btn_continue = self.driver.find_element(By.ID, self.id_finish_btn)
            # Verificar título da pagina
            is_title_checkout_overview_page = \
                self.driver.find_element(By.CLASS_NAME, self.class_title).text == self.txt_page_title
            return is_url_page and element_menu and btn_continue and is_title_checkout_overview_page
        except NoSuchElementException:
            return False

    def click_finish_btn(self):
        self.driver.find_element(By.ID, self.id_finish_btn).click()

    def is_checkout_products_correct(self, product_list):
        # Get checkout products names (WebElements)
        checkout_products = self.driver.find_elements(By.CLASS_NAME, self.class_product_item_name)
        checkout_products_names = []
        for checkout_item in checkout_products:
            checkout_products_names.append(checkout_item.text)
        return set(product_list) == set(checkout_products_names)