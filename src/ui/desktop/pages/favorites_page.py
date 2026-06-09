"""
Favorites page.

Displays saved favorite conversions
for quick access and management.
"""

import customtkinter as ctk

from src.converter.engine import ConversionEngine


class FavoritesPage(ctk.CTkFrame):
    """
    Favorites dashboard.

    Shows all saved favorite
    conversions and allows users
    to refresh the favorites list.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.engine = ConversionEngine()

        self.create_widgets()
        self.load_favorites()

    def create_widgets(self):

        ctk.CTkLabel(
            self,
            text="Favorites",
            font=("Arial", 30, "bold")
        ).pack(
            pady=(20, 0)
        )

        ctk.CTkLabel(
            self,
            text="Manage your saved unit conversions",
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 20)
        )

        self.favorites_card = ctk.CTkFrame(self)

        self.favorites_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            self.favorites_card,
            text="Saved Favorites",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            self.favorites_card,
            text="Quick access to your saved conversions",
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 20)
        )

        self.favorites_box = ctk.CTkTextbox(
            self.favorites_card,
            height=400
        )

        self.favorites_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.favorites_box.configure(
            state="disabled"
        )

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            text_color="green"
        )

        self.status_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkButton(
            self.favorites_card,
            text="Refresh Favorites",
            command=self.load_favorites
        ).pack(
            padx=15,
            pady=(0, 15)
        )

    def load_favorites(self):
        """
        Load saved favorites and display
        them inside the favorites panel.
        """
        self.favorites_box.configure(
            state="normal"
        )

        self.favorites_box.delete(
            "1.0",
            "end"
        )

        favorites = self.engine.get_favorites()

        if not favorites:

            self.favorites_box.insert(
                "end",
                "No favorites conversions saved yet."
            )

            self.favorites_box.configure(
            state="disabled"
            )
            
            return

        for item in favorites:

            self.favorites_box.insert(
                "end",
                f"📌 {item['category']} | "
                f"    {item['conversion']}\n"
            )

        self.favorites_box.configure(
            state="disabled"
        )

        self.status_label.configure(
            text="✓ Favorites loaded",
            text_color="green"
        )