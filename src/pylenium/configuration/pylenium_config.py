from dataclasses import dataclass
from typing import Dict

import yaml

from pylenium.exceptions.exceptions import PyleniumCapabilitiesException, PyleniumInvalidYamlException
from pylenium.string_globals import LOCALHOST_URL, CHROME, NO_CAP_FILE_FOUND_EXCEPTION, \
    CAP_FILE_YAML_FORMAT_NOT_ACCEPTABLE
from yaml.parser import ParserError


@dataclass
class PageLoadingStrategy:
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
        self.browser: str = config.getoption("browser") or CHROME
        self.headless: bool = config.getoption("headless")
        self.remote: bool = config.getoption("remote")
        self.server: str = config.getoption("server") or LOCALHOST_URL
        self.server_port: int = config.getoption("server_port") or 4444
        self.browser_resolution: str = config.getoption(
            "browser_resolution"
        ) or "1366x768"
        self.browser_version: str = config.getoption("browser_version") or "latest"
        self.browser_maximized: bool = config.getoption("browser_maximized")
        self.aquire_binary: bool = config.getoption("acquire_binary")
        self.driver_binary_path: str = config.getoption("driver_binary_path") or None
        self.page_load_strategy: PageLoadingStrategy = config.getoption(
            "page_load_strategy"
        )
        self.browser_capabilities: Dict = self._try_parse_capabilities_yaml(config.getoption('browser_capabilities'))
        self.base_url: ValidUrl = config.getoption("base_url") or None
        self.explicit_wait: int = config.getoption("explicit_wait")
        self.polling_interval: int = config.getoption("polling_interval")
        self.screenshot_on_fail: bool = config.getoption("store_screenshot")
        self.page_source_on_fail: bool = config.getoption("store_page_source")
        self.stack_trace_on_fail: bool = config.getoption("store_stack_trace")
        self.click_with_js: bool = config.getoption("click_with_js")
        self.sendkeys_with_js: bool = config.getoption("sendkeys_with_js")
        self.default_selector: str = config.getoption("default_selector")
        self.driver_listener_path: str = config.getoption("driver_listener") or None

    @staticmethod
    def _try_parse_capabilities_yaml(file_path) -> dict:
        if file_path is None:
            return {}
        try:
            with open(file_path, "r") as yaml_file:
                parsed_yaml = yaml.safe_load(yaml_file)
                return parsed_yaml["Capabilities"]
        except FileNotFoundError:
            raise PyleniumCapabilitiesException(NO_CAP_FILE_FOUND_EXCEPTION)
        except ParserError:
            raise PyleniumInvalidYamlException(CAP_FILE_YAML_FORMAT_NOT_ACCEPTABLE)
