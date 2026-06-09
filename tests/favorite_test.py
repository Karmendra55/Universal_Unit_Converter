import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.engine import ConversionEngine

engine = ConversionEngine()

engine.add_favorite(
    "Length",
    "Km to Miles",
)

engine.add_favorite(
    "Temperature",
    "Celsius to Fahrenheit",
)

print(engine.get_favorites())