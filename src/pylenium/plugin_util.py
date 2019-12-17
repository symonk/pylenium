import logging
import os

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
