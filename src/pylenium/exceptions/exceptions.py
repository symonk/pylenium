# Pylenium custom exceptions


class DialogTextMisMatch(Exception):
    pass


class ElementIsNotClickable(Exception):
    pass


class ElementNotFound(Exception):
    pass


class ElementShould(Exception):
    pass


class ElementShouldNot(Exception):
    pass


class InvalidStateException(Exception):
    pass


class ListSizeMisMatch(Exception):
    pass


class SoftAssertion(Exception):
    pass


class TextsMisMatch(Exception):
    pass


class TimeoutException(Exception):
    pass


class UIAssertionException(Exception):
    pass


class PyPageException(Exception):
    pass


class PyleniumProxyException(Exception):
    pass
