from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager


class AbstractDriverFactory(ABC):
    def __init__(self, config):
        self.config = config
        self.base_url = self._config_pluck("base_url")
        self.headless = self._config_pluck("headless")
        self.resolution = self._config_pluck("browser_resolution")
        self.maximized = not self._config_pluck("browser_not_maximized")

    @abstractmethod
    def create_driver(self) -> WebDriver:
        """
        Solely responsible for instantiating a bespoke instance of the webdriver using a number of arguments from the
        pytest CLI
        :return: an instance of remote web driver
        """

    def _config_pluck(self, option) -> Any:
        """
        Quick way to retrieve a value from the pytest config specifying a default if it does not exist
        :param option: the option (str) to go hunting for
        :return: the value stored in the config options for the given option (key)
        """
        return self.config.getoption(option)


class ChromeDriverFactory(AbstractDriverFactory):
    def __init__(self, config):
        super().__init__(config)
        self.chrome_options = ChromeOptions()
        self.desired_capabilities = None

    def create_driver(self) -> WebDriver:
        """
        Chrome driver creation
        :return: the instantiated instance of the chrome driver
        """
        self._resolve_options()
        self._resolve_desired_capabilities()
        binary_path = self._resolve_driver_path()
        driver = ChromeDriver(
            executable_path=binary_path,
            options=self.chrome_options,
            desired_capabilities=self.desired_capabilities,
        )
        return self._load_base_url_if_necessary(driver)

    def _load_base_url_if_necessary(self, driver) -> WebDriver:
        """
        Checks --base-url for a loadable url and loads it prior to returning the driver
        :param driver: the driver instances; recently instantiated
        :return: the driver for fluency
        """
        if self.base_url is not None:
            driver.get(self.base_url)
        return driver

    def _resolve_driver_path(self) -> str:
        """
        Decide if we need to:
        A) Acquire the driver binary if --acquire binary was provided
        B) Use a local path passed by the user through --driver-binary-path
        note: Precedence here is that --acquire-binary is king, followed by path
        note: Driver-binary-path is validated at plugin load time, if we cannot find it we won't get this far
        :return: the path to the chrome-driver binary - downloaded or installed by the user
        """
        if self._config_pluck("acquire_binary"):
            return ChromeDriverManager().install()
        return self._config_pluck("driver_binary_path")

    def _resolve_options(self) -> None:
        """
        Build up chrome options through what is passed to the CLI as well as what is provided on the command line args
        note: if the browser is maximized, --browser-resolution wont play any part, we apply it first
        :return: None; this is done in-place on self.chrome_options
        """
        if self.headless:
            self.chrome_options.add_argument("--headless")
            self.chrome_options.add_argument("--disable-gpu")
        if self.resolution:
            self.chrome_options.add_argument(
                f"--window-size={self.resolution.width},{self.resolution.height}"
            )
        if self.maximized:
            self.chrome_options.add_argument("--start-maximized")

    def _resolve_desired_capabilities(self) -> None:
        """
        Build up desired caps through what is passed to the CLI as well as what is provided on the command line args
        note: we could do the merging our selves between options/capabilities but lets let selenium handle it for us.
        :return: None; this is done in-place on self.desired_capabilities
        """
        self.desired_capabilities = self.config.getoption("browser_capabilities")
