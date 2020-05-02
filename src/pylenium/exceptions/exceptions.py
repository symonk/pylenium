class NoThreadedDriverFoundException(Exception):
    """
    Raised when attempting to fetch a driver from the thread local storage but none exists for the current threading id
    note: User should never really be able to get into this state; likely indicates a core pylenium defect
    """


class InvalidUrl(Exception):
    """
    Raised on various parseargs options when expecting a URL could not be successfully validated as a valid URL
    """


class NoCapabilitiesDictionaryException(Exception):
    """
    Raised when parsing user provided desired capabilities for browsers through --browser-capabilities
    Note: We check the provided .py module for a 'capabilities' dictionary explicitly; naming it otherwise will
    not work.
    """
