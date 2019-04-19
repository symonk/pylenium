from __future__ import annotations
from concurrent.futures.thread import ThreadPoolExecutor

import pytest

from conditions.condition import Text
from core.pylenium import start, find, terminate, By


class TestOpen(object):

    # Page Objects and business logic sold separately!
    @pytest.mark.skip
    def test_my_login(self):
        start('https://www.google.co.uk')
        find(By.NAME, 'q').set_value("Cheese!")
        find(By.CSS_SELECTOR, '#submit').click()
        find(By.CSS_SELECTOR, '#password').should_have(Text("Hello, Simon!"))
        terminate()

    @pytest.mark.travis
    def test_travis(self):
        google = 'https://www.google.co.uk/'
        actual = start(google).url()
        assert actual == google

    @pytest.mark.travis
    def test_travis2(self):
        google = 'https://www.google.co.uk/'
        actual = start(google).url()
        assert actual == google

    @pytest.mark.travis
    def test_travis3(self):
        google = 'https://www.google.co.uk/'
        actual = start(google).url()
        assert actual == google
