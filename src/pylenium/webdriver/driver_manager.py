import threading

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from webdriver_manager.chrome import ChromeDriverManager

from pylenium.exceptions.exceptions import NoThreadedDriverFoundException


class DriverController:
    def __init__(self):
        self.factory = DriverFactory()

    def start(
        self, remote=None, capabilities=None, options=None, command_executor=None
    ) -> RemoteDriver:
        """
        Entry point for building up a web driver instance; This will return an appropriate web driver instance based on
        a number of different command line interface option value(s).  This driver is bound to thread local storage and
        invoking start() on subsequent threads will return a new instance of the web driver.
        :param remote:
        :param capabilities:
        :param options:
        :param command_executor:
        :return: a thread-local instance of a web driver appropriate to the cli args provided
        """
        return self.factory.build()

    def finish(self) -> None:
        self.factory.destroy_driver()


class DriverFactory:
    """
    A factory responsible for instantiating driver instance(s) based on a number of different args provided.
    """

    def __init__(self, *args, **kwargs):
        self._thread_storage = threading.local()
        self._thread_storage.drivers = {}
        self.drivers = self._thread_storage.drivers

    def build(self) -> RemoteDriver:
        if self.drivers.get(threading.get_ident(), None) is None:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            driver = ChromeDriver(
                executable_path=ChromeDriverManager().install(), options=chrome_options
            )
            self.drivers[threading.get_ident()] = driver
        return self._fetch()

    def _fetch(self) -> RemoteDriver:
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

    def _handle_driver_path_or_acquisition(
        self,
        acquire_binary: bool = False,
        browser: str = None,
        remote: bool = False,
        binary_path: str = None,
    ) -> str:
        """
        Responsible for a few things:
        Firstly checking that the driver is not remote; path is not necessary then.
        Secondly checking that if acquire-binary was provided that we care not about path, but instead do the install
        and return the path
        Thirdly if --acquire-binary is not provided, ensure a path is and pass it through
        :return: a path to the drivers local binary on disk
        """

    def destroy_driver(self) -> None:
        """
        Destroy the driver for the executing thread
        :return: None
        """
        driver = self._fetch()
        driver.quit()
