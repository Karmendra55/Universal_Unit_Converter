"""
Desktop application entry point.

Creates the main application window,
navigation sidebar and page routing
for all converter modules.
"""

import customtkinter as ctk

from .pages.converter_page import ConverterPage
from .pages.history_page import HistoryPage
from .pages.favorites_page import FavoritesPage
from .pages.analytics_page import AnalyticsPage
from .pages.settings_page import SettingsPage
from .pages.currency_page import CurrencyPage
from src.converter.settings import SettingsManager

class UniversalUnitConverterApp(ctk.CTk):
    """
    Main desktop application window.

    Responsible for application layout,
    sidebar navigation, page switching
    and startup configuration.
    """

    def __init__(self):
        super().__init__()

        self.title("Universal Unit Converter")

        self.geometry("1280x900")
        self.minsize(1100, 800)

        try:
            self.iconbitmap("assets/icon.ico")
        except Exception:
            pass

        self.settings_manager = SettingsManager()
        ctk.set_default_color_theme("blue")

        settings = self.settings_manager.load_settings()

        ctk.set_appearance_mode(
            settings.get("theme", "system")
        )

        self.create_layout()

        self.pages = {
            "Converter": ConverterPage,
            "Currency": CurrencyPage,
            "Favorites": FavoritesPage,
            "History": HistoryPage,
            "Analytics": AnalyticsPage,
            "Settings": SettingsPage,
        }

    def create_layout(self):
        """
        Create the main application layout
        consisting of sidebar navigation
        and content display areas.
        """
        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.content_frame = ctk.CTkFrame(
            self
        )

        self.content_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.create_sidebar()

    def create_sidebar(self):
        """
        Build the navigation sidebar and
        page selection controls.
        """
        ctk.CTkLabel(
            self.sidebar,
            text="UUC",
            font=("Arial", 34, "bold")
        ).pack(
            pady=(25, 5)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Universal Unit Converter",
            font=("Arial", 13),
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 25)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Navigation",
            font=("Arial", 13, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 10)
        )

        pages = [
            ("🔄 Converter", ConverterPage),
            ("💱 Currency", CurrencyPage),
            ("⭐ Favorites", FavoritesPage),
            ("📜 History", HistoryPage),
            ("📊 Analytics", AnalyticsPage),
            ("⚙ Settings", SettingsPage),
        ]

        for text, command in pages:

            ctk.CTkButton(
                self.sidebar,
                text=text,
                command=command,
            ).pack(
                fill="x",
                padx=10,
                pady=5,
            )

        for text, page_class in pages:

            ctk.CTkButton(
                self.sidebar,
                text=text,
                command=lambda p=page_class:
                    self.show_page(p)
            ).pack(
                fill="x",
                padx=12,
                pady=4
            )

        ctk.CTkLabel(
            self.sidebar,
            text="",
        ).pack(
            expand=True,
            fill="both"
        )

        # Footer

        ctk.CTkLabel(
            self.sidebar,
            text="Made by\nKarmendra B. Srivastava",
            font=("Arial", 12),
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 15)
        )

    def clear_content(self):
        """
        Remove all widgets currently
        displayed in the content area.
        """
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_converter(self):
        self.clear_content()
        ConverterPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True,
        )

    def show_history(self):
        self.clear_content()
        HistoryPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True,
        )

    def show_favorites(self):
        self.clear_content()
        FavoritesPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True,
        )

    def show_analytics(self):
        self.clear_content()
        AnalyticsPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True,
        )

    def show_settings(self):
        self.clear_content()
        SettingsPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True,
        )

    def show_currency(self):
        self.clear_content()
        CurrencyPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True,
        )

    def show_page(self, page_class):
        """
        Clear the content area and
        display the selected page.
        """

        self.clear_content()

        page_class(
            self.content_frame
        ).pack(
            fill="both",
            expand=True
        )

        startup_page = (
            self.settings_manager
            .load_settings()
            .get("startup_page", "Converter")
        )

        self.show_page(
            self.pages[startup_page]
        )

    def create_layout(self):
        """
        Create the main application layout
        consisting of sidebar navigation
        and content display areas.
        """
        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0,
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.content_frame = ctk.CTkFrame(
            self
        )

        self.content_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.create_sidebar()

    def create_sidebar(self):
        """
        Build the navigation sidebar and
        page selection controls.
        """
        ctk.CTkLabel(
            self.sidebar,
            text="UUC",
            font=("Arial", 34, "bold")
        ).pack(
            pady=(25, 5)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Universal Unit Converter",
            font=("Arial", 13),
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 25)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Navigation",
            font=("Arial", 13, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(10, 10)
        )

        ctk.CTkLabel(
            self.sidebar,
            text="Universal Unit\nConverter",
            font=("Arial", 20, "bold"),
        ).pack(
            pady=20
        )

        pages = [
            ("🔄 Converter", ConverterPage),
            ("💱 Currency", CurrencyPage),
            ("⭐ Favorites", FavoritesPage),
            ("📜 History", HistoryPage),
            ("📊 Analytics", AnalyticsPage),
            ("⚙ Settings", SettingsPage),
        ]

        for text, page_class in pages:
            ctk.CTkButton(
                self.sidebar,
                text=text,
                command=lambda p=page_class:
                    self.show_page(p)
            ).pack(
                fill="x",
                padx=12,
                pady=4
            )

        ctk.CTkLabel(
            self.sidebar,
            text="",
        ).pack(
            expand=True,
            fill="both"
        )

        # Footer

        ctk.CTkLabel(
            self.sidebar,
            text="Made by\nKarmendra B. Srivastava",
            font=("Arial", 12),
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 15)
        )

    def clear_content(self):
        """
        Remove all widgets currently
        displayed in the content area.
        """
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_page(self, page_class):
        """
        Clear the content area and
        display the selected page.
        """

        self.clear_content()

        page_class(
            self.content_frame
        ).pack(
            fill="both",
            expand=True
        )
