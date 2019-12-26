from __future__ import annotations

import threading
from abc import ABC, abstractmethod
from functools import partial

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pylenium.configuration.pylenium_config import PyleniumConfig
from pylenium.exceptions.exceptions import PyleniumArgumentException
from pylenium.logging.log import log
from pylenium.resources.ascii import ASCII
from pylenium.strategies.page_loading_strategy import (
    SlowLoadingPageStrategy,
    FastLoadingPageStrategy,
    NormalLoadingPageStrategy,
)
from pylenium.string_globals import (
    PYLENIUM,
    CHROME,
    EXEC_STARTED,
    RELEASE_INFO,
    GRATITUDE_MSG,
    REMOTE,
    FIREFOX,
)
from pylenium.utilities import plugin_log_seperate, plugin_log_message
from pylenium.webdriver.pylenium_driver import PyleniumDriver
from pylenium.webelements.pylenium_element import PyleniumElement

thread_local_drivers = None
configuration = None


def pytest_addoption(parser):
    """
    Main entry point for pylenium to register configuration / runtime arguments
    """
    group = parser.getgroup(PYLENIUM)
    group.addoption(
        "--browser",
        action="store",
        dest="browser",
        default=CHROME,
        help="Specify the browser pylenium should use",
    )

    group.addoption(
        "--headless",
        action="store_true",
        default=False,
        dest="headless",
        help="Specify if the browser should be headless",
    )

    group.addoption(
        "--remote",
        action="store_true",
        dest="remote",
        help="Specify if the browser should be remote (selenium grid)",
    )

    group.addoption(
        "--server",
        action="store",
        dest="server",
        default="http://localhost",
        help="Specify the selenium hub server url",
    )

    group.addoption(
        "--server_port",
        action="store",
        default=4444,
        type=int,
        dest="server_port",
        help="Specify the selenium hub port",
    )

    group.addoption(
        "--browser-resolution",
        action="store",
        default="1920x1080",
        dest="browser_resolution",
        help="Specify the browser resolution",
    )

    group.addoption(
        "--browser-version",
        action="store",
        default="latest",
        dest="browser_version",
        help="Specify the browser version",
    )

    group.addoption(
        "--acquire-binary",
        action="store_true",
        default=False,
        dest="acquire_binary",
        help="Specify if pylenium should acquire the chrome binary version specified or latest",
    )

    group.addoption(
        "--driver-binary-path",
        action="store",
        default=None,
        dest="driver_binary_path",
        help="If not using acquire binary, set the directory pylenium should look for the driver bianary",
    )

    strategies = {
        "slow": SlowLoadingPageStrategy,
        "normal": NormalLoadingPageStrategy,
        "fast": FastLoadingPageStrategy,
    }

    def _resolve_strategy(choice: str):
        return strategies.get(choice, NormalLoadingPageStrategy())

    group.addoption(
        "--page-load-strategy",
        action="store",
        default="normal",
        type=_resolve_strategy,
        dest="page_load_strategy",
        choices=[
            SlowLoadingPageStrategy,
            NormalLoadingPageStrategy,
            FastLoadingPageStrategy,
        ],
        help="Specify the page loading strategy",
    )

    group.addoption(
        "--browser-capabilities-file",
        action="store",
        dest="browser_capabilities",
        help="Specify a python file which contains a dictionary outlining browser capabilities",
    )

    group.addoption(
        "--base-url",
        action="store",
        dest="base_url",
        default="http://localhost:8080",
        help="Specify a base url to launch when any webdriver are instantiated",
    )

    group.addoption(
        "--explicit-wait",
        action="store",
        type=int,
        default=30,
        dest="explicit_wait",
        help="Specify how long smart waiting in pylenium should give as a grace period",
    )

    group.addoption(
        "--polling-interval",
        action="store",
        type=float,
        default=0.25,
        dest="polling_interval",
        help="Specify how long pylenium should poll during explicit waiting conditions",
    )

    group.addoption(
        "--page-source-on-fail",
        action="store_true",
        default=False,
        dest="store_page_source",
        help="Store page source HTML for each test in the event of failures",
    )

    group.addoption(
        "--screenshot-on-fail",
        action="store_true",
        default=False,
        dest="store_screenshot",
        help="Store screenshot for each test in the event of failures",
    )

    group.addoption(
        "--stack-trace-on-fail",
        action="store_true",
        default=False,
        dest="store_stack_trace",
        help="Store stack trace info for each test in the event of failures",
    )

    group.addoption(
        "--click-with-js",
        action="store_true",
        default=False,
        dest="click_with_js",
        help="Attempt to do clicks using a javascript wraparound",
    )

    group.addoption(
        "--sendkeys-with-js",
        action="store_true",
        default=False,
        dest="sendkeys_with_js",
        help="Attempt to do sendkeys using a javascript wraparound",
    )

    group.addoption(
        "--default-selector",
        action="store",
        default="css",
        dest="default_selector",
        choices=["css", "id"],
        help="When no locator is specified, default to this value",
    )

    group.addoption(
        "--driver-listener",
        action="store",
        default=None,
        dest="driver_listener",
        help="File path to your .py module which implements seleniums AbstractEventListener"
        "n.b -> if passed; this will create an EventFiringWebDriver automatically",
    )

    group.addoption(
        "--browser-maximized",
        action="store_true",
        default=False,
        dest="browser_maximized",
        help="Should pylenium maximize the browser when it is instantiated",
    )


