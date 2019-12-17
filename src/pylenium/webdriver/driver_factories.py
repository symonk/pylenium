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
import logging
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pylenium.configuration.pylenium_config import PyleniumConfig
from pylenium.drivers.pylenium_driver import PyleniumDriver

log = logging.getLogger('pylenium')


class AbstractDriverFactory(ABC):

    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def resolve_capabilities(self):
        pass


class ChromeDriverFactory(AbstractDriverFactory):

    def resolve_capabilities(self) -> Options:
        pylenium_chrome_opts = Options()
        pylenium_chrome_opts.add_argument("--headless")
        pylenium_chrome_opts.add_argument("--no-sandbox")
        pylenium_chrome_opts.add_argument("--disable-dev-shm-usage")
        return pylenium_chrome_opts

    def get_driver(self):
        config = PyleniumConfig()
        return PyleniumDriver(
            config,
            webdriver.Chrome(ChromeDriverManager().install(), options=self.resolve_capabilities(config)),
        )


class FireFoxDriverFactory(AbstractDriverFactory):

    def resolve_capabilities(self) -> Options:
        pass

    def get_driver(self):
        config = PyleniumConfig()
        return PyleniumDriver(config, webdriver.Firefox(GeckoDriverManager().install()))


class RemoteWebDriverFactory(AbstractDriverFactory):

    def resolve_capabilities(self) -> Options:
        pass

    def get_driver(self):
        config = PyleniumConfig()
        return PyleniumDriver(
            config,
            webdriver.Remote(
                command_executor=f"{config.server}:{config.server_port}/wd/hub",
                desired_capabilities=config.browser_capabilities
            ))
