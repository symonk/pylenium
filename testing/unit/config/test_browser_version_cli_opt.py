# -*- coding: utf-8 -*-


def test_default(testdir):
    testdir.makepyfile(
        """
        def test_default(browser_version):
            assert browser_version == 'latest'
    """
    )
    result = testdir.runpytest("-v")
    result.stdout.fnmatch_lines(
        ["*::test_default PASSED*", ]
    )
    assert result.ret == 0


def test_override(testdir):
    testdir.makepyfile(
        """
        def test_override(browser_version):
            assert browser_version == 'v78.12323'
    """
    )
    result = testdir.runpytest("--browser-version=v78.12323", "-v")
    result.stdout.fnmatch_lines(
        ["*::test_override PASSED*", ]
    )
    assert result.ret == 0
