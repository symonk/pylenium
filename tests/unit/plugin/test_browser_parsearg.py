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

#  MIT License
#
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#
from pytest import ExitCode


def test_default_browser_is_chrome(testdir):
    testdir.makepyfile(
        """
    def test_default_browser_is_chrome(request):
        assert request.config.getoption('browser') == 'chrome'
    """
    )
    result = testdir.inline_run()
    assert result.ret == ExitCode.OK


def test_overriding_to_firefox_is_supported(testdir):
    testdir.makepyfile(
        """
    def test_browser_can_be_firefox(request):
        assert request.config.getoption('browser') == 'firefox'
    """
    )
    result = testdir.inline_run("--browser=Firefox")
    assert result.ret == ExitCode.OK


def test_cannot_set_browser_to_supported_choice(testdir):
    testdir.makepyfile(
        """
    def test_browser_can_be_firefox(request):
        pass
    """
    )
    result = testdir.runpytest("--browser=Unsupported")
    result.stderr.fnmatch_lines(["*--browser: invalid choice: 'Unsupported'*"])
    assert result.ret == ExitCode.USAGE_ERROR
