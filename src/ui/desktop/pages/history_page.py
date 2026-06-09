"""
History page.

Displays previously performed
conversions with timestamps for
quick reference and tracking.
"""

import customtkinter as ctk

from src.converter.history import HistoryManager


class HistoryPage(ctk.CTkFrame):
    """
    History dashboard.

    Shows recently completed
    conversions along with their
    timestamps and details.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.history_manager = HistoryManager()

        self.create_widgets()
        self.load_history()

    def create_widgets(self):
        """
        Create and arrange all history
        interface components.
        """

        ctk.CTkLabel(
            self,
            text="Conversion History",
            font=("Arial", 30, "bold")
        ).pack(
            pady=(20, 0)
        )

        ctk.CTkLabel(
            self,
            text="View your recent conversion activity",
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 20)
        )

        self.history_card = ctk.CTkFrame(self)

        self.history_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            self.history_card,
            text="Recent Conversions",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        self.history_box = ctk.CTkTextbox(
            self.history_card,
            height=400
        )

        self.history_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.history_box.configure(
            state="disabled"
        )

        self.status_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.record_count_label = ctk.CTkLabel(
            self,
            text=""
        )

        self.record_count_label.pack(
            anchor="w",
            padx=20
        )

        self.status_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        ctk.CTkButton(
            self.history_card,
            text="Refresh History",
            command=self.load_history
        ).pack(
            padx=15,
            pady=(0, 15)
        )

    def load_history(self):
        """
        Load conversion history records
        and display them in the history panel.
        """
        self.history_box.configure(
            state="normal"
        )
        
        self.history_box.delete(
            "1.0",
            "end"
        )

        records = self.history_manager.load_history()

        self.record_count_label.configure(
            text=f"Total Records: {len(records)}"
        )

        if not records:

            self.history_box.insert(
                "end",
                "No conversion history available yet."
            )

            self.record_count_label.configure(
                text="Total Records: 0"
            )

            self.status_label.configure(
                text="No history records found",
                text_color="orange"
            )

            self.history_box.configure(
                state="disabled"
            )

            return

        for record in reversed(records):

            self.history_box.insert(
                "end",
                f"🕒 {record.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Category: {record.category}\n"
                f"Conversion: {record.conversion}\n"
                f"Value: {record.input_value} → {record.result}\n\n"
            )

        self.history_box.configure(
            state="disabled"
        )

        self.status_label.configure(
            text=f"✓ Loaded {len(records)} records",
            text_color="green"
        )