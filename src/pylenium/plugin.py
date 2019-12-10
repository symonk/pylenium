import pytest
import yaml
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from yaml.parser import ParserError

from pylenium import log
from pylenium.configuration.pylenium_config import PyleniumConfig
from pylenium.drivers.event_listener import PyleniumEventListener
from pylenium.exceptions.exceptions import PyleniumCapabilitiesException, PyleniumInvalidYamlException
from pylenium.globals import PYLENIUM, CHROME, EXEC_STARTED, RELEASE_INFO, GRATITUDE_MSG, NO_CAP_FILE_FOUND_EXCEPTION, \
    CAP_FILE_YAML_FORMAT_NOT_ACCEPTABLE
from pylenium.plugin_util import plugin_log_seperate, plugin_log_message
from pylenium.resources.ascii import ASCII
from pylenium.webdriver.driver_factories import DriverFactory


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
        "--aquire-binary",
        action="store_true",
        default=False,
        dest="aquire_binary",
        help="Specify if pylenium should aquire the chrome binary version specified or latest",
    )

    group.addoption(
        "--driver-binary-path",
        action="store",
        default="",
        dest="driver_binary_path",
        help="If not using aquire binary, set the directory pylenium should look for the driver bianary",
    )

    group.addoption(
        "--page-load-strategy",
        action="store",
        default="normal",
        dest="page_load_strategy",
        choices=["slow", "normal", "fast"],
        help="Specify the page loading strategy",
    )

    group.addoption(
        "--browser-capabilities-file",
        action="store",
        default="",
        dest="browser_capabilities",
        help="Specify a python file which contains a dictionary outlining browser capabilities",
    )

    group.addoption(
        "--base-url",
        action="store",
        dest="base_url",
        default="http://localhost:8080",
        help="Specify a base url to launch when any drivers are instantiated",
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
        action="store",
        default=False,
        type=bool,
        dest="store_page_source",
        help="Store page source HTML for each test in the event of failures",
    )

    group.addoption(
        "--screenshot-on-fail",
        action="store",
        default=False,
        type=bool,
        dest="store_screenshot",
        help="Store screenshot for each test in the event of failures",
    )

    group.addoption(
        "--stack-trace-on-fail",
        action="store",
        default=False,
        type=bool,
        dest="store_stack_trace",
        help="Store stack trace info for each test in the event of failures",
    )

    group.addoption(
        "--click-with-js",
        action="store",
        type=bool,
        default=False,
        dest="click_with_js",
        help="Attempt to do clicks using a javascript wraparound",
    )

    group.addoption(
        "--sendkeys-with-js",
        action="store",
        type=bool,
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


def pytest_configure(config):
    _configure_metadata()
    py_config = PyleniumConfig()

    cap_file_path = config.getoption('browser_capabilities')
    if cap_file_path:
        py_config.browser_capabilities = _try_parse_capabilities_yaml(cap_file_path)
    config.pylenium_config = py_config


def _configure_metadata():
    log.info(ASCII)
    plugin_log_seperate()
    plugin_log_message(EXEC_STARTED)
    plugin_log_message(RELEASE_INFO)
    plugin_log_message(GRATITUDE_MSG)
    plugin_log_seperate()


def _try_parse_capabilities_yaml(file_path) -> dict:
    try:
        with open(file_path, 'r') as yaml_file:
            parsed_yaml = yaml.safe_load(yaml_file)
            return parsed_yaml['Capabilities']
    except FileNotFoundError:
        raise PyleniumCapabilitiesException(NO_CAP_FILE_FOUND_EXCEPTION)
    except ParserError:
        raise PyleniumInvalidYamlException(CAP_FILE_YAML_FORMAT_NOT_ACCEPTABLE)


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
def aquire_binary(request):
    return request.config.getoption("aquire_binary")


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
def pylenium_config(request):
    return request.config.pylenium_config


@pytest.fixture
def driver(pylenium_config):
    driver = DriverFactory.instantiate(pylenium_config)
    yield EventFiringWebDriver(driver.wrapped_driver, PyleniumEventListener())
