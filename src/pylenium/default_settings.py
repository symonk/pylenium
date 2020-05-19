from typing import Callable, Optional

from pylenium.constants.strings import CHROME
from pylenium.constants.strings import GRID_LOCALHOST

BROWSER = CHROME
HEADLESS = False
SELENIUM_GRID_URL: str = GRID_LOCALHOST
BROWSER_RESOLUTION: str = "1280x1024"
BROWSER_VERSION: str = "latest"
DRIVER_BINARY_PATH: str = "acquire"
browser_capabilities: Optional[dict] = {}
CHROME_OPTS: Optional[list] = None
BASE_URL: Optional[str] = None
EXPLICIT_WAIT: int = 30
POLLING_INTERVAL: float = 0.25
PAGE_SOURCE_ON_FAIL: bool = False
SCREENSHOT_ON_FAIL: bool = False
STACK_TRACE_ON_FAIL: bool = False
CLICK_WITH_JAVASCRIPT: bool = False
SENDKEYS_WITH_JAVASCRIPT: bool = False
DEFAULT_SELECTOR: str = "id"
DRIVER_LISTENER: Optional[Callable] = None
BROWSER_NOT_MAXIMIZED: bool = False
