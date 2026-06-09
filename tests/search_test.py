import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.engine import ConversionEngine

engine = ConversionEngine()

results = engine.search("meter")

for result in results:
    print(result)