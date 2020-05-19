from pytest import ExitCode


def test_base_url_loading_is_correct(request, integration):
    integration.makepyfile(
        f"""
        def test_base_url_loading(pydriver):

            assert pydriver.current_url == "{integration.server_url}/"
        """
    )
    result = integration.run_headless_it()
    assert result.ret == ExitCode.OK


def test_base_url_invalid_url(testdir):
    testdir.makepyfile(
        """
        def test_base_url_loading(pydriver):
            pass
        """
    )
    result = testdir.runpytest("--base-url", "goog", "--headless")
    assert result.ret == ExitCode.USAGE_ERROR
    result.stderr.fnmatch_lines(["ERROR: url: goog was not a valid url"])
