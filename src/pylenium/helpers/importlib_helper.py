def load_module_dict_from_path(path: str) -> dict:
    """
    Given a path, loads the module and returns its dictionary.  Pylenium uses this for a couple of things,
    loading a overridable settings config file as well as instantiating an instance of an event listener for selenium.
    :param path:
    :return:
    """
