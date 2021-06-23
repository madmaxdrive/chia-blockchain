import os
from pathlib import Path

from chia.util.config import _constants

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("CHIA_ROOT", f"~/.{_constants()['name']}/mainnet"))).resolve()
