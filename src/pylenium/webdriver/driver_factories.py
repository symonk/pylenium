#  MIT License
#
#  Copyright (c) 2019 Simon Kerr
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
#  Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
#  NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import threading
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pylenium.configuration.pylenium_config import PyleniumConfig
from pylenium.drivers.event_listener import PyleniumEventListener
from pylenium.drivers.pylenium_driver import PyleniumDriver
from pylenium.exceptions.exceptions import PyleniumArgumentException
from pylenium.globals import FIREFOX, REMOTE, CHROME

log = logging.getLogger('pylenium')


class ChromeDriverFactory:
    def __call__(self, config: PyleniumConfig) -> PyleniumDriver:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return PyleniumDriver(
            config,
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
        )


class FireFoxDriverFactory:
    def __call__(self, config: PyleniumConfig) -> PyleniumDriver:
        return PyleniumDriver(config, webdriver.Firefox(GeckoDriverManager().install()))


class RemoteWebDriverFactory:
    def __call__(self, config: PyleniumConfig) -> PyleniumDriver:
        return PyleniumDriver(
            config,
            webdriver.Remote(
                command_executor=f"{config.server}:{config.server_port}/wd/hub",
                desired_capabilities=config.browser_capabilities
            ),
        )


class DriverFactory:

    driver_store = threading.local()
    config = None

    @classmethod
    def get_webdriver(cls, config: PyleniumConfig = None) -> PyleniumDriver:
        if hasattr(cls.driver_store, 'pydriver'):
            log.info(f"Web driver already instantiated for this thread, returning it")
            return cls.driver_store.pydriver

        if cls.config is None and config:
            cls.config = config

        browser = cls.config.browser
        is_remote = cls.config.remote
        wrap_driver = cls.config.wrap_driver
        if browser == CHROME:
            driver = ChromeDriverFactory()(config)
        elif browser == FIREFOX:
            driver = FireFoxDriverFactory()(config)
        elif browser == REMOTE or is_remote:
            driver = RemoteWebDriverFactory()(config)
        else:
            raise PyleniumArgumentException()
        cls.driver_store.pydriver = driver
        return driver if not wrap_driver else EventFiringWebDriver(driver.wrapped_driver, PyleniumEventListener())
