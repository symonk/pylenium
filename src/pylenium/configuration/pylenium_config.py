from dataclasses import dataclass
from typing import Callable, Set


@dataclass(frozen=True)
class PyleniumConfig:
    """
    The pylenium config; built up by the plugin and consumed by the driver factories.
    Also available in tests via the pylenium_config session scoped fixture.
    This config is immutable, populating by CLI args and should not be changed
    """

    browser: str
    headless: bool
    selenium_grid_url: str
    browser_resolution: str
    browser_version: str
    acquire_binary: bool
    driver_binary_path: str
    browser_capabilities: dict
    chrome_opts: list
    base_url: str
    explicit_wait: int
    polling_interval: int
    page_source_on_fail: bool
    screenshot_on_fail: bool
    stack_trace_on_fail: bool
    click_with_javascript: bool
    sendkeys_with_javascript: bool
    default_selector: str
    driver_listener: Callable
    browser_not_maximized: bool

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
