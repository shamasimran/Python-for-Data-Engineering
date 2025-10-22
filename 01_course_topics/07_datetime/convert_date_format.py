from datetime import datetime, date, time, timedelta

# Common Format Codes:
# Code	Meaning	            Example
# %Y	Year (4 digits)	    2025
# %m	Month (01–12)	    10
# %d	Day (01–31)	        21
# %H	Hour (00–23)	    14
# %M	Minute (00–59)	    45
# %S	Second (00–59)	    12
# %A	Weekday name	    Tuesday
# %B	Month name	        October

def print_current_datetime():
    now = datetime.now()
    print("Current Date and Time:", now)
    
def print_current_time():
    today = date.today()
    print("Today's Date:", today)
    current_time = datetime.now().time()
    print("Current Time:", current_time)    

def print_specific_datetime():
    custom_date = date(2025, 12, 31)
    print("Custom Date:", custom_date)
    custom_datetime = datetime(2025, 12, 31, 23, 59, 59)
    print("Custom DateTime:", custom_datetime)

# convert_date_format("2025-04-06", "%Y-%m-%d", "%d/%m/%Y")
def convert_date_format(date_str, from_format, to_format):
    return datetime.strptime(date_str, from_format).strftime(to_format)


def convert_string_to_datetime():
    date_string = "2025-10-21 14:30:00"
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print("Parsed DateTime:", parsed_date)


def date_arithmetic():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    next_week = today + timedelta(weeks=1)
    print("Yesterday:", yesterday)
    print("Next Week:", next_week)
    
def compare_dates():
    date1 = datetime(2025, 10, 21)
    date2 = datetime(2025, 12, 25)
    print("Is date1 before date2?", date1 < date2)
    print("Is date1 after date2?", date1 > date2)
 
def date_with_timezone():
    from datetime import timezone
    utc_now = datetime.now(timezone.utc)
    print("Current UTC DateTime:", utc_now)
           

if __name__ == "__main__":
    print(convert_date_format("2025-04-06", "%Y-%m-%d", "%d/%m/%Y"))
