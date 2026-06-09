"""
Conversion engine.

Coordinates conversions, history,
favorites, analytics and settings
for the application.
"""

from datetime import datetime

from .conversions import CONVERSIONS
from .exceptions import (InvalidCategoryError, InvalidConversionError, InvalidValueError)
from .history import HistoryManager
from .models import ConversionRecord
from .favorites import FavoritesManager
from .utils import format_result
from .search import SearchManager
from .analytics import AnalyticsManager
from .settings import SettingsManager

class ConversionEngine:
    """
    Main conversion engine used by all interfaces.
    """

    def __init__(self):
        """
        Initialize application services.
        """
        self.history = HistoryManager()
        self.favorites = FavoritesManager()
        self.search_manager = SearchManager()
        self.analytics = AnalyticsManager()
        self.settings = SettingsManager()

    @staticmethod
    def get_categories() -> list[str]:
        """
        Return all available categories.
        """
        return sorted(CONVERSIONS.keys())

    @staticmethod
    def get_conversions(category: str) -> list[str]:
        """
        Return available conversions in a category.
        """

        if category not in CONVERSIONS:
            raise InvalidCategoryError(
                f"Unknown category: {category}"
            )

        return sorted(CONVERSIONS[category].keys())
    
    def add_favorite(self, category: str, conversion_name: str) -> None:
        """
        Save a conversion as fav.
        """
        self.favorites.add_favorite(
            category,
            conversion_name,
        )

    def remove_favorite(self, category: str, conversion_name: str) -> None:
        self.favorites.remove_favorite(
            category,
            conversion_name,
        )

    def get_favorites(self) -> list:
        """
        Return all saved favs.
        """
        return self.favorites.get_favorites()

    def search(self, query: str):
        """
        Search categories and conversions.
        """
        return self.search_manager.search(query)
    
    def get_total_conversions(self) -> int:
        """
        Return total conversion count.
        """
        return self.analytics.total_conversions()
    
    def get_favorite_count(self):
        """
        Return the Favorite count.
        """
        return self.analytics.favorite_count()
    
    def get_most_used_category(self):
        """
        Return the most used category
        """
        return self.analytics.most_used_category()
    
    def get_most_used_conversion(self):
        """
        Return the most user conversion
        """
        return self.analytics.most_used_conversion()
    
    def get_settings(self) -> dict :
        """
        Return application settings.
        """
        return self.settings.load_settings()
    
    def update_setting(self, key:str, value) -> None:
        """
        For Updating a setting value.
        """
        self.settings.update_setting(key, value)

    def convert(
        self,
        category: str,
        conversion_name: str,
        value: float,
        save_history: bool = True,
    ) -> float:
        """
        Perform conversion and optionally save it.
        """

        if category not in CONVERSIONS:
            raise InvalidCategoryError(
                f"Unknown category: {category}"
            )

        if conversion_name not in CONVERSIONS[category]:
            raise InvalidConversionError(
                f"Unknown conversion: {conversion_name}"
            )

        try:
            value = float(value)
        except (TypeError, ValueError):
            raise InvalidValueError(
                "Value must be numeric."
            )

        precision = self.settings.get_setting(
            "precision"
        )
        result = format_result(
            CONVERSIONS[category][conversion_name](value),
            precision=precision,
        )

        # Record successful conversion
        if save_history:
            record = ConversionRecord(
                category=category,
                conversion=conversion_name,
                input_value=value,
                result=result,
                timestamp=datetime.now(),
            )

            self.history.save_record(record)

        return result