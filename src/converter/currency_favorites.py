"""
Currency favorites manager.

Handles storage and retrieval of
favorite currency conversion pairs.
"""

import json

from .config import (
    CURRENCY_FAVORITES_FILE
)

class CurrencyFavoritesManager:
    """
    Manages favorite currency pairs
    saved by the user.
    """
    def __init__(self):
        """
        Initialize favorites storage.
        """
        self.file_path = (
            CURRENCY_FAVORITES_FILE
        )

        if not self.file_path.exists():

            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump([], file)

    def load(self):
        """
        Load saved currency pairs
        """
        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(self, data):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def add_pair(self, from_currency, to_currency):
        """
        Add a fav currency pair
        """
        pairs = self.load()

        pair = {
            "from": from_currency,
            "to": to_currency
        }

        if pair not in pairs:

            pairs.append(pair)

            self.save(pairs)

    def remove_pair(self, from_currency, to_currency):
        """
        Remove a fav currency pair
        """
        pairs = self.load()

        pairs = [
            pair
            for pair in pairs
            if not (
                pair["from"]
                == from_currency
                and
                pair["to"]
                == to_currency
            )
        ]

        self.save(pairs)

    def get_pairs(self):
        return self.load()