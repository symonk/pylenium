# -*- coding: utf-8 -*-


def test_remote_enabled(testdir):
    testdir.makepyfile("""
        def test_remote_enabled(remote):
            assert remote
    """)
    result = testdir.runpytest(
        '--remote',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_remote_enabled PASSED*',
    ])
    assert result.ret == 0


def test_remote_disabled(testdir):
    testdir.makepyfile("""
        def test_remote_disabled(remote):
            assert not remote
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_remote_disabled PASSED*',
    ])
    assert result.ret == 0


def test_remote_with_browser_equals(testdir):
    pass
