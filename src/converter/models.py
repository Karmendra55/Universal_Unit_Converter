"""
Application data models.

Contains structured data objects
used throughout the converter.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class ConversionRecord:
    """
    Represents a single conversion performed by the user.
    """
    category: str
    conversion: str
    input_value: float
    result: float
    timestamp: datetime