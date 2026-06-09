from src.converter.conversions import CONVERSIONS


def test_length_exists():
    assert "Length" in CONVERSIONS


def test_weight_exists():
    assert "Weight" in CONVERSIONS


def test_temperature_exists():
    assert "Temperature" in CONVERSIONS