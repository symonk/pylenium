import threading

from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from pylenium.exceptions.exceptions import NoThreadedDriverFoundException
from pylenium.webdriver.driver_factory import ChromeDriverFactory


class DriverManager:
    _supported_factories = {"chrome": ChromeDriverFactory}

    def __init__(self, config):
        self.config = config
        self._thread_storage = threading.local()
        self._thread_storage.drivers = {}
        self.drivers = self._thread_storage.drivers

    def start_driver(self) -> RemoteDriver:
        """
        Entry point for pylenium to manage driver instances, this offloads instantiation off to a bunch of
        factory implementations, each responsible for instantiating a basic instance based on the --browser provided.
        Each factory is responsible for managing the args that it requires from the pytest config to keep this nice
        and clean.
        :return: The instantiated instance of the driver, if one already was created for the create we will return it
        instead
        """
        driver = self.drivers.get(threading.get_ident(), None)
        if driver is None:
            user_browser_specified = self.config.getoption("browser")
            driver = self._supported_factories.get(user_browser_specified)(
                self.config
            ).create_driver()
            self.drivers[threading.get_ident()] = driver
        return self._fetch_driver()

    def _fetch_driver(self) -> RemoteDriver:
        """
        This should never be called by users directly; instead it is part of a latter piece of logic based on the
        outcome of self.build()
        :return: an instance of RemoteWebDriver based on specification(s) provided.
        """
        try:
            return self.drivers[threading.get_ident()]
        except KeyError:
            raise NoThreadedDriverFoundException(
                f"No threaded driver found for this thread: {threading.get_ident()}"
            )

    def shutdown_driver(self) -> None:
        driver = self._fetch_driver()
        driver.quit()
        self.drivers.pop(threading.get_ident())