def pytest_configure(config):
    _resolve_config_from_parseargs(config)
    _init_thread_local_drivers()


def _resolve_config_from_parseargs(config):
    """
    Prepares the globally instantiated pylenium config after parsing command line arguments
    :param config: the pytest test config object
    """
    global configuration
    configuration = PyleniumConfig(config)


def _init_thread_local_drivers():
    global thread_local_drivers
    thread_local_drivers = ThreadLocalDriverManager(configuration)


def _configure_metadata():
    log.info(ASCII)
    plugin_log_seperate()
    plugin_log_message(EXEC_STARTED)
    plugin_log_message(RELEASE_INFO)
    plugin_log_message(GRATITUDE_MSG)
    plugin_log_seperate()


def get_webdriver():
    """
    Pyleniums bread and butter, creates a fresh driver for every new thread or returns the driver coupled to the
    thread which asked for one, if no driver exist for that thread we will use the pylenium config to create one
    """
    return thread_local_drivers.get_driver()


def get_configuration():
    return configuration


def find(locator):
    pass


def find_all(locator):
    pass


def XPATH(selector) -> PyleniumElement:
    return get_webdriver().browser.find_element_by_xpath(selector)


@pytest.fixture
def browser(request):
    return request.config.getoption("browser")


@pytest.fixture
def headless(request):
    return request.config.getoption("headless")


@pytest.fixture
def remote(request):
    return request.config.getoption("remote")


@pytest.fixture
def server(request):
    return request.config.getoption("server")


@pytest.fixture
def server_port(request):
    return request.config.getoption("server_port")


@pytest.fixture
def browser_resolution(request):
    return request.config.getoption("browser_resolution")


@pytest.fixture
def browser_version(request):
    return request.config.getoption("browser_version")


@pytest.fixture
def acquire_binary(request):
    return request.config.getoption("acquire_binary")


@pytest.fixture
def driver_binary_path(request):
    return request.config.getoption("driver_binary_path")


@pytest.fixture
def page_load_strategy(request):
    return request.config.getoption("page_load_strategy")


@pytest.fixture
def base_url(request):
    return request.config.getoption("base_url")


@pytest.fixture
def explicit_wait(request):
    return request.config.getoption("explicit_wait")


@pytest.fixture
def polling_interval(request):
    return request.config.getoption("polling_interval")


@pytest.fixture
def browser_capabilities_file(request):
    return request.config.getoption("browser_capabilities")


