# -*- coding: utf-8 -*-


def test_default(testdir):
    testdir.makepyfile(
        """
        def test_default(server):
            assert server == 'http://localhost'
    """
    )
    result = testdir.runpytest("-v")
    result.stdout.fnmatch_lines(
        ["*::test_default PASSED*",]
    )
    assert result.ret == 0


def test_server_override(testdir):
    testdir.makepyfile(
        """
        def test_server_override(server):
            assert server == '10.0.0.1'
    """
    )
    result = testdir.runpytest("--server=10.0.0.1", "-v")
    result.stdout.fnmatch_lines(
        ["*::test_server_override PASSED*",]
    )
    assert result.ret == 0
