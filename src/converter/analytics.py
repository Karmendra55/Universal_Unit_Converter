"""
Analytics utilities.

Provides statistics and insights
based on conversion history and
saved favorites.
"""

from collections import Counter

from .history import HistoryManager
from .favorites import FavoritesManager


class AnalyticsManager:
    """
    Analytics service.

    Calculates usage statistics from
    conversion history and favorites data.
    """

    def __init__(self):
        self.history_manager = HistoryManager()
        self.favorites_manager = FavoritesManager()

    def total_conversions(self) -> int:
        """
        Return the total no. of recorded conversions.
        """
        return len(
            self.history_manager.load_history()
        )

    def favorite_count(self) -> int:
        """
        Return total no. of saved favorites.
        """
        return len(
            self.favorites_manager.get_favorites()
        )

    def most_used_category(self) -> str | None:
        """
        Return the most frequently
        used conversion category.
        """

        history = self.history_manager.load_history()

        if not history:
            return None

        counter = Counter(
            record.category
            for record in history
        )

        return counter.most_common(1)[0][0]

    def most_used_conversion(self) -> str | None:
        """
        Return the most frequently
        used conversion type.
        """

        history = self.history_manager.load_history()

        if not history:
            return None

        counter = Counter(
            record.conversion
            for record in history
        )

        return counter.most_common(1)[0][0]