from datetime import datetime

def format_date(date_obj, format="%Y-%m-%d"):
    """Formats a datetime object into a string."""
    return date_obj.strftime(format)
