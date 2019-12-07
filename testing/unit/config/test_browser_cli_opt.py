# -*- coding: utf-8 -*-


def test_default(testdir):
    testdir.makepyfile("""
        def test_default(browser):
            assert browser == "CHROME"
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_default PASSED*',
    ])
    assert result.ret == 0


def test_override(testdir):
    testdir.makepyfile("""
        def test_override(browser):
            assert browser == "firefox"
    """)
    result = testdir.runpytest(
        '--browser=firefox',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_override PASSED*',
    ])
    assert result.ret == 0
