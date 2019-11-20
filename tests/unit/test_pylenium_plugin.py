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
