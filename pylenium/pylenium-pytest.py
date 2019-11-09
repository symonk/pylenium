from pylenium.configuration.PyleniumConfig import PyleniumConfig
from pylenium.globals import PYLENIUM, CHROME


def pytest_addoption(parser):
    """
    Main entry point for pylenium to register configuration / runtime arguments
    :param parser:
    :return:
    """
    group = parser.getgroup(PYLENIUM)
    group.addoption('--browser',
                    action='store',
                    dest='browser',
                    default=CHROME,
                    help='Specify the browser pylenium should use')



    pylenium_config = PyleniumConfig()
