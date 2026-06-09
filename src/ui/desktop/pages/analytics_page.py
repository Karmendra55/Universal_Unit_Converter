"""
Analytics dashboard page.

Displays usage statistics, favorites information,
and conversion insights gathered from user activity.
"""

import customtkinter as ctk

from src.converter.engine import ConversionEngine


class AnalyticsPage(ctk.CTkFrame):
    """
    Analytics dashboard for the application.

    Shows conversion statistics and usage trends
    in a card-based layout.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.engine = ConversionEngine()

        self.create_widgets()

    def create_widgets(self):
        """
        Build the analytics dashboard UI.
        """

        ctk.CTkLabel(
            self,
            text="Analytics Dashboard",
            font=("Arial", 30, "bold")
        ).pack(
            pady=(25, 10)
        )

        ctk.CTkLabel(
            self,
            text="Insights from your conversion activity",
            font=("Arial", 14)
        ).pack(
            pady=(0, 20)
        )

        dashboard = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        dashboard.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        stats = [
            (
                "Total Conversions",
                self.engine.get_total_conversions(),
                "All recorded conversions"
            ),
            (
                "Favorite Count",
                self.engine.get_favorite_count(),
                "Saved favorite conversions"
            ),
            (
                "Most Used Category",
                self.engine.get_most_used_category() or "N/A",
                "Most frequently used category"
            ),
            (
                "Most Used Conversion",
                self.engine.get_most_used_conversion() or "N/A",
                "Most frequently used conversion"
            ),
        ]

        for index, (title, value, subtitle) in enumerate(stats):

            row = index // 2
            column = index % 2

            card = ctk.CTkFrame(
                dashboard,
                corner_radius=12
            )

            card.grid(
                row=row,
                column=column,
                padx=15,
                pady=15,
                sticky="nsew"
            )

            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 16, "bold")
            ).pack(
                pady=(15, 5)
            )

            ctk.CTkLabel(
                card,
                text=str(value),
                font=("Arial", 28, "bold")
            ).pack(
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=subtitle,
                font=("Arial", 12)
            ).pack(
                pady=(0, 15)
            )

        dashboard.grid_columnconfigure(
            (0, 1),
            weight=1
        )

        dashboard.grid_rowconfigure(
            (0, 1),
            weight=1
        )