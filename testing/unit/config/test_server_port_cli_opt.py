# -*- coding: utf-8 -*-


def test_default(testdir):
    testdir.makepyfile(
        """
        def test_default(server_port):
            assert server_port == 4444
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
        def test_override(server_port):
            assert server_port == 9999
    """
    )
    result = testdir.runpytest("--server_port=9999", "-v")
    result.stdout.fnmatch_lines(
        ["*::test_override PASSED*",]
    )
    assert result.ret == 0
