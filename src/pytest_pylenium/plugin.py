import pytest

from src.pytest_pylenium.configuration.pylenium_config import PyleniumConfig
from src.pytest_pylenium.globals import PYLENIUM, CHROME


def pytest_addoption(parser):
    """
    Main entry point for pytest_pylenium to register configuration / runtime arguments
    """
    group = parser.getgroup(PYLENIUM)
    group.addoption('--browser',
                    action='store',
                    dest='browser',
                    default=CHROME,
                    help='Specify the browser pytest_pylenium should use')


def pytest_configure(config):
    browser = config.getoption('browser')
    pylenium_config = PyleniumConfig(browser)


@pytest.fixture
def browser(request):
    return request.config.getoption('browser')
