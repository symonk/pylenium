import threading

from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from pylenium.exceptions.exceptions import NoThreadedDriverFoundException
from pylenium.webdriver.driver_factory import ChromeDriverFactory
from pylenium.webdriver.driver_factory import AbstractDriverFactory
from pylenium.configuration.pylenium_config import PyleniumConfig
from typing import Dict, Type


class DriverManager:
    _supported_factories: Dict[str, Type[AbstractDriverFactory]] = {
        "chrome": ChromeDriverFactory
    }

    def __init__(self, config: PyleniumConfig):
        self.config = config
        self.drivers = threading.local().drivers = {}

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
            factory = self._supported_factories.get(self.config.browser)
            driver = factory(self.config).create_driver()
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
            ) from None

    def shutdown_driver(self) -> None:
        """
        Shuts down the thread local driver
        """
        driver = self._fetch_driver()
        driver.quit()
        self.drivers.pop(threading.get_ident())
