from pylenium.configuration.pylenium_config import PyleniumConfig
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


def pytest_configure(config):
    browser = config.getoption('browser')
    pylenium_config = PyleniumConfig(browser)
