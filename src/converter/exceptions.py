"""
Custom exceptions used throughout the converter system.
"""


class ConversionError(Exception):
    """Base exception for all conversion-related errors."""
    pass


class InvalidCategoryError(ConversionError):
    """Raised when a category does not exist."""
    pass


class InvalidConversionError(ConversionError):
    """Raised when a conversion does not exist."""
    pass


class InvalidValueError(ConversionError):
    """Raised when the provided value is invalid."""
    pass

class CurrencyError(ConversionError):
    """Currency service error."""
    pass