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


def test_valid_file_is_ok(testdir):
    capabilities = testdir.makepyfile(
        """
        capabilities = {}
        """
    )
    testdir.makepyfile(
        """
        def test_browser_capabilities_py_file(request):
            pass
        """
    )
    result = testdir.runpytest("--browser-capabilities", capabilities)
    assert result.ret == ExitCode.OK
