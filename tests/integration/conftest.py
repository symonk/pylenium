from pathlib import Path

from _pytest.pytester import Testdir
from pytest import fixture


class CustomTestdir(Testdir):
    server_url = None
    run_headless_it = None


@fixture(autouse=True)
def integration(request, httpserver) -> CustomTestdir:
    test_item = request.node
    html_arg = [
        list(marker.args)[0]
        for marker in test_item.own_markers
        if marker.name == "requires_html"
    ]
    if not html_arg:
        html_arg = ["blank.html"]
    if "integration" not in test_item.fixturenames:
        return

    # Test requires to be served HTML; at the moment we can only serve one file so we will pick the first
    root_content_path = Path.joinpath(Path(__file__).parent, "http_server_content")
    with open(Path.joinpath(root_content_path, html_arg[0]), "r") as file:
        httpserver.serve_content(file.read())

    integration: Testdir = request.getfixturevalue("testdir")

    def run_headless_it(*args, **kwargs):
        return integration.runpytest(
            "--headless", "--base-url", httpserver.url, *args, **kwargs
        )

    integration.server_url = httpserver.url
    integration.run_headless_it = run_headless_it
    yield integration
