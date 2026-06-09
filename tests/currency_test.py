import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.currency import CurrencyService

service = CurrencyService()

result = service.convert(
    amount=100,
    from_currency="USD",
    to_currency="INR",
)

print(result)