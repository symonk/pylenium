# -*- coding: utf-8 -*-


def test_version_default(testdir):
    testdir.makepyfile("""
        def test_default_browser_version(browser_version):
            assert browser_version == 'latest'
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_default_browser_version PASSED*',
    ])
    assert result.ret == 0


def test_version_override(testdir):
    testdir.makepyfile("""
        def test_override_browser_version(browser_version):
            assert browser_version == 'v78.12323'
    """)
    result = testdir.runpytest(
        '--browser-version=v78.12323',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_override_browser_version PASSED*',
    ])
    assert result.ret == 0
