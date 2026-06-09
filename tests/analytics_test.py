import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.engine import ConversionEngine

engine = ConversionEngine()

print(
    "Total:",
    engine.get_total_conversions()
)

print(
    "Favorites:",
    engine.get_favorite_count()
)

print(
    "Category:",
    engine.get_most_used_category()
)

print(
    "Conversion:",
    engine.get_most_used_conversion()
)