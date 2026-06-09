import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.converter.export import ExportManager

exporter = ExportManager()

file_path = exporter.export_history_csv()

print(f"Exported: {file_path}")