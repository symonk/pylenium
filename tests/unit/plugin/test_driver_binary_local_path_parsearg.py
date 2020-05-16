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


def test_driver_binary_path_default(testdir):
    testdir.makepyfile(
        """
    def test_driver_binary_path_default(request):
        assert request.config.getoption('driver_binary_path') is 'acquire'
        """
    )
    result = testdir.inline_run()
    assert result.ret == ExitCode.OK


def test_driver_binary_path_custom(testdir):
    testdir.makepyfile(
        """
    def test_driver_binary_path_custom(request):
        assert request.config.getoption('driver_binary_path') == '~/dummydir/binary.exe'
    """
    )
    result = testdir.inline_run("--driver-binary-path", "~/dummydir/binary.exe")
    assert result.ret == ExitCode.OK
