from selenium.webdriver.common.by import By

from Pages.PageObject import PageObject


class MenuPage(PageObject):
    # Page Elements
    id_menu_icon = 'react-burger-menu-btn'
    class_menu_items = 'bm-item-list'
    id_cross_btn = 'react-burger-cross-btn'
    id_logout_menu_item = 'logout_sidebar_link'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_icon).click()

    def is_menu_open(self):
        # Get elements from menu
        menu_items = self.driver.find_element(By.CLASS_NAME, self.class_menu_items)
        menu_cross_icon = self.driver.find_element(By.ID, self.id_cross_btn)
        return menu_items and menu_cross_icon

    def click_logout(self):
        self.driver.find_element(By.ID, self.id_logout_menu_item).click()


