from pytest import ExitCode


def test_chrome_opts_default_is_empty(testdir):
    testdir.makepyfile(
        """
    def test_chrome_opts_default_is_empty(request):
        assert not request.config.getoption('chrome_opts')
    """
    )
    result = testdir.inline_run()
    assert result.ret == ExitCode.OK


def test_chrome_opts_can_be_overwritten(testdir):
    testdir.makepyfile(
        """
    def test_chrome_opts_can_be_overwritten(request):
        opts = request.config.getoption('chrome_opts')
        assert {'--headless', '--disablegpu', 'blah'} == opts
    """
    )
    result = testdir.runpytest("--chrome-opts", "--headless, --disablegpu, blah")
    assert result.ret == ExitCode.OK
