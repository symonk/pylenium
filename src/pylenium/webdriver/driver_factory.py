from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager


class AbstractDriverFactory(ABC):
    @abstractmethod
    def create_driver(self) -> WebDriver:
        """
        Solely responsible for instantiating a bespoke instance of the webdriver using a number of arguments from the
        pytest CLI
        :return: an instance of remote web driver
        """


class ChromeDriverFactory(AbstractDriverFactory):
    def __init__(self, config):
        self.config = config
        super().__init__()

    def create_driver(self) -> WebDriver:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = ChromeDriver(
            executable_path=ChromeDriverManager().install(), options=chrome_options
        )
        base_url = self.config.getoption("base_url")
        if base_url:
            driver.get(base_url)
        return driver
