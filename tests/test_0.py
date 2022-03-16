from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"


def setup():
    global driver
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(URL)


def test_click_login_btn():
    driver.find_element(By.ID, 'login-button').click()
    assert driver.current_url == URL, "Página requerida não encontrada!"

    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
    assert error_message == 'Epic sadface: Username is required', "Mensagem de erro incorreta!"


def teardown():
    driver.quit()

