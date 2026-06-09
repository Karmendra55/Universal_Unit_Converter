from src.converter.engine import ConversionEngine


def test_search_meter():
    engine = ConversionEngine()

    results = engine.search("meter")

    assert len(results) > 0