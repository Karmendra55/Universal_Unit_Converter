"""
Converter dashboard page.

Used for conversion of the majorly known units,
and conversion them including saving, favorites and exporting.
"""

import customtkinter as ctk
import pyperclip

from src.converter.engine import ConversionEngine
from src.converter.exceptions import ConversionError
from src.converter.export import ExportManager

class ConverterPage(ctk.CTkFrame):
    """
    Main unit conversion page.

    Provides unit conversion, search,
    favorites management, export tools,
    and recent conversion history.
    """
    def __init__(self, parent):
        """
        Initialize converter page and load
        required conversion services.
        """
        super().__init__(parent)

        self.engine = ConversionEngine()
        self.export_manager = ExportManager()

        self.category_var = ctk.StringVar()
        self.conversion_var = ctk.StringVar()

        self.create_widgets()
        
        self.load_recent()

    def create_widgets(self):
        """
        Update available conversions when
        the selected category changes.
        """
        # Header

        ctk.CTkLabel(
            self,
            text="Unit Converter",
            font=("Arial", 30, "bold")
        ).pack(pady=(20, 0))

        ctk.CTkLabel(
            self,
            text="Convert between 100+ measurement units",
            text_color=("gray40", "gray70")
        ).pack(pady=(0, 20))

        # Converter Card

        self.converter_card = ctk.CTkFrame(self)

        self.converter_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Search

        self.search_entry = ctk.CTkEntry(
            self.converter_card,
            height=40,
            placeholder_text="Search conversion..."
        )

        self.search_entry.pack(
            fill="x",
            padx=20,
            pady=(20, 10)
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_conversion
        )

        # Category

        ctk.CTkLabel(
            self.converter_card,
            text="Category"
        ).pack(anchor="w", padx=20)

        self.category_menu = ctk.CTkOptionMenu(
            self.converter_card,
            values=self.engine.get_categories(),
            variable=self.category_var,
            command=self.update_conversions
        )

        self.category_menu.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Conversion

        ctk.CTkLabel(
            self.converter_card,
            text="Conversion"
        ).pack(anchor="w", padx=20)

        self.conversion_menu = ctk.CTkOptionMenu(
            self.converter_card,
            values=["Select Category First"],
            variable=self.conversion_var,
            command=lambda _: self.convert()
        )

        self.conversion_menu.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Value

        ctk.CTkLabel(
            self.converter_card,
            text="Value"
        ).pack(anchor="w", padx=20)

        self.value_entry = ctk.CTkEntry(
            self.converter_card,
            height=40
        )

        self.value_entry.pack(
            fill="x",
            padx=20,
            pady=5
        )

        self.value_entry.bind(
            "<KeyRelease>",
            lambda event: self.convert()
        )

        # Buttons

        button_frame = ctk.CTkFrame(
            self.converter_card,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=15
        )


        ctk.CTkButton(
            button_frame,
            text="Copy Result",
            command=self.copy_result
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="Add Favorite",
            command=self.add_favorite
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="Export History",
            command=self.export_history
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # Result Card

        self.result_frame = ctk.CTkFrame(self)

        self.result_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            self.result_frame,
            text="Conversion Result",
            font=("Arial", 16, "bold")
        ).pack(
            pady=(15, 5)
        )

        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="0",
            font=("Arial", 36, "bold")
        )

        self.result_label.pack(
            pady=15
        )

        # Status Message

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            text_color="green"
        )

        self.status_label.pack(
            pady=(0, 10)
        )

        # Recent Conversions

        ctk.CTkLabel(
            self,
            text="Recent Conversions",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=20
        )

        self.recent_box = ctk.CTkTextbox(
            self,
            height=150
        )

        self.recent_box.pack(
            fill="x",
            padx=20,
            pady=10
        )

        categories = self.engine.get_categories()

        if categories:
            self.category_var.set(categories[0])
            self.update_conversions(categories[0])

    def update_conversions(self, category):

        conversions = self.engine.get_conversions(
            category
        )

        self.conversion_menu.configure(
            values=conversions
        )

        self.conversion_var.set(
            conversions[0]
        )

        self.convert()

    def convert(self):
        """
        Perform unit conversion and update
        the result display.
        """

        try:

            value_text = self.value_entry.get().strip()

            if not value_text:
                self.result_label.configure(text="0")
                return

            value = float(value_text)

            result = self.engine.convert(
                category=self.category_var.get(),
                conversion_name=self.conversion_var.get(),
                value=value
            )

            self.result_label.configure(
                text=f"{result:,.4f}"
            )

            self.load_recent()

        except (
            ValueError,
            ConversionError
        ) as error:

            self.result_label.configure(
                text=str(error)
            )

    def add_favorite(self):
        """
        Add or remove the selected conversion
        from favorites.
        """

        category = self.category_var.get()
        conversion = self.conversion_var.get()

        if self.engine.favorites.is_favorite(
            category,
            conversion
        ):

            self.engine.remove_favorite(
                category,
                conversion
            )

            self.status_label.configure(
                text="Removed from favorites",
                text_color="orange"
            )

        else:

            self.engine.add_favorite(
                category,
                conversion
            )

            self.status_label.configure(
                text="Added to favorites",
                text_color="green"
            )

    def copy_result(self):
        """
        Copy the current conversion result
        to the clipboard.
        """

        result = self.result_label.cget("text")

        if result and result != "0":

            pyperclip.copy(result)

            self.status_label.configure(
                text="✓ Result copied to clipboard",
                text_color="green"
            )

    def load_recent(self):
        """
        Load the most recent conversions
        into the history panel.
        """
        self.recent_box.configure(
            state="normal"
        )

        self.recent_box.delete(
            "1.0",
            "end"
        )

        records = (
            self.engine
            .history
            .load_history()
        )

        for record in reversed(records[-8:]):

            self.recent_box.insert(
                "end",
                f"{record.conversion}\n "
                f"{record.input_value} → "
                f"{record.result}\n\n"
            )

        self.recent_box.configure(
            state="disabled"
        )

    def search_conversion(self, event=None):
        """
        Search available conversions and
        automatically select the best match.
        """

        query = self.search_entry.get()

        if not query:
            return

        results = self.engine.search(query)

        if not results:
            return

        first = results[0]

        self.category_var.set(
            first["category"]
        )

        self.update_conversions(
            first["category"]
        )

        if first["type"] == "conversion":

            self.conversion_var.set(
                first["conversion"]
            )

    def export_history(self):
        """
        Export conversion history to a CSV file.
        """

        path = self.export_manager.export_history_csv()

        self.status_label.configure(
            text=f"History exported to {path}",
            text_color="green"
        )

        self.load_recent()