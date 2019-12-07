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
from pylenium.core.navigator import Navigator
from pylenium.elements.pylenium_element import PyleniumElement
from pylenium.waiting.pylenium_wait import PyleniumWait


class PyleniumDriver:

    def __init__(self, config, driver_to_wrap):
        self.config = config
        self.wrapped_driver = driver_to_wrap
        self.wrapped_driver._web_element_cls = PyleniumElement
        self.navigator = Navigator()

    def open(self, url):
        return self.navigator.open(self.wrapped_driver, url)

    def wait(self) -> PyleniumWait:
        return PyleniumWait(self.wrapped_driver, self.config.explicit_wait, self.config.polling_interval)
