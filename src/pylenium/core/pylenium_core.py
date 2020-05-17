from dataclasses import dataclass
from selenium.webdriver.common.by import By


@dataclass(frozen=True)
class Locatable:
    by: By
    selector: str

    def __call__(self):
        pass


def id(selector: str) -> Locatable:
    """
    Pylenium ID locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.ID, selector)


def xpath(selector: str) -> Locatable:
    """
    Pylenium xpath locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.XPATH, selector)


def link_text(selector: str) -> Locatable:
    """
    Pylenium link text locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.LINK_TEXT, selector)


def partial_link_text(selector: str) -> Locatable:
    """
    Pylenium partial link text locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.PARTIAL_LINK_TEXT, selector)


def name(selector: str) -> Locatable:
    """
    Pylenium name locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.NAME, selector)


def tag_name(selector: str) -> Locatable:
    """
    Pylenium tag name locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.TAG_NAME, selector)


def class_name(selector: str) -> Locatable:
    """
    Pylenium class name locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.CLASS_NAME, selector)


def css(selector: str):
    """
    Pylenium css locator
    :param selector: the string of the selector for us to do lookup of
    :return: an instance of Locator (By and selector encapsulated together)
    """
    return Locatable(By.CSS_SELECTOR, selector)
