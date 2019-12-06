# -*- coding: utf-8 -*-


def test_resolution_default(testdir):
    testdir.makepyfile("""
        def test_default_browser_res(browser_resolution):
            assert browser_resolution == '1920x1080'
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_default_browser_res PASSED*',
    ])
    assert result.ret == 0


def test_resolution_override(testdir):
    testdir.makepyfile("""
        def test_override_browser_res(browser_resolution):
            assert browser_resolution == '1280x1024'
    """)
    result = testdir.runpytest(
        '--browser-resolution=1280x1024',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_override_browser_res PASSED*',
    ])
    assert result.ret == 0
