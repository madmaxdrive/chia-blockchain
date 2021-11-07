import os
from pathlib import Path

from chia.util.config import _constants

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv(f"{_constants()['name'].upper()}", f"~/.{_constants()['name']}/mainnet"))).resolve()
