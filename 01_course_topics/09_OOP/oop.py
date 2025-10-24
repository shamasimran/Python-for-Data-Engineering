"""
Topic 09: Object-Oriented Programming (OOP)
--------------------------------------------
This example shows how OOP principles — inheritance, polymorphism, 
encapsulation, and abstraction — are used in a Data Engineering context.

We’ll simulate an ETL (Extract, Transform, Load) pipeline:
- A base class (ETLJob) defines the workflow and common behavior.
- Child classes (CSVToDBETL, APIToJSONETL) inherit and customize that logic.
"""

from datetime import datetime
import os

# ---------------------------------------------------------------------
# BASE CLASS: ETLJob
# ---------------------------------------------------------------------
class ETLJob:
    """
    Base (parent) class that defines the general structure of an ETL job.
    It contains:
    - Common attributes (job_name, start_time, etc.)
    - Shared methods (log, run)
    - Abstract methods (extract, transform, load)
    """

    def __init__(self, job_name):
        self.job_name = job_name
        self._start_time = None   # Encapsulated attribute (private)
        self._end_time = None

    def log(self, message):
        """A shared logging method for all ETL jobs."""
        print(f"[{datetime.now().strftime('%H:%M:%S')}][{self.job_name}] {message}")

    # --------------------------------------------------------------
    # Abstract methods — meant to be overridden by child classes
    # --------------------------------------------------------------
    def extract(self):
        """Each child class will define how data is extracted."""
        raise NotImplementedError("Extract method must be implemented by subclasses")

    def transform(self, data):
        """Each child class will define how data is transformed."""
        raise NotImplementedError("Transform method must be implemented by subclasses")

    def load(self, data):
        """Each child class will define how data is loaded."""
        raise NotImplementedError("Load method must be implemented by subclasses")

    # --------------------------------------------------------------
    # Shared method — common to all ETL jobs
    # --------------------------------------------------------------
    def run(self):
        """
        The 'run' method provides a reusable ETL workflow:
        1. Extract data
        2. Transform data
        3. Load data
        Child classes inherit this method automatically.
        """
        self._start_time = datetime.now()
        self.log("ETL job started.")

        # Polymorphism: each subclass will use its own version of these methods
        data = self.extract()
        transformed = self.transform(data)
        self.load(transformed)

        self._end_time = datetime.now()
        duration = (self._end_time - self._start_time).seconds
        self.log(f"ETL job completed in {duration} seconds.\n")


# ---------------------------------------------------------------------
#  CHILD CLASS #1: CSVToDBETL
# ---------------------------------------------------------------------
class CSVToDBETL(ETLJob): 
    """
    This child class inherits from ETLJob (INHERITANCE).
    It implements its own version of extract, transform, and load (POLYMORPHISM).
    """

    def __init__(self, job_name, source_file, target_db):
        # Call parent constructor using super() to reuse base setup
        super().__init__(job_name)
        self.source_file = source_file
        self.target_db = target_db

    def extract(self):
        self.log(f"Extracting data from CSV file: {self.source_file}")
        # Simulated CSV data
        return [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30},
        ]

    def transform(self, data):
        self.log("Transforming data: Converting names to uppercase.")
        return [{"id": d["id"], "name": d["name"].upper(), "age": d["age"]} for d in data]

    def load(self, data):
        self.log(f"Loading data into database: {self.target_db}")
        for record in data:
            print("Inserted:", record)


# ---------------------------------------------------------------------
# CHILD CLASS #2: APIToJSONETL
# ---------------------------------------------------------------------
class APIToJSONETL(ETLJob):
    """
    Another child class that inherits from ETLJob.
    Demonstrates polymorphism: same method names, different behavior.
    """

    def __init__(self, job_name, api_endpoint, output_file):
        super().__init__(job_name)
        self.api_endpoint = api_endpoint
        self.output_file = output_file

    def extract(self):
        self.log(f"Fetching data from API: {self.api_endpoint}")
        # Simulated API response
        return [{"city": "Karachi", "temp": 33}, {"city": "Lahore", "temp": 31}]

    def transform(self, data):
        self.log("Transforming data: Adding temperature units.")
        return [{"city": d["city"], "temp": f"{d['temp']}°C"} for d in data]

    def load(self, data):
        self.log(f"Writing transformed data to JSON file: {self.output_file}")
        import json
        with open(self.output_file, "w") as f:
            json.dump(data, f, indent=4)
        self.log("Data successfully written to file.")

# ---------------------------------------------------------------------
# DEMO: Running both ETL jobs
# ---------------------------------------------------------------------
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    # Create ETL objects for two different data sources
    csv_etl = CSVToDBETL("CSVToDB", "users.csv", "SQLServer")
    api_etl = APIToJSONETL("APIToJSON", "https://api.weatherdata.io", "weather.json")

    # Each uses the same run() from the base class,
    # but calls its own extract/transform/load implementation.
    csv_etl.run()
    api_etl.run()
