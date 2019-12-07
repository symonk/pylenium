# -*- coding: utf-8 -*-


def test_default(testdir):
    testdir.makepyfile("""
        def test_default(remote):
            assert not remote
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
        def test_override(remote):
            assert remote
    """)
    result = testdir.runpytest(
        '--remote',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_override PASSED*',
    ])
    assert result.ret == 0
