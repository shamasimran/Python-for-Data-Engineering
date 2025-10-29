import pyodbc

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        "SERVER=ARHUM-PC\SQLEXPRESS;" 
        "trusted_connection=yes;"
    )
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")