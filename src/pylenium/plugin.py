import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from pylenium.drivers.event_listener import PyleniumEventListener
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
                    default=False,
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

    group.addoption('--server_port',
                    action='store',
                    default=4444,
                    type=int,
                    dest='server_port',
                    help='Specify the selenium hub port')

    group.addoption('--browser-resolution',
                    action='store',
                    default='1920x1080',
                    dest='browser_resolution',
                    help='Specify the browser resolution')

    group.addoption('--browser-version',
                    action='store',
                    default='latest',
                    dest='browser_version',
                    help='Specify the browser version')

    group.addoption('--aquire-binary',
                    action='store_true',
                    default=False,
                    dest='aquire_binary',
                    help='Specify if pylenium should aquire the chrome binary version specified or latest')

    group.addoption('--driver-binary-path',
                    action='store',
                    default='',
                    dest='driver_binary_path',
                    help='If not using aquire binary, set the directory pylenium should look for the driver bianary')

    group.addoption('--page-load-strategy',
                    action='store',
                    default='normal',
                    dest='page_load_strategy',
                    choices=['slow', 'normal', 'fast'],
                    help='Specify the page loading strategy')

    group.addoption('--page-source-on-fail',
                    action='store',
                    default=False,
                    type=bool,
                    dest='store_page_source',
                    help='Store page source HTML for each test in the event of failures')

    group.addoption('--screenshot-on-fail',
                    action='store',
                    default=False,
                    type=bool,
                    dest='store_screenshot',
                    help='Store screenshot for each test in the event of failures')

    group.addoption('--stack-trace-on-fail',
                    action='store',
                    default=False,
                    type=bool,
                    dest='store_stack_trace',
                    help='Store stack trace info for each test in the event of failures')


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
def server_port(request):
    return request.config.getoption('server_port')


@pytest.fixture
def browser_resolution(request):
    return request.config.getoption('browser_resolution')


@pytest.fixture
def browser_version(request):
    return request.config.getoption('browser_version')


@pytest.fixture
def aquire_binary(request):
    return request.config.getoption('aquire_binary')


@pytest.fixture
def driver_binary_path(request):
    return request.config.getoption('driver_binary_path')


@pytest.fixture
def page_load_strategy(request):
    return request.config.getoption('page_load_strategy')


@pytest.fixture
def store_page_source_on_fail(request):
    return request.config.getoption('store_page_source')


@pytest.fixture
def store_screenshot_on_fail(request):
    return request.config.getoption('store_screenshot')


@pytest.fixture
def store_stack_trace_on_fail(request):
    return request.config.getoption('store_stack_trace')


@pytest.fixture
def driver(request):
    # some magic for travis for now...
    from webdriver_manager.chrome import ChromeDriverManager
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    yield EventFiringWebDriver(webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
                               PyleniumEventListener())
