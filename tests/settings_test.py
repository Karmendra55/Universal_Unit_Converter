import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.engine import ConversionEngine

engine = ConversionEngine()

print(
    engine.get_settings()
)

engine.update_setting(
    "precision",
    4,
)

print(
    engine.get_settings()
)