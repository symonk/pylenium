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
from selenium.webdriver.common import by


def id(value: str):
    return by.ID(value)


def xpath(value: str):
    return by.XPATH(value)


def link_text(value: str):
    return by.LINK_TEXT(value)


def partial_link_text(value: str):
    return by.PARTIAL_LINK_TEXT(value)


def name(value: str):
    return by.NAME(value)


def tag_name(value: str):
    return by.TAG_NAME(value)


def class_name(value: str):
    return by.CLASS_NAME(value)


def css(value: str):
    return by.CSS_SELECTOR(value)


def find(locator):
    pass


def find_all(locator):
    pass
