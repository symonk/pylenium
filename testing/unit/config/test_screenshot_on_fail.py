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


def test_default(testdir):
    testdir.makepyfile(
        """
        def test_default(store_screenshot_on_fail):
            assert not store_screenshot_on_fail
    """
    )
    result = testdir.runpytest("-v")
    result.stdout.fnmatch_lines(
        ["*::test_default PASSED*",]
    )
    assert result.ret == 0


def test_override(testdir):
    testdir.makepyfile(
        """
        def test_override(store_screenshot_on_fail):
            assert store_screenshot_on_fail
    """
    )
    result = testdir.runpytest("--screenshot-on-fail=True", "-v")
    result.stdout.fnmatch_lines(
        ["*::test_override PASSED*",]
    )
    assert result.ret == 0
