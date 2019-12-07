import logging
import sys

from . import _version as __version__

__all__ = ["__version__"]

log = logging.getLogger("Pylenium")
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
