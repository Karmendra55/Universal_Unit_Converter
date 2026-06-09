"""
Settings page.

Allows users to customize
application appearance and
conversion preferences.
"""

import customtkinter as ctk

from src.converter.engine import ConversionEngine


class SettingsPage(ctk.CTkFrame):
    """
    Settings dashboard.

    Provides controls for application theme and
    conversion precision.
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.engine = ConversionEngine()

        self.create_widgets()

    def create_widgets(self):

        settings = self.engine.get_settings()

        ctk.CTkLabel(
            self,
            text="Settings",
            font=("Arial", 30, "bold")
        ).pack(
            pady=(20, 0)
        )

        ctk.CTkLabel(
            self,
            text="Customize application preferences",
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 20)
        )

        # Settings Card

        self.settings_card = ctk.CTkFrame(self)

        self.settings_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Card Heading

        ctk.CTkLabel(
            self.settings_card,
            text="Application Preferences",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        # Startup Page

        ctk.CTkLabel(
            self.settings_card,
            text="Default Startup Page",
            font=("Arial", 14, "bold")
        ).pack(
            anchor="w",
            padx=20
        )

        ctk.CTkLabel(
            self.settings_card,
            text="Choose which page opens when the application starts.",
            text_color=("gray40", "gray70")
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.start_page_menu = ctk.CTkOptionMenu(
            self.settings_card,
            values=[
                "Converter",
                "Currency",
                "Favorites",
                "History",
                "Analytics"
            ]
        )

        self.start_page_menu.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.start_page_menu.set(
            settings.get(
                "startup_page",
                "Converter"
            )
        )

        # Theme

        ctk.CTkLabel(
            self.settings_card,
            text="Theme",
            font=("Arial", 14, "bold")
        ).pack(
            anchor="w",
            padx=20
        )

        ctk.CTkLabel(
            self.settings_card,
            text="Choose light, dark, or follow the system theme.",
            text_color=("gray40", "gray70")
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.theme_menu = ctk.CTkOptionMenu(
            self.settings_card,
            values=["light", "dark", "system"]
        )

        self.theme_menu.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        # Precision

        ctk.CTkLabel(
            self.settings_card,
            text="Decimal Precision",
            font=("Arial", 14, "bold")
        ).pack(
            anchor="w",
            padx=20
        )

        ctk.CTkLabel(
            self.settings_card,
            text="Controls the number of decimal places displayed in results.",
            text_color=("gray40", "gray70")
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.precision_menu = ctk.CTkOptionMenu(
            self.settings_card,
            values=["2", "4", "6", "8"]
        )

        self.precision_menu.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        ctk.CTkButton(
            self.settings_card,
            text="Save Settings",
            command=self.save_settings
        ).pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        self.status_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.status_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

    def save_settings(self):
        """
        Save selected settings and
        immediately apply appearance
        changes to the application.
        """
        self.engine.update_setting(
            "precision",
            int(
                self.precision_menu.get()
            )
        )

        self.engine.update_setting(
            "theme",
            self.theme_menu.get()
        )

        ctk.set_appearance_mode(
            self.theme_menu.get()
        )

        self.status_label.configure(
            text="✓ Settings saved successfully",
            text_color="green"
        )