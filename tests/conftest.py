from src.converter.engine import ConversionEngine

import pytest


@pytest.fixture
def engine():
    return ConversionEngine()