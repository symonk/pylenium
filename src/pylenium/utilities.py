import logging
import os
from runpy import run_path

from pylenium.exceptions.exceptions import PyleniumEventFiringWrapperException
from pylenium.string_globals import PYTEST_XDIST_WORKER

log = logging.getLogger("Pylenium")


def is_master_process():
    """
    Determines if the currently executing process is that of the master node and not a XDIST worker process
    :return: bool indicating if the execution is occuring on the master node
    n.b -> This is important to prevent plugin from being spammed by all x-dist processes
    """
    return not os.environ.get(PYTEST_XDIST_WORKER)


def plugin_log_seperate(number_of_stars: int = 30):
    log.info("*****" * number_of_stars)


def plugin_log_message(message: str):
    log.info(message)


def is_a_file(file_path: str) -> bool:
    """
    Simple check on a given file path to see if it is a valid file
    useful to avoid FileNotFoundErrors etc
    :param file_path: the file path on the system to look for the file
    :return: True if the file does exist
    """
    return os.path.exists(file_path)


def get_instance_of_listener_from_path(module_file_path):
    if is_a_file(module_file_path):
        event_listener_module = run_path(module_file_path)
        return event_listener_module["PyleniumEventListener"]()
    else:
        raise PyleniumEventFiringWrapperException(
            "--driver-listener= path was not found, is it correct?"
        )
