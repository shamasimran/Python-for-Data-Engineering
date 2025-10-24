from datetime import datetime

class DateCalculator:
    """Provides date calculation utilities."""

    @staticmethod
    def days_between(start_date, end_date):
        """Returns the number of days between two dates."""
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        return (end_date - start_date).days
