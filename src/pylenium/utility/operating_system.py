from typing import Dict

from pytest import UsageError
from pylenium.exceptions.exceptions import NoCapabilitiesDictionaryException
from os.path import isfile
import importlib.util


def is_py_file(path: str) -> str:
    """
    Raise a pytest UsageError if the path provided is not one of a valid .py file
    :param path: the file path passed as an arg to some command line options
    :return: the path if it was successfully located
    """
    if not path.endswith(".py"):
        raise UsageError(f"File path provided: {path} was not a .py file")
    if not isfile(path):
        raise UsageError(f"Pylenium was unable to find the file provided at: {path}")
    return path


def parse_capabilities_from_disk(path: str) -> Dict:
    """
    Takes the path provided to --browser-capabilities; loads it and attempts to discovery a 'capabilities' dictionary.
    Note: This must be explicitly called 'capabilities' and should be of <class 'dict'>
    :param path: the path on the file system to load
    :return: The dictionary of desired capabilities that we found
    """
    is_py_file(path)
    spec = importlib.util.spec_from_file_location(name="py_desired_caps", location=path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:
        caps = mod.capabilities
        if not isinstance(caps, Dict):
            raise ValueError(
                f"The .py file provided: {path} contained a 'capabilities' attribute, but it was not of"
                f"type<Dict>"
            )
        return caps
    except AttributeError:
        raise NoCapabilitiesDictionaryException(
            f"The .py file provided: {path} did not have a 'capabilities' attribute"
            f"Make sure it contains one, explicitly called 'capabilities'"
        ) from None
