import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pylenium.globals import PYLENIUM, CHROME, EXEC_STARTED, RELEASE_INFO, GRATITUDE_MSG
from pylenium import log
from pylenium.plugin_util import plugin_log_seperate, plugin_log_message
from pylenium.resources.ascii import ASCII


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

    group.addoption('--remote',
                    action='store_true',
                    dest='remote',
                    help='Specify if the browser should be remote (selenium grid)')

    group.addoption('--server',
                    action='store',
                    dest='server',
                    default='http://localhost',
                    help='Specify the selenium hub server url')

    group.addoption('--port',
                    action='store',
                    default=4444,
                    type=int,
                    dest='port',
                    help='Specify the selenium hub port')


def pytest_configure(config):
    _configure_metadata()


def _configure_metadata():
    log.info(ASCII)
    plugin_log_seperate()
    plugin_log_message(EXEC_STARTED)
    plugin_log_message(RELEASE_INFO)
    plugin_log_message(GRATITUDE_MSG)
    plugin_log_seperate()


@pytest.fixture
def browser(request):
    return request.config.getoption('browser')


@pytest.fixture
def headless(request):
    return request.config.getoption('headless')


@pytest.fixture
def remote(request):
    return request.config.getoption('remote')


@pytest.fixture
def server(request):
    return request.config.getoption('server')


@pytest.fixture
def port(request):
    return request.config.getoption('port')


@pytest.fixture
def driver(request):
    # some magic for travis for now...
    from webdriver_manager.chrome import ChromeDriverManager
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    yield webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
