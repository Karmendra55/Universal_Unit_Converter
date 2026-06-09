"""
Currency exchange page.

Provides live currency conversion,
exchange rate tracking and
multi-currency comparison.
"""

import customtkinter as ctk
import json

from src.converter.config import CURRENCY_ABBR_FILE
from src.converter.currency import CurrencyService

class CurrencyPage(ctk.CTkFrame):
    """
    Currency conversion dashboard.

    Allows users to convert between
    currencies, and compare exchange
    rates across major world currencies.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.currency_service = CurrencyService()
        self.currency_names = json.loads(
            CURRENCY_ABBR_FILE.read_text(
                encoding="utf-8"
            )
        )
        self.top_currencies = [
            "USD",
            "EUR",
            "GBP",
            "INR",
            "JPY",
            "AUD",
            "CAD",
            "CHF",
            "CNY",
            "SGD",
        ]

        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange all currency
        exchange interface components.
        """

        ctk.CTkLabel(
            self,
            text="Currency Exchange",
            font=("Arial", 30, "bold")
        ).pack(
            pady=(20, 0)
        )

        ctk.CTkLabel(
            self,
            text="Live exchange rates and multi-currency comparison",
            text_color=("gray40", "gray70")
        ).pack(
            pady=(0, 20)
        )

        self.currency_card = ctk.CTkFrame(self)

        self.currency_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # Amount

        ctk.CTkLabel(
            self.currency_card,
            text="Amount",
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.amount_entry = ctk.CTkEntry(
            self.currency_card,
            height=40
            )

        self.amount_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        ctk.CTkLabel(
            self.currency_card,
            text="Search Source Currency"
        ).pack(
            anchor="w",
            padx=20
        )

        self.search_entry = ctk.CTkEntry(
            self.currency_card,
            placeholder_text="Type currency name...",
            height=40
        )

        self.search_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_currency
        )

        self.amount_entry.bind(
            "<KeyRelease>",
            lambda event: self.convert_currency()
        )

        # From Currency

        currencies = [
            self.display_name(code)
            for code in sorted(
                self.currency_names.keys(),
                key=lambda code:
                self.currency_names[code]
            )
        ]

        self.from_var = ctk.StringVar(
            value=self.display_name("USD")
        )

        self.to_var = ctk.StringVar(
            value=self.display_name("INR")
        )

        ctk.CTkLabel(
            self.currency_card,
            text="From",
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.from_menu = ctk.CTkOptionMenu(
            self.currency_card,
            values=currencies,
            variable=self.from_var,
        )

        self.from_menu.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        button_frame = ctk.CTkFrame(
            self.currency_card,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=20,
            pady=15
        )

        ctk.CTkButton(
            button_frame,
            text="⇅ Swap",
            command=self.swap_currencies
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        # To Currency

        ctk.CTkLabel(
            self.currency_card,
            text="Search Target Currency"
        ).pack(
            anchor="w",
            padx=20
        )

        self.to_search_entry = ctk.CTkEntry(
            self.currency_card,
            placeholder_text="Search target currency...",
            height=40
        )

        self.to_search_entry.pack(
            fill="x",
            padx=20,
            pady=5,
        )

        self.to_search_entry.bind(
            "<KeyRelease>",
            self.search_to_currency
        )

        ctk.CTkLabel(
            self.currency_card,
            text="To",
        ).pack(anchor="w", padx=20, pady=(15, 5))

        self.to_menu = ctk.CTkOptionMenu(
            self.currency_card,
            values=currencies,
            variable=self.to_var,
        )

        self.to_menu.pack(
            fill="x",
            padx=20,
            pady=5,
        )


        ctk.CTkButton(
            button_frame,
            text="🔄 Refresh Rates",
            command=self.refresh_rates
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=5
        )

        self.from_menu.configure(
            command=lambda _: self.convert_currency()
        )

        self.to_menu.configure(
            command=lambda _: self.convert_currency()
        )

        # Result

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
            pady=(10, 5)
        )

        self.rate_label = ctk.CTkLabel(
            self.result_frame,
            text="",
            text_color=("gray40", "gray70")
        )

        self.rate_label.pack()

        self.updated_label = ctk.CTkLabel(
            self.result_frame,
            text=""
        )

        self.updated_label.pack(
            pady=(5, 15)
        )

        self.updated_label.configure(
            text=(
                f"Updated: "
                f"{self.currency_service.get_cache_age()}"
            )
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

        comparison_frame = ctk.CTkFrame(self)

        comparison_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        ctk.CTkLabel(
            comparison_frame,
            text="Top Currency Comparison",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 5)
        )

        self.multi_box = ctk.CTkTextbox(
            comparison_frame,
            height=180
        )

        self.multi_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        self.multi_box.configure(
            state="disabled"
        )

        self.updated_label.configure(
            text=(
                f"Updated: "
                f"{self.currency_service.get_cache_age()}"
            )
        )

        

    def convert_currency(self):
        """
        Convert the entered amount and update exchange rate displays.
        """
        try:

            if not self.amount_entry.get().strip():

                self.result_label.configure(
                    text="0"
                )

                self.rate_label.configure(
                    text=""
                )

                return

            from_code = self.extract_code(
                self.from_var.get()
            )

            to_code = self.extract_code(
                self.to_var.get()
            )

            amount = float(
                self.amount_entry.get()
            )

            result = self.currency_service.convert(
                amount,
                from_code,
                to_code,
            )

            self.result_label.configure(
                text=f"{result:,.4f} {to_code}",
                text_color=("black", "white")
            )

            rate = self.currency_service.convert(
                1,
                from_code,
                to_code,
            )

            self.rate_label.configure(
                text=(
                    f"1 {from_code} = "
                    f"{rate:.4f} {to_code}"
                )
            )

            self.updated_label.configure(
                text=(
                    "Cache Age: "
                    f"{self.currency_service.get_cache_age()}"
                )
            )

            self.multi_box.configure(
                state="normal"
            )

            self.multi_box.delete(
                "1.0",
                "end"
            )

            for code in self.top_currencies:

                if code == from_code:
                    continue

                try:

                    value = self.currency_service.convert(
                        amount,
                        from_code,
                        code,
                    )

                    self.multi_box.insert(
                        "end",
                        f"{self.display_name(code)}\n"
                        f"  → {value:,.2f}\n\n"
                    )

                except Exception:
                    pass

            self.multi_box.configure(
                state="disabled"
            )

        except Exception as error:

            self.result_label.configure(text=str(error), text_color="red")

    def swap_currencies(self):
        """
        Swap source and target currencies.
        """
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        self.from_var.set(to_value)
        self.to_var.set(from_value)

        if self.amount_entry.get():
            self.convert_currency()

    def display_name(self, code):
        """
        Return formatted currency display name.
        """
        return (
            f"{self.currency_names.get(code, code)} "
            f"({code})"
        )
    
    def extract_code(self, text):
        """
        Extract currency code from formatted display text.
        """
        return text.split("(")[-1].replace(")", "")
    
    def refresh_rates(self):
        """
        Force refresh exchange rates from the remote API.
        """
        try:

            self.currency_service.refresh_rates()

            self.status_label.configure(
                text="✓ Exchange rates refreshed",
                text_color="green"
            )

            self.updated_label.configure(
                text=(
                    "Cache Age: "
                    f"{self.currency_service.get_cache_age()}"
                )
            )

        except Exception as error:

            self.result_label.configure(
                text=str(error),
                text_color="red"
            )

    def search_currency(self, event=None):
        """
        Search and select source currency.
        """
        query = (
            self.search_entry.get()
            .strip()
            .lower()
        )

        if not query:
            return

        for code, name in self.currency_names.items():

            full_text = (
                f"{name} {code}"
            ).lower()

            if query in full_text:

                self.from_var.set(
                    self.display_name(code)
                )
                self.convert_currency()
                break

    def search_to_currency(self, event=None):
        """
        Search and select target currency.
        """

        query = (
            self.to_search_entry.get()
            .strip()
            .lower()
        )

        if not query:
            return

        for code, name in self.currency_names.items():

            full_text = (
                f"{name} {code}"
            ).lower()

            if query in full_text:

                self.to_var.set(
                    self.display_name(code)
                )
                self.convert_currency()
                break