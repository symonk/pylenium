from selenium.webdriver.remote.webelement import WebElement


class PyleniumWebElement(WebElement):
    def __init__(self, parent, id_, w3c=False):
        super().__init__(parent, id_, w3c)