@pytest.fixture
def store_page_source_on_fail(request):
    return request.config.getoption("store_page_source")


@pytest.fixture
def store_screenshot_on_fail(request):
    return request.config.getoption("store_screenshot")


@pytest.fixture
def store_stack_trace_on_fail(request):
    return request.config.getoption("store_stack_trace")


@pytest.fixture
def click_with_js(request):
    return request.config.getoption("click_with_js")


@pytest.fixture
def sendkeys_with_js(request):
    return request.config.getoption("sendkeys_with_js")


@pytest.fixture
def default_selector(request):
    return request.config.getoption("default_selector")


@pytest.fixture
def driver_listener(request):
    return request.config.getoption("driver_listener")


@pytest.fixture
def browser_maximized(request):
    return request.config.getoption("browser_maximized")


@pytest.fixture
def pylenium_config():
    return configuration


@pytest.fixture
def driver(pylenium_config):
    driver = get_webdriver()
    yield driver


@pytest.fixture(autouse=True)
def destroy_drivers(request):
    def finalizer():
        for driver in thread_local_drivers.threaded_drivers.drivers.values():
            driver.quit()
        thread_local_drivers.threaded_drivers.drivers.pop(threading.get_ident(), None)

    request.addfinalizer(finalizer)


# Driver management
class ThreadLocalDriverManager:
    def __init__(self, config):
        self.threaded_drivers = threading.local()
        self.threaded_drivers.drivers = {}
        self.config = config
        self.supported_drivers = {
            CHROME: partial(ChromeDriverFactory().get_driver),
            FIREFOX: partial(FireFoxDriverFactory().get_driver),
            REMOTE: partial(RemoteWebDriverFactory().get_driver),
        }

    def get_driver(self):
        """
        Spawns a new thread local driver or returns the already instantiated one if such a driver exists
        for the given thread
        :return: an instance of PyleniumDriver
        """
        driver = self._resolve_driver_from_config()
        return driver

    def _resolve_driver_from_config(self) -> PyleniumDriver:
        thread_id = threading.get_ident()
        driver = self.threaded_drivers.drivers.get(thread_id, None)
        if driver:
            return driver

        runtime_browser = self.config.browser

        if runtime_browser not in self.supported_drivers.keys():
            raise PyleniumArgumentException(
                f"Unsupported --browser option, selection was {runtime_browser}"
            )
        else:
            self.threaded_drivers.drivers[thread_id] = self.supported_drivers.get(
                runtime_browser
            )()
            return self.threaded_drivers.drivers.get(thread_id)


class AbstractDriverFactory(ABC):
    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def resolve_capabilities(self):
        pass


class ChromeDriverFactory(AbstractDriverFactory):
    def resolve_capabilities(self) -> Options:
        pylenium_chrome_opts = Options()
        pylenium_chrome_opts.add_argument("--headless")
        pylenium_chrome_opts.add_argument("--no-sandbox")
        pylenium_chrome_opts.add_argument("--disable-dev-shm-usage")
        return pylenium_chrome_opts

    def get_driver(self):
        return PyleniumDriver(
            configuration,
            webdriver.Chrome(
                ChromeDriverManager().install(), options=self.resolve_capabilities()
            ),
        )


class FireFoxDriverFactory(AbstractDriverFactory):
    def resolve_capabilities(self) -> Options:
        pass

    def get_driver(self):
        return PyleniumDriver(
            configuration, webdriver.Firefox(GeckoDriverManager().install())
        )


class RemoteWebDriverFactory(AbstractDriverFactory):
    def resolve_capabilities(self) -> Options:
        pass

    def get_driver(self):
        return PyleniumDriver(
            configuration,
            webdriver.Remote(
                command_executor=f"{pylenium_config.server}:{pylenium_config.server_port}/wd/hub",
                desired_capabilities=pylenium_config.browser_capabilities,
            ),
        )
