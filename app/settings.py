from pathlib import Path

APP_NAME = "Roblox Favorites Explorer"
VERSION = "0.1.0"

ROOT = Path(__file__).parent.parent

CACHE_DIR = ROOT / "cache"
EXPORT_DIR = ROOT / "exports"
LOG_DIR = ROOT / "logs"

CACHE_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

REQUEST_TIMEOUT = 20

THREADS = 8
