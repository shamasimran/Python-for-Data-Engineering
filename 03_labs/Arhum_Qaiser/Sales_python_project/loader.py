import pyodbc
from logger_config import setup_logger
from config import config_dba

class loader:
    def __init__(self):
        self.logger = setup_logger()

    def connect(self):
        try:
            conn_str = (
                f"DRIVER={{{config_dba['driver']}}};"
                f"SERVER={config_dba['server']};"
                f"DATABASE={config_dba['database']};"
                "Trusted_Connection=yes;"
            )
            conn = pyodbc.connect(conn_str)
            self.logger.info("Successfully connected to the database using Windows Authentication.")
            return conn
        except Exception as e:
            self.logger.error(f"Database connection failed: {e}")
            return None

    def create_and_insert(self, conn, records):
        create_table_query = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Sales')
        CREATE TABLE Sales (
            ReportID varchar(50),
            SalesPersonID varchar(50),
            ProductID varchar(50),
            Quantity varchar(50),
            TotalSalesValue FLOAT
        )
        """
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            conn.commit()
            self.logger.info("SalesData table is ready.")
        except Exception as e:
            self.logger.error(f"Failed to create table: {e}")

        inserted = 0
        for r in records:
            try:
                cursor.execute(
                    """
                    INSERT INTO Sales (ReportID, SalesPersonID, ProductID, Quantity, TotalSalesValue)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    r["ReportID"], r["SalesPersonID"], r["ProductID"], r["Quantity"], r["TotalSalesValue"]
                )
                inserted += 1
            except Exception as e:
                self.logger.error(f"Failed to insert record {r}: {e}")

        conn.commit()
        cursor.close()
        self.logger.info(f"Inserted {inserted} records into SalesData table.")
