
from pytest import ExitCode


def test_event_listener_can_be_passed(testdir):
    pkg, mod, clazz = "mypackage", "mymodule", "MyEventListenerClazz"
    pkg_file = testdir.mkpydir(pkg)
    mod_file = testdir.makepyfile(
        mymodule=f"""
    from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener

    class {clazz}(AbstractEventListener):
        pass

    """
    )
    mod_file.move(pkg_file.join(mod_file.basename))
    expected = f"{pkg}.{mod}.{clazz}"
    testdir.makepyfile(
        f"""
    def test_event_listener(request):
        from mymodule import {clazz}
        assert isinstance(request.config.getoption('driver_listener')(), {clazz})
    """
    )
    testdir.syspathinsert(path=pkg_file)
    result = testdir.runpytest(f"--driver-listener={expected}")
    assert result.ret == ExitCode.OK


def test_no_listener_is_none_by_default(testdir):
    testdir.makepyfile(
        f"""
       def test_event_listener(request):
           assert request.config.getoption('driver_listener') is None
       """
    )
    result = testdir.runpytest()
    assert result.ret == ExitCode.OK


def test_no_such_class_found_raises(testdir):
    testdir.makepyfile(
        f"""
       def test_no_valid_listener(request):
           pass
       """
    )
    result = testdir.runpytest("--driver-listener", "a.b.C")
    assert result.ret == ExitCode.USAGE_ERROR
    result.stderr.fnmatch_lines(
        ["*ERROR: Unable to find the event driver subclass in b.C"]
    )
