"""
Currency exchange service.

Provides live exchange rates,
currency conversion and local
rate caching functionality.
"""

import json
from datetime import datetime, timedelta

import requests

from .config import CURRENCY_CACHE_FILE
from .exceptions import CurrencyError

class CurrencyService:
    """
    Handles currency exchange rates,
    caching and currency conversion.
    """
    API_URL = (
        "https://open.er-api.com/v6/latest/USD"
    )

    def __init__(self):
        self.cache_file = CURRENCY_CACHE_FILE

    def _load_cache(self) -> dict | None:
        """
        Load cached exchange rate data.
        """
        if not self.cache_file.exists():
            return None

        with open(
            self.cache_file,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def _save_cache(self, data: dict) -> None:
        """
        Save exchange rate data to cache.
        """
        with open(
            self.cache_file,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
            )

    def convert(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
    ):

        # Fetch fresh rates from API
        rates = self.get_rates() 

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in rates:
            raise ValueError(
                f"Unsupported currency: "
                f"{from_currency}"
            )

        if to_currency not in rates:
            raise ValueError(
                f"Unsupported currency: "
                f"{to_currency}"
            )

        usd_amount = (
            amount / rates[from_currency]
        )

        return (
            usd_amount * rates[to_currency]
        )

    def get_rates(self):
        """
        Returns exchange rates.
        Uses cache when available.
        """

        cache = self._load_cache()

        if cache:

            timestamp = datetime.fromisoformat(
                cache["timestamp"]
            )

            age = datetime.now() - timestamp

            if age < timedelta(hours=12):
                return cache["rates"]
            
        try:

            response = requests.get(
                self.API_URL,
                timeout=10,
            )

            response.raise_for_status()

        except requests.RequestException as error:
            raise CurrencyError(
                "Unable to retrieve exchange rates."
            )

        data = response.json()

        rates = data["rates"]

        self._save_cache(
            {
                "timestamp":
                datetime.now().isoformat(),
                "rates": rates,
            }
        )

        return rates
    
    def get_last_updated(self) -> str:
        """
        Return the timestamp of the
        most recent cache update.
        """
        cache = self._load_cache()

        if not cache:
            return "Unknown"

        return cache["timestamp"]
    
    def refresh_rates(self):
        """
        Force refresh exchange rates.
        """

        response = requests.get(
            self.API_URL,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        rates = data["rates"]

        cache_data = {
            "timestamp": datetime.now().isoformat(),
            "rates": rates,
        }

        self._save_cache(cache_data)

        return rates
    
    def get_cache_age(self) -> str:
        """
        Return a human-readable cache age.
        """

        cache = self._load_cache()

        if not cache:
            return "Unknown"

        timestamp = datetime.fromisoformat(
            cache["timestamp"]
        )

        age = datetime.now() - timestamp

        hours = age.seconds // 3600

        minutes = (
            age.seconds % 3600
        ) // 60

        return f"{hours}h {minutes}m ago"