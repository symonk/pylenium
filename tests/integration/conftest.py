from threading import Thread

from pytest import fixture
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from os import path


class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        tests_dir = path.abspath(path.abspath(path.curdir))
        servable_content = path.join(tests_dir, "http_server_content")
        super().__init__(*args, directory=servable_content, **kwargs)


@fixture(scope="session", autouse=True)
def local_http_server(request) -> None:
    """
    Starts a local http server for selenium based integration testing; this only happens during integration tests
    as any test in here should be exercising real life browser type behaviour
    :param request: the pytest request fixture
    """
    if _is_xdist_worker_or_master(request.config):
        server = HTTPServer(
            server_address=("", 8080), RequestHandlerClass=CustomHandler
        )
        threaded_server = Thread(target=server.serve_forever, daemon=True)
        yield threaded_server.start()


def _is_xdist_worker_or_master(config) -> bool:
    """
    Attempt to retrieve a gatewayid for xdist runs.
    note: xdist does not honor session scope fixtures so it would launch N http servers
    This way we check for the worker and only do this if (master) aka noxdist or gw0 the initial xdist slave
    :param config: the pytest config object
    :return: a boolean indicating if it is ok to do work for one process or is sequential
    """
    gatewayid = "master"
    try:
        gatewayid = config.slaveinput["slave_id"]
    except AttributeError:
        return gatewayid in {"master", "gw0"}
