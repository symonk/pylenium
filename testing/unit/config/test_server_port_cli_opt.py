# -*- coding: utf-8 -*-


def test_port_default(testdir):
    testdir.makepyfile("""
        def test_server_port(port):
            assert port == 4444
    """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_server_port PASSED*',
    ])
    assert result.ret == 0


def test_server_override(testdir):
    testdir.makepyfile("""
        def test_port_override(port):
            assert port == 9999
    """)
    result = testdir.runpytest(
        '--port=9999',
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_port_override PASSED*',
    ])
    assert result.ret == 0
