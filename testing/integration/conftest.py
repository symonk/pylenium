import os
import time
from subprocess import Popen

import pytest

PORT = "1337"
DIRECTORY = os.path.join(__file__.replace("conftest.py", ""), "static_content")


@pytest.fixture(scope="session", autouse=True)
def pylenium_httpserver(request):
    os.chdir(DIRECTORY)
    server_process = Popen(["python", "-m", "http.server", PORT])
    time.sleep(1)
    request.addfinalizer(server_process.kill)
