"""
Shared utility functions.
"""
def format_result(
    value: float,
    precision: int = 6,
) -> float:
    """
    Format a conversion result using
    the configured decimal precision.

    Parameters
    ----------
    value : float
        Result value to format.

    precision : int
        Number of decimal places.

    Returns
    -------
    float
        Rounded value.
    """

    return round(
        value,
        precision
    )