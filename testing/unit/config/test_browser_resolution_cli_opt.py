# -*- coding: utf-8 -*-


def test_default(testdir):
    testdir.makepyfile(
        """
        def test_default(browser_resolution):
            assert browser_resolution == '1920x1080'
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
        def test_override(browser_resolution):
            assert browser_resolution == '1280x1024'
    """
    )
    result = testdir.runpytest("--browser-resolution=1280x1024", "-v")
    result.stdout.fnmatch_lines(
        ["*::test_override PASSED*",]
    )
    assert result.ret == 0
