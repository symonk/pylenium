from typing import Dict

from pytest import fixture

from pylenium.constants.strings import PYLENIUM
from pylenium.constants.strings import GRID_LOCALHOST
from pylenium.constants.strings import CHROME
from pylenium.constants.strings import FIREFOX
from pylenium.webdriver.driver_manager import DriverManager
from pylenium.utility.operating_system import is_py_file
from pylenium.utility.operating_system import parse_capabilities_from_disk
from pylenium.utility.network import validate_url


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
        type=lambda browser: browser.lower(),
        choices=[CHROME, FIREFOX],
        help="Specify the browser pylenium should use",
    )

    group.addoption(
        "--headless",
        action="store_true",
        dest="headless",
        help="Specify if the browser should be headless",
    )

    group.addoption(
        "--command-executor",
        action="store",
        dest="selenium_grid_url",
        default=GRID_LOCALHOST,
        help="Specify the full url for your selenium hub, should include /wd/hub",
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
        dest="acquire_binary",
        help="Specify if pylenium should acquire the chrome binary version specified or latest",
    )

    group.addoption(
        "--driver-binary-path",
        action="store",
        default=None,
        dest="driver_binary_path",
        help="If not using acquire binary, set the directory pylenium should look for the driver binary",
    )

    def _resolve_capabilities(file_path: str) -> Dict:
        """
        Takes the --desired-capabilities file path, validates it and returns into the config a dictionary of the
        desired capabilities to be instantiated into the driver at creation time.
        note: This is exposed through a separate fixture 'py_desired_caps'
        :param file_path:
        :return: a dictionary of desired capabilities
        """
        is_py_file(file_path)
        return parse_capabilities_from_disk(file_path)

    group.addoption(
        "--browser-capabilities",
        action="store",
        dest="browser_capabilities",
        type=_resolve_capabilities,
        default=None,
        help="Specify a python file which contains a dictionary outlining browser capabilities"
        "Note: This .py file should contain a dictionary called 'capabilities' explicitly",
    )

    group.addoption(
        "--chrome-switches",
        type=lambda option: option.strip().split(","),
        help="delimited list of chrome options / switches",
        default=[],
    )

    group.addoption(
        "--base-url",
        action="store",
        dest="base_url",
        type=lambda url: validate_url(url),
        help="Specify a base url to launch when any driver are instantiated",
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


@fixture(name="pydriver")
def pylenium_webdriver(request):
    driver_manager = DriverManager(request.config)
    request.addfinalizer(driver_manager.shutdown_driver)
    driver = driver_manager.start_driver()
    yield driver


@fixture(scope="session", name="py_desired_caps")
def pylenium_desired_capabilities(request):
    return request.config.getoption("browser_capabilities")
