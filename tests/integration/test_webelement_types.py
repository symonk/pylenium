from pytest import ExitCode


def test_web_element_types(testdir):
    testdir.makepyfile(
        """
        def test_element_type(pydriver):
            from selenium.webdriver.remote.webdriver import WebDriver
            assert isinstance(pydriver, WebDriver)
        """
    )
    result = testdir.runpytest("--acquire-binary", "--headless")
    assert result.ret == ExitCode.OK
