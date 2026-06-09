"""
Search functionality for categories and conversions.
"""

from .conversions import CONVERSIONS


class SearchManager:
    """
    Handles searching categories and conversions.
    """

    @staticmethod
    def search(query: str) -> list[dict]:
        """
        Search through categories and conversions.

        Parameters
        ----------
        query : str

        Returns
        -------
        list[dict]
        """

        query = query.strip().lower()

        if not query:
            return []

        results = []

        for category, conversions in CONVERSIONS.items():

            if query in category.lower():
                results.append(
                    {
                        "type": "category",
                        "category": category,
                    }
                )

            for conversion in conversions:

                if query in conversion.lower():
                    results.append(
                        {
                            "type": "conversion",
                            "category": category,
                            "conversion": conversion,
                        }
                    )

        return results