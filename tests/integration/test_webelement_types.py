import pytest
from pytest import ExitCode
from tests.integration.testdir_utilities import HTTP_SERVER_CONFTEST


@pytest.mark.skip
def test_web_element_types(testdir):
    testdir.makeconftest(HTTP_SERVER_CONFTEST)
    testdir.makepyfile(
        """
        def test_element_type(pydriver):
            from pylenium import PyleniumWebElement
            element = pydriver.find_element_by_id('simple_element')
            assert isinstance(element, PyleniumWebElement)
        """
    )
    result = testdir.runpytest(
        "--acquire-binary",
        "--base-url",
        "http://localhost:8080/simple_element.html",
        "--setup-show",
    )
    assert result.ret == ExitCode.OK
