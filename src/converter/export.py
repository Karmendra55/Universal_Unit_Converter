"""
Export manager.

Provides functionality for exporting
application data to external formats.
"""

import csv
from pathlib import Path
from datetime import datetime

from .history import HistoryManager
from .config import EXPORT_DIR

class ExportManager:
    """
    Handles exporting conversion
    history and application data.
    """
    def __init__(self):
        """
        Initialize export dependencies.
        """
        self.history_manager = HistoryManager()

    def export_history_csv(
        self,
        file_path: str | None = None,
    ) -> str:
        """
        Export conversion history to CSV.

        Returns the exported file path.
        """

        # Generate export file path
        if file_path is None:
            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S_%f"
            )

            file_path = (
                EXPORT_DIR /
                f"history_{timestamp}.csv"
            )

        export_path = Path(file_path)

        export_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        
        # Load history records
        records = self.history_manager.load_history()

        with open(
            export_path,
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(
                [
                    "Category",
                    "Conversion",
                    "Input Value",
                    "Result",
                    "Timestamp",
                ]
            )

            for record in records:
                writer.writerow(
                    [
                        record.category,
                        record.conversion,
                        record.input_value,
                        record.result,
                        record.timestamp.isoformat(),
                    ]
                )

        return str(export_path)