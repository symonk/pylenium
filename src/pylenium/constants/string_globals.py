#  MIT License
#
#  Copyright (c) 2019 Simon Kerr
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
#  Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
#  NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from pylenium._version import VERSION

PYLENIUM = "Pylenium"
CHROME = "CHROME"
FIREFOX = "FIREFOX"
REMOTE = "REMOTE"
LOCALHOST_URL = "http://localhost:8080"

# PYTEST XDIST
PYTEST_XDIST_WORKER = "PYTEST_XDIST_WORKER"

# PLUGIN MISC
EXEC_STARTED = "Pylenium-pytest has been loaded... Firing on all cylinders!"
RELEASE_INFO = (
    f"Pylenium is currently in its alpha stage(s), version detected {VERSION}"
)
GRATITUDE_MSG = "We appreciate your feedback here: https://github.com/symonk/pylenium"
NO_CAP_FILE_FOUND_EXCEPTION = (
    "Unable to find the file you specified for --browser-capabilities-file"
)
CAP_FILE_YAML_FORMAT_NOT_ACCEPTABLE = (
    "Unable to parse the YAML file for capabilities, ensure it meets the YAML spec"
)
