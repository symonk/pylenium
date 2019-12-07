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
    testdir.makepyfile("""
        def test_default(default_selector):
            assert default_selector == 'css'
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_default PASSED*',
    ])
    assert result.ret == 0


def test_override_id(testdir):
    testdir.makepyfile("""
        def test_override(default_selector):
            assert default_selector == 'id'
    """)
    result = testdir.runpytest(
        '--default-selector=id',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_override PASSED*',
    ])
    assert result.ret == 0


def test_override_xpath(testdir):
    testdir.makepyfile("""
        def test_override(default_selector):
            assert default_selector == 'id'
    """)
    result = testdir.runpytest(
        '--default-selector=id',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_override PASSED*',
    ])
    assert result.ret == 0


def test_override_unsupported(testdir):
    testdir.makepyfile("""
        def test_override(default_selector):
            pass
    """)
    result = testdir.runpytest(
        '--default-selector=xpath',
        '-v'
    )
    result.stderr.fnmatch_lines([
        "*--default-selector: invalid choice: 'xpath' (choose from 'css', 'id')*"
    ])
    assert result.ret == 4
