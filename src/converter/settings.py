import json

from .config import SETTINGS_FILE


DEFAULT_SETTINGS = {
    "precision": 6,
    "theme": "system",
    "startup_page": "Converter",
    "save_history": True,
    "auto_copy_result": False,
    "currency_cache_hours": 12,
}


class SettingsManager:
    """
    Handles application settings.
    """

    def __init__(self):
        self.settings_file = SETTINGS_FILE

        if not self.settings_file.exists():
            self.save_settings(DEFAULT_SETTINGS)

    def load_settings(self) -> dict:
        with open(
            self.settings_file,
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    def save_settings(
        self,
        settings: dict,
    ) -> None:
        with open(
            self.settings_file,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                settings,
                file,
                indent=4,
            )

    def get_setting(
        self,
        key: str,
    ):
        settings = self.load_settings()

        return settings.get(key)

    def update_setting(
        self,
        key: str,
        value,
    ) -> None:
        settings = self.load_settings()

        settings[key] = value

        self.save_settings(settings)