import pytest
from pytest import ExitCode


@pytest.mark.requires_html("simple_element.html")
def test_web_element_types(integration):
    integration.makepyfile(
        """
        def test_element_type(pydriver):
            from pylenium import PyleniumWebElement
            element = pydriver.find_element_by_id('simple_element')
            assert isinstance(element, PyleniumWebElement)
        """
    )
    result = integration.run_headless_it()
    assert result.ret == ExitCode.OK
