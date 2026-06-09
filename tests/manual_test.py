import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.engine import ConversionEngine

engine = ConversionEngine()

result = engine.convert(
    category="Length",
    conversion_name="Km to Miles",
    value=10,
)

print(result)

print(engine.get_categories())

print(
    engine.get_conversions("Temperature")
)