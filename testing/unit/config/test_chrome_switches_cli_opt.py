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
NO_CHROME_SWITCHES = 'pylenium.exceptions.custom_exceptions.PyleniumCommandLineArgException: ' \
                     'Attempting to use the chrome_switches fixture without --chrome-switches'
CHROME_SWITCHES_WITHOUT_CHROME = ' pylenium.exceptions.custom_exceptions.PyleniumCommandLineArgException: ' \
                                 'Attempting to use the chrome_switches fixture with non chrome browser'


def test_switches(testdir):
    testdir.makepyfile(
        """
        def test_default(chrome_switches):
            assert len(chrome_switches) == 2
            assert chrome_switches[0] == '--headless'
            assert chrome_switches[1] == '--hide-icons'
    """
    )
    result = testdir.runpytest("--chrome-switches=--headless,--hide-icons", "-v")
    result.stdout.fnmatch_lines(
        ["*::test_default PASSED*",]
    )
    assert result.ret == 0


def test_no_switches_with_fixture(testdir):
    testdir.makepyfile(
        """
        def test_default(chrome_switches):
            pass
    """
    )
    result = testdir.runpytest("-v")
    result.stdout.fnmatch_lines(
        [f"*{NO_CHROME_SWITCHES}*", ]
    )
    assert result.ret == 1


def test_switches_without_chrome(testdir):
    testdir.makepyfile(
        """
        def test_default(chrome_switches):
            pass
    """
    )
    result = testdir.runpytest("--browser=firefox","-v")
    result.stdout.fnmatch_lines(
        [f"*{CHROME_SWITCHES_WITHOUT_CHROME}*", ]
    )
    assert result.ret == 1
