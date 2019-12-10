# -*- coding: utf-8 -*-


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
        def test_default(browser_capabilities_file):
            assert not browser_capabilities_file
    """
    )
    result = testdir.runpytest("-v")
    result.stdout.fnmatch_lines(
        ["*::test_default PASSED*",]
    )
    assert result.ret == 0


def test_cap_file_dict(testdir):
    testdir.makepyfile(
        """
        def test_override(pylenium_config):
            assert isinstance(pylenium_config.browser_capabilities, dict)
            assert pylenium_config.browser_capabilities['os'] == 'Windows'
            assert pylenium_config.browser_capabilities['os_version'] == 'Sierra'
            assert pylenium_config.browser_capabilities['browser'] == 'Chrome'
            assert pylenium_config.browser_capabilities['browser_version'] == '79.0'
            assert pylenium_config.browser_capabilities['browserstack.local'] == 'false'
            assert pylenium_config.browser_capabilities['browserstack.selenium_version'] == '3.14.0'
            assert pylenium_config.browser_capabilities['browserstack.chrome.driver'] == '2.43'
    """
    )
    result = testdir.runpytest(
        "--browser-capabilities-file=C://workspace//pylenium//testing//test_files//browser_stack_capabilities.yaml", "-v"
    )
    result.stdout.fnmatch_lines(
        ["*::test_override PASSED*",]
    )
    assert result.ret == 0


def test_cannot_find_yaml_file(testdir):
    testdir.makepyfile(
        """
        def test_override(pylenium_config):
        from pylenium.exceptions.exceptions import PyleniumCapabilitiesException
            with pytest.raises(PyleniumCapabilitiesException) as e_info:
                pass
    """
    )
    result = testdir.runpytest(
        "--browser-capabilities-file=nofile", "-v"
    )
    result.stderr.fnmatch_lines(
        ["*pylenium.exceptions.exceptions.PyleniumCapabilitiesException*",]
    )
    assert result.ret == 3


def test_yaml_bad_format(testdir):
    testdir.makepyfile(
        """
        def test_override(pylenium_config):
        from pylenium.exceptions.exceptions import PyleniumInvalidYamlException
            with pytest.raises(PyleniumInvalidYamlException) as e_info:
                pass
    """
    )
    result = testdir.runpytest(
        "--browser-capabilities-file=C://workspace//pylenium//testing//test_files//bad_yaml_format.yaml", "-v"
    )
    result.stderr.fnmatch_lines(
        ["*pylenium.exceptions.exceptions.PyleniumInvalidYamlException*",]
    )
    assert result.ret == 3
