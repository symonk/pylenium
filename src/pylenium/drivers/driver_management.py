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
from functools import partial
from pylenium.configuration.pylenium_config import PyleniumConfig
from pylenium.drivers.pylenium_driver import PyleniumDriver
from pylenium.exceptions.exceptions import PyleniumArgumentException
from pylenium.string_globals import CHROME, FIREFOX, REMOTE
from pylenium.webdriver.driver_factories import ChromeDriverFactory, FireFoxDriverFactory, RemoteWebDriverFactory

log = logging.getLogger('pylenium')


class ThreadLocalDriverManager:

    def __init__(self):
        self.threaded_drivers = threading.local()
        self.threaded_drivers.drivers = {}
        self.config = PyleniumConfig()
        self.supported_drivers = {CHROME: partial(ChromeDriverFactory().get_driver),
                                  FIREFOX: partial(FireFoxDriverFactory().get_driver),
                                  REMOTE: partial(RemoteWebDriverFactory().get_driver)}

    def get_driver(self):
        """
        Spawns a new thread local driver or returns the already instantiated one if such a driver exists
        for the given thread
        :return: an instance of PyleniumDriver
        """
        driver = self._resolve_driver_from_config()
        return driver

    def _resolve_driver_from_config(self) -> PyleniumDriver:
        thread_id = threading.get_ident()
        driver = self.threaded_drivers.drivers.get(thread_id, None)
        if driver:
            return driver

        runtime_browser = self.config.browser

        if runtime_browser not in self.supported_drivers:
            raise PyleniumArgumentException(f"Unsupported --browser option, selection was {runtime_browser}")
        else:
            self.threaded_drivers.drivers[thread_id] = self.supported_drivers.get(runtime_browser)()
            return self.threaded_drivers.drivers.get(thread_id)
