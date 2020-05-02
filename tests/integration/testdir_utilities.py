
HTTP_SERVER_CONFTEST = """
from threading import Thread

from pytest import fixture
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from os import path


class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        tests_dir = path.abspath(path.abspath(path.curdir))
        servable_content = path.join(tests_dir, "http_server_content")
        raise Exception(servable_content)
        super().__init__(*args, directory=servable_content, **kwargs)


@fixture(scope="session", autouse=True)
def local_http_server(request) -> None:
    if _is_xdist_worker_or_master(request.config):
        server = HTTPServer(
            server_address=("", 8080), RequestHandlerClass=CustomHandler
        )
        threaded_server = Thread(target=server.serve_forever, daemon=True)
        yield threaded_server.start()


def _is_xdist_worker_or_master(config) -> bool:
    gatewayid = "master"
    try:
        gatewayid = config.slaveinput["slave_id"]
    except AttributeError:
        return gatewayid in {"master", "gw0"}

"""
