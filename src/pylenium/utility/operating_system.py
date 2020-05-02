from pytest import UsageError
from os.path import isfile


def is_py_file(path: str) -> None:
    """
    Raise a pytest UsageError if the path provided is not one of a valid .py file
    :param path: the file path passed as an arg to some command line options
    """
    if not path.endswith(".py"):
        raise UsageError(f"File path provided: {path} was not a .py file")
    if not isfile(path):
        raise UsageError(f"Pylenium was unable to find the file provided at: {path}")
