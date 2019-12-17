from ._version import VERSION

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
NO_CAP_FILE_FOUND_EXCEPTION = "Unable to find the file you specified for --browser-capabilities-file"
CAP_FILE_YAML_FORMAT_NOT_ACCEPTABLE = "Unable to parse the YAML file for capabilities, ensure it meets the YAML spec"
