from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#driver = webdriver.Chrome(executable_path=r"../drivers_mac/chromedriver")

driver.get(URL)

driver.find_element(By.ID, 'login-button').click()

assert driver.current_url == URL, "Página requerida não encontrada!"

error_message = driver.find_element(By.CLASS_NAME, 'error-message-container').text
assert error_message == 'Epic sadface: Username is required', "Mensagem de erro incorreta!"

driver.quit()

