import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pylenium.globals import PYLENIUM, CHROME


def pytest_addoption(parser):
    """
    Main entry point for pylenium to register configuration / runtime arguments
    """
    group = parser.getgroup(PYLENIUM)
    group.addoption('--browser',
                    action='store',
                    dest='browser',
                    default=CHROME,
                    help='Specify the browser pylenium should use')
    group.addoption('--headless',
                    action='store_true',
                    dest='headless',
                    help='Specify if the browser should be headless')


@pytest.fixture
def browser(request):
    return request.config.getoption('browser')


@pytest.fixture
def headless(request):
    return request.config.getoption('headless')


@pytest.fixture
def driver(request):
    from webdriver_manager.chrome import ChromeDriverManager
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    yield webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
