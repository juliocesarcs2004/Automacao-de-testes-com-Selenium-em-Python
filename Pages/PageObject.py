from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class PageObject:
    def __init__(self, browser=None, driver=None):
        if driver:
            self.driver = driver
            self.driver.implicitly_wait(2)
        else:
            if browser == 'chrome':
                service = ServiceChrome(executable_path=ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service)
            elif browser == 'firefox':
                service = ServiceFirefox(executable_path=GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=service)
            elif browser == 'safari':
                self.driver = webdriver.Safari()

    def close(self):
        self.driver.quit()





