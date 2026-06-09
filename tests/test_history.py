from src.converter.history import HistoryManager
from src.converter.models import ConversionRecord

from datetime import datetime


def test_save_record(tmp_path):

    manager = HistoryManager()

    manager.file_path = (
        tmp_path / "history.json"
    )

    record = ConversionRecord(
        category="Length",
        conversion="Km to Miles",
        input_value=10,
        result=6.21371,
        timestamp=datetime.now(),
    )

    manager.save_record(record)

    history = manager.load_history()

    assert len(history) == 1