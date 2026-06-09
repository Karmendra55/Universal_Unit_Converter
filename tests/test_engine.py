from src.converter.engine import ConversionEngine

def test_km_to_miles():
    engine = ConversionEngine()

    engine.update_setting(
        "precision",
        6
    )

    result = engine.convert(
        "Length",
        "Km to Miles",
        10,
        save_history=False,
    )

    assert result == 6.21371

def test_celsius_to_fahrenheit(engine):
    result = engine.convert(
        "Temperature",
        "Celsius to Fahrenheit",
        100,
        save_history=False,
    )

    assert result == 212