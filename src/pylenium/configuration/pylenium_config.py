from dataclasses import dataclass
from typing import Any

from pylenium.string_globals import LOCALHOST_URL, CHROME


@dataclass
class PageLoadingStrategy:
    pass


@dataclass
class BrowserCapabilities:
    pass


@dataclass
class ValidUrl:
    pass


class PyleniumConfig:
    """
    Pyleniums core config, this is built as part of the plugins parse args
    Pylenium will assume sensible default value(s) here
    n.b -> This is considered a singleton, changing it mid run is not advised

    Attributes:
        --browser: The browser in which to execute testing on
        --headless: Should the browser run headlessly
        --remote: Should the browser be instantiated for the selenium grid
        --server: Server ip address of the selenium grid
        --server_port: Server port of the selenium grid
        --browser_resolution: Size of the instantiated browser window
        --browser_version: Version of the browser we should attempt to automatically aquire (unnecessary with --remote=True)
        --browser_maximized: Should the browser instantiated be maximized
        --aquire_binary: Should we aquire the binary automatically and cache it locally
        --driver_binary_path: If you do not want to aquire the binary, the path to your chromedriver or geckodriver binary
        --page_load_strategy: The strategy we should use to load page(s) and ensure it is time to proceed
        --browser_capabilities: Path to a file containing a dictionary of your browser capabilities @default None
        --load_base_url: On driver instantiation, automatically load your applications base url (e.g login page)
        --explicit_wait: Time in milliseconds to explicitly wait for pyleniums smart actions
        --polling_interval: Time in milliseconds to check smart actions predicates to decipher if continuation should occur
        --screenshot_on_fail: Attach a screenshot of the browser if a testing fails
        --page_source_on_fail: Attach the page source (DOM) of the browser if a testing fails
        --stack_trace_on_fail: Provides basic information regarding the reason behind a testing failing
        --click_with_js: Attempt to do clicks using javascript actions (not selenium click actions)
        --sendkeys_with_js: Attempt to send keys (text) using javascript actions (not selenium click actions)
        --default_selector: Default selector for PyleniumElements to use for lookup
        --no-wrap-driver: Should pylenium wrap the driver instance in our own EventFiringWebDriver
        --driver-listener: The path to the .py module we should load your event firing webdriver listener from
    """

    def __init__(self, config):
        self.config = config
        self.browser: str = self._resolve_pytest_config_option("browser") or CHROME
        self.headless: bool = self._resolve_pytest_config_option("headless")
        self.remote: bool = self._resolve_pytest_config_option("remote")
        self.server: str = self._resolve_pytest_config_option("server") or LOCALHOST_URL
        self.server_port: int = self._resolve_pytest_config_option(
            "server_port"
        ) or 4444
        self.browser_resolution: str = self._resolve_pytest_config_option(
            "browser_resolution"
        ) or "1366x768"
        self.browser_version: str = self._resolve_pytest_config_option(
            "browser_version"
        ) or "latest"
        self.browser_maximized: bool = self._resolve_pytest_config_option(
            "browser_maximized"
        )
        self.aquire_binary: bool = self._resolve_pytest_config_option("acquire_binary")
        self.driver_binary_path: str = self._resolve_pytest_config_option(
            "driver_binary_path"
        ) or None
        self.page_load_strategy: PageLoadingStrategy = self._resolve_pytest_config_option(
            "page_load_strategy"
        )
        self.browser_capabilities: BrowserCapabilities = self._resolve_pytest_config_option(
            "browser_capabilities"
        )
        self.load_base_url: bool = self._resolve_pytest_config_option("load_base_url")
        self.base_url: ValidUrl = self._resolve_pytest_config_option("base_url")
        self.explicit_wait: int = self._resolve_pytest_config_option("explicit_wait")
        self.polling_interval: int = self._resolve_pytest_config_option(
            "polling_interval"
        )
        self.screenshot_on_fail: bool = self._resolve_pytest_config_option(
            "store_screenshot"
        )
        self.page_source_on_fail: bool = self._resolve_pytest_config_option(
            "store_page_source"
        )
        self.stack_trace_on_fail: bool = self._resolve_pytest_config_option(
            "store_stack_trace"
        )
        self.click_with_js: bool = self._resolve_pytest_config_option("click_with_js")
        self.sendkeys_with_js: bool = self._resolve_pytest_config_option(
            "sendkeys_with_js"
        )
        self.default_selector: str = self._resolve_pytest_config_option(
            "default_selector"
        )
        self.wrap_driver: bool = self._resolve_pytest_config_option("wrap_driver")
        self.driver_listener_path: str = self._resolve_pytest_config_option(
            "driver_listener"
        ) or None

    @staticmethod
    def _resolve_pytest_config_option(self, name: str) -> Any:
        breakpoint()
        print(1)
