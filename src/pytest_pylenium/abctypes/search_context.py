from abc import ABC, abstractmethod
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ISearchContext(metaclass=ABC):

    @abstractmethod
    def find_element(self, by: By, value=None) -> WebElement:
        raise NotImplementedError

    @abstractmethod
    def find_elements(self, by: By, value=None) -> List[WebElement]:
        raise NotImplementedError
