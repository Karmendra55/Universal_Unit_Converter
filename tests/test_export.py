from src.converter.export import ExportManager


def test_export_csv(tmp_path):

    exporter = ExportManager()

    path = tmp_path / "test.csv"

    exporter.export_history_csv(
        str(path)
    )

    assert path.exists()