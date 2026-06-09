"""
Favorites manager.

Handles storage and management
of user favorite conversions.
"""
from pathlib import Path
import json

from .config import FAVORITES_FILE

class FavoritesManager:
    """
    Manage favorite conversions.
    """

    def __init__(self, file_path=None):
        """
        Initialize favorite storage.
        """
        self.file_path = (
            Path(file_path)
            if file_path
            else FAVORITES_FILE
        )

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def _load(self) -> list:
        """
        Load favorites from storage.
        """
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _save(self, data: list) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_favorites(self) -> list:
        """
        Return all saved favorites.
        """
        return self._load()

    def add_favorite(
        self,
        category: str,
        conversion: str,
    ) -> None:
        """
        Add a conversion to favorites.
        """
        favorites = self._load()
        
        # Favorite entry structure
        favorite = {
            "category": category,
            "conversion": conversion,
        }

        if favorite not in favorites:
            favorites.append(favorite)
            self._save(favorites)

    def remove_favorite(
        self,
        category: str,
        conversion: str,
    ) -> None:
        favorites = self._load()

        favorites = [
            item
            for item in favorites
            if not (
                item["category"] == category
                and item["conversion"] == conversion
            )
        ]

        self._save(favorites)

    def clear_favorites(self) -> None:
        """
        Remove all saved favorites.
        """

        self._save([])

    def is_favorite(
        self,
        category: str,
        conversion: str,
    ) -> bool:
        """
        Check whether a conversion
        is saved as a favorite.
        """
        favorites = self._load()

        return any(
            item["category"] == category
            and item["conversion"] == conversion
            for item in favorites
        )