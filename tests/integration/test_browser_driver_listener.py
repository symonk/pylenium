from pytest import ExitCode


def test_event_listener_is_wrapped(integration):
    pkg, mod, clazz = "tpkg", "tmod", "Wrapper"
    pkg_file = integration.mkpydir(pkg)
    mod_file = integration.makepyfile(
        tmod="""
    from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener

    class {clazz}(AbstractEventListener):
        pass

    """
    )
    mod_file.move(pkg_file.join(mod_file.basename))
    expected = f"{pkg}.{mod}.{clazz}"
    integration.makepyfile(
        """
    def test_event_listener_is_wrapped(pydriver):
        from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
        assert isinstance(pydriver, EventFiringWebDriver)
    """
    )
    integration.syspathinsert(path=pkg_file)
    result = integration.run_headless_it(f"--driver-listener={expected}")
    assert result.ret == ExitCode.OK
