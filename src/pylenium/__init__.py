import logging
import sys

from . import _version as __version__
from pylenium.pylenium_core import find, find_all

__all__ = ["__version__", "find", "find_all"]

log = logging.getLogger("Pylenium")
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
