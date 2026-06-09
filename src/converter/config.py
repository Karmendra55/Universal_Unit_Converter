"""
Application configuration.

Defines project paths, data storage
locations and export directories used
throughout the application.
"""

from pathlib import Path

# Project root directory.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Application data directories.
DATA_DIR = PROJECT_ROOT / "data"
EXPORT_DIR = PROJECT_ROOT / "exports"

DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

EXPORT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

# Persistent storage files.
HISTORY_FILE = DATA_DIR / "history.json"
FAVORITES_FILE = DATA_DIR / "favorites.json"
SETTINGS_FILE = DATA_DIR / "settings.json"

# Currency-related files.
CURRENCY_CACHE_FILE = DATA_DIR / "currency_cache.json"
CURRENCY_ABBR_FILE = DATA_DIR / "currency_abbr.json"
CURRENCY_FAVORITES_FILE = DATA_DIR / "currency_favorites.json"