from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class PyleniumEventListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Navigating to!")
