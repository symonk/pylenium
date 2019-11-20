from abc import ABC, abstractmethod
from typing import List

from selenium.webdriver.remote.webelement import WebElement


class IPyleniumElementLocator(metaclass=ABC):

    @abstractmethod
    def find(self) -> WebElement:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    def __str__(self):
        return self.description


class IPyleniumListElementLocator(metaclass=ABC):

    @abstractmethod
    def find(self) -> List[WebElement]:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    def __str__(self):
        return self.description
