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


def test_default_commmand_executor(testdir):
    testdir.makepyfile(
        """
    def test_default_commmand_executor(request):
        from pylenium import GRID_LOCALHOST
        assert request.config.getoption('selenium_grid_url') == GRID_LOCALHOST
    """
    )
    result = testdir.inline_run()
    assert result.ret == ExitCode.OK


def test_default_commmand_executor_override(testdir):
    testdir.makepyfile(
        """
    def test_default_commmand_executor_override(request):
        assert request.config.getoption('selenium_grid_url') == "https://10.0.0.1:4444/wd/hub"
    """
    )
    result = testdir.runpytest("--command-executor", "https://10.0.0.1:4444/wd/hub")
    assert result.ret == ExitCode.OK
