from pytest import ExitCode


def test_browser_capabilities_not_a_py_file(testdir):
    testdir.makepyfile(
        """
        def test_browser_capabilities_not_a_py_file(request):
            pass
        """
    )
    result = testdir.runpytest("--browser-capabilities", "not-a-file")
    assert result.ret == ExitCode.USAGE_ERROR
    result.stderr.fnmatch_lines(
        ["ERROR: File path provided: not-a-file was not a .py file"]
    )


def test_browser_not_a_real_py_file(testdir):
    testdir.makepyfile(
        """
        def test_browser_not_a_real_py_file(request):
            pass
        """
    )
    result = testdir.runpytest("--browser-capabilities", "no.py")
    assert result.ret == ExitCode.USAGE_ERROR
    result.stderr.fnmatch_lines(
        ["ERROR: Pylenium was unable to find the file provided at: no.py"]
    )


def test_desired_caps_get_loaded_into_browser(testdir):
    capabilities = testdir.makepyfile(
        custom="""
        capabilities = {}
        capabilities['a'] = 1
        capabilities['b'] = 2
        capabilities['c'] = 3
        """
    )

    testdir.makepyfile(
        """
        def test_browser_capabilities_py_file(py_desired_caps):
            assert py_desired_caps['a'] == 1
            assert py_desired_caps['b'] == 2
            assert py_desired_caps['c'] == 3
        """
    )
    result = testdir.runpytest(
        "--browser-capabilities", capabilities, "--acquire-binary"
    )
    assert result.ret == ExitCode.OK
