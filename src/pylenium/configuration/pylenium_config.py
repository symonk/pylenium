from dataclasses import dataclass
from typing import Callable, Set


@dataclass()
class PyleniumConfig:
    """
    The pylenium config; built up by the plugin and consumed by the driver factories.
    Also available in tests via the pylenium_config session scoped fixture.
    This config should not be overwritten at runtime as it applies to all instantiated browsers.
    """

    BROWSER: str
    HEADLESS: bool
    SELENIUM_GRID_URL: str
    BROWSER_RESOLUTION: str
    BROWSER_VERSION: str
    DRIVER_BINARY_PATH: str
    BROWSER_CAPABILITIES: dict
    CHROME_OPTS: list
    BASE_URL: str
    EXPLICIT_WAIT: int
    POLLING_INTERVAL: int
    PAGE_SOURCE_ON_FAIL: bool
    SCREENSHOT_ON_FAIL: bool
    STACK_TRACE_ON_FAIL: bool
    CLICK_WITH_JAVASCRIPT: bool
    SENDKEYS_WITH_JAVASCRIPT: bool
    DEFAULT_SELECTOR: str
    DRIVER_LISTENER: Callable
    BROWSER_NOT_MAXIMIZED: bool

    @staticmethod
    def get_attributes_as_strings() -> Set:
        """
        Returns a set of instance attributes
        :return: all the instance variable attributes of the pylenium config as a set of strings
        """
        import inspect

        _, values = inspect.getmembers(
            PyleniumConfig, lambda attr: not (inspect.isroutine(attr))
        )[0]
        attrs = set(values.keys())
        return attrs
