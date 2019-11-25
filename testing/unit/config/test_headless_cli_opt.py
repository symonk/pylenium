# -*- coding: utf-8 -*-


def test_headless_enabled(testdir):
    testdir.makepyfile("""
        def test_headless_enabled(headless):
            assert headless
    """)
    result = testdir.runpytest(
        '--headless',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_headless_enabled PASSED*',
    ])
    assert result.ret == 0


def test_headless_disabled(testdir):
    testdir.makepyfile("""
        def test_headless_disabled(headless):
            assert not headless
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_headless_disabled PASSED*',
    ])
    assert result.ret == 0
