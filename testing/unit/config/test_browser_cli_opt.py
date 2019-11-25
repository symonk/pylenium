# -*- coding: utf-8 -*-


def test_browser_chrome(testdir):
    testdir.makepyfile("""
        def test_chrome(browser):
            assert browser == "chrome"
    """)
    result = testdir.runpytest(
        '--browser=chrome',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_chrome PASSED*',
    ])
    assert result.ret == 0


def test_browser_without_anything(testdir):
    testdir.makepyfile("""
        def test_no_argument(browser):
            assert browser == "CHROME"
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_no_argument PASSED*',
    ])
    assert result.ret == 0


def test_browser_firefox(testdir):
    testdir.makepyfile("""
        def test_firefox(browser):
            assert browser == "firefox"
    """)
    result = testdir.runpytest(
        '--browser=firefox',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_firefox PASSED*',
    ])
    assert result.ret == 0
