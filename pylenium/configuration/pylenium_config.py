from dataclasses import dataclass

from pylenium.globals import LOCALHOST_URL


@dataclass
class SupportedBrowser:
    browser: Browser.CHROME


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
    """
    browser: SupportedBrowser = SupportedBrowser()
    headless: bool = False
    remote: bool = False
    server: str = LOCALHOST_URL
    server_port: int = 4444
    browser_size: str = '1366x768'
    browser_version: str = 'latest'
    browser_maximized: bool = True
    aquire_binary: bool = True
    browser_path: str = None
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

