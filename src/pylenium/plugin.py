from pytest import fixture

from pylenium import PYLENIUM
from pylenium import GRID_LOCALHOST
from pylenium import CHROME
from pylenium import FIREFOX
from pylenium import DriverController
from pylenium import is_py_file


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

    group.addoption(
        "--browser-capabilities",
        action="store",
        dest="browser_capabilities",
        type=lambda file_path: is_py_file(file_path),
        help="Specify a python file which contains a dictionary outlining browser capabilities",
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
        default="http://localhost:8080",
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
    factory = DriverController()
    request.addfinalizer(factory.finish)
    yield factory.start()


def pytest_configure(config) -> None:
    """
    Main entry point for the plugin, hooked by pytest using pluggy
    :param config: The pytest config object
    """
