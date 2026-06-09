from src.converter.favorites import FavoritesManager

def test_add_favorite():
    manager = FavoritesManager()

    manager.add_favorite(
        "Length",
        "Km to Miles"
    )

    favorites = manager.get_favorites()

    assert len(favorites) >= 1