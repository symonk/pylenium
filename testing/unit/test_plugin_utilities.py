from pylenium.constants.string_globals import PYTEST_XDIST_WORKER
from pylenium.utilities.plugin_utility import is_master_process


def test_is_master_on_xdist_worker(monkeypatch):
    monkeypatch.setenv(PYTEST_XDIST_WORKER, "gw100")
    assert not is_master_process()


def test_is_master_on_master():
    assert is_master_process()
