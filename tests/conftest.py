import pytest

from Pages.LoginPage import LoginPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run the tests")


@pytest.fixture
def browser(request):
    selected_browser = request.config.getoption('browser')
    if selected_browser.lower() not in ['chrome', 'safari', 'firefox']:
        selected_browser = 'chrome'
    print(f'Browser selecionado para testes: {selected_browser.upper()}')
    yield selected_browser.lower()


@pytest.fixture()
def login_page_open(browser):
    print('Abrir página de Login')
    login_page = LoginPage(browser=browser)
    yield login_page
    print(f'Fechar browser')
    login_page.close()









