from typing import Callable


def _locatable(selector: str, locator_type: id) -> Callable:
    """
    Lazily used in page objects to store a locator, this returns a callable used by the driver when the time comes to
    actually interact with the element
    :return:
    """
    return lambda: 0


def xpath(selector: str) -> Callable:
    """
    Pylenium xpath locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of callable that can be used to find the element
    """
    return _locatable(selector, "xpath")


def css(selector: str):
    """
    Pylenium css locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of callable that can be used to find the element
    """
    return _locatable(selector, "css")
