from dataclasses import dataclass

from pylenium.globals import LOCALHOST_URL, CHROME


@dataclass
class PageLoadingStrategy:
    pass


@dataclass
class BrowserCapabilities:
    pass


@dataclass
class ValidUrl:
    pass


@dataclass
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
    """
    browser: str = CHROME
    headless: bool = False
    remote: bool = False
    server: str = LOCALHOST_URL
    server_port: int = 4444
    browser_resolution: str = '1366x768'
    browser_version: str = 'latest'
    browser_maximized: bool = True
    aquire_binary: bool = True
    driver_binary_path: str = None
    page_load_strategy: PageLoadingStrategy = PageLoadingStrategy()
    browser_capabilities: BrowserCapabilities = None
    load_base_url: bool = False
    base_url: ValidUrl = LOCALHOST_URL
    explicit_wait: int = 15000
    polling_interval: int = 200
    screenshot_on_fail: bool = False
    page_source_on_fail: bool = False
    stack_trace_on_fail: bool = False
    click_with_js: bool = False
    sendkeys_with_js: bool = False
    default_selector: str = 'CSS'
