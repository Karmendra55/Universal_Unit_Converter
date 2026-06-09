"""
History manager.

Handles storage and retrieval
of conversion history records.
"""
import json
from datetime import datetime

from .models import ConversionRecord
from .config import HISTORY_FILE

class HistoryManager:
    """
    Handles storage and retrieval of conversion history.
    """

    def __init__(self):
        """
        Initialize history storage.
        """
        self.file_path = HISTORY_FILE

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_record(self, record: ConversionRecord) -> None:
        """
        Save a conversion record to history.
        """
        history = self.load_raw()

        # Store serialized record
        history.append(
            {
                "category": record.category,
                "conversion": record.conversion,
                "input_value": record.input_value,
                "result": record.result,
                "timestamp": record.timestamp.isoformat(),
            }
        )

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def load_raw(self) -> list:
        """
        Load raw history data
        from the storage file.
        """
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_history(self) -> list[ConversionRecord]:
        records = []

        # Convert stored dict into instances
        for item in self.load_raw():
            records.append(
                ConversionRecord(
                    category=item["category"],
                    conversion=item["conversion"],
                    input_value=item["input_value"],
                    result=item["result"],
                    timestamp=datetime.fromisoformat(
                        item["timestamp"]
                    ),
                )
            )

        return records
    
    def clear_history(self) -> None:
        """
        Remove all stored history records.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump([], file)