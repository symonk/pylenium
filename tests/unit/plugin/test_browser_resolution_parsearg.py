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
from pytest import ExitCode


def test_default_browser_resolution(testdir):
    testdir.makepyfile(
        """
    def test_default_browser_resolution(request):
        width, height = request.config.getoption('browser_resolution')
        assert width == '1280'
        assert height == '1024'
    """
    )
    result = testdir.inline_run()
    assert result.ret == ExitCode.OK


def test_browser_resolution_custom(testdir):
    testdir.makepyfile(
        """
    def test_default_browser_resolution(request):
        width, height = request.config.getoption('browser_resolution')
        assert width == '1920'
        assert height == '1080'
    """
    )
    result = testdir.runpytest(
        "--browser-resolution", "1920x1080", "--not-maximized", "--acquire-binary"
    )
    assert result.ret == ExitCode.OK
