from __future__ import annotations
from abc import ABC
from abc import abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from pylenium.webelement.pylenium_element import PyleniumWebElement
from pylenium.configuration.pylenium_config import PyleniumConfig


class AbstractDriverFactory(ABC):
    def __init__(self, config: PyleniumConfig):
        self.config = config
        self.base_url = self.config.base_url
        self.headless = self.config.headless
        self.resolution = self.config.browser_resolution
        self.maximized = not self.config.browser_not_maximized

    @abstractmethod
    def create_driver(self) -> WebDriver:
        """
        Solely responsible for instantiating a bespoke instance of the webdriver using a number of arguments from the
        pytest CLI
        :return: an instance of remote web driver
        """


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
        self._apply_custom_webelement_to_driver(driver)
        self._load_base_url_if_necessary(driver)
        return self._wrap_driver_if_applicable(driver)

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
        if self.config.acquire_binary:
            return ChromeDriverManager().install()
        return self.config.driver_binary_path

    def _resolve_options(self) -> None:
        """
        Build up chrome options through what is passed to the CLI as well as what is provided on the command line args
        note: if the browser is maximized, --browser-resolution wont play any part, we apply it first
        :return: None; this is done in-place on self.chrome_options
        """
        if self.headless:
            self.chrome_options.add_argument("--headless")
        if self.resolution:
            self.chrome_options.add_argument(
                f"--window-size={self.resolution.width},{self.resolution.height}"
            )
        if self.maximized:
            self.chrome_options.add_argument("--start-maximized")
        user_chrome_options = self.config.chrome_opts
        if user_chrome_options:
            for argument in user_chrome_options:
                self.chrome_options.add_argument(argument)

    def _resolve_desired_capabilities(self) -> None:
        """
        Build up desired caps through what is passed to the CLI as well as what is provided on the command line args
        note: we could do the merging our selves between options/capabilities but lets let selenium handle it for us.
        :return: None; this is done in-place on self.desired_capabilities
        """
        self.desired_capabilities = self.config.browser_capabilities

    @staticmethod
    def _apply_custom_webelement_to_driver(driver) -> WebDriver:
        """
        Modifies the instantiated drivers returned WebElement to our custom child class, this enables us to take more
        control of WebElements and make them a lot more test friendly
        :return: The driver instance for fluency
        """
        driver._web_element_cls = PyleniumWebElement
        return driver

    def _wrap_driver_if_applicable(self, driver) -> WebDriver:
        """
        Given the --driver-listener CLI arg, wrap the driver into an EventFiringWebDriver using the class passed
        by the user; note their module should be discoverable by python and if it is not, we cannot possibly get here.
        parser will raise a ValueError alerting them about the issue
        :param driver: the webdriver instance to 'potentially' wrap
        :return: the drriver instance for fluency
        """
        event_firing = self.config.driver_listener
        if event_firing is not None:
            driver = EventFiringWebDriver(driver, event_firing())
        return driver
