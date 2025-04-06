from datetime import datetime

def convert_date_format(date_str, from_format, to_format):
    return datetime.strptime(date_str, from_format).strftime(to_format)

if __name__ == "__main__":
    print(convert_date_format("2025-04-06", "%Y-%m-%d", "%d/%m/%Y"))
