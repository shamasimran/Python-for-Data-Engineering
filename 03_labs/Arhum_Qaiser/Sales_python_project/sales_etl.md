# Sales Data ETL Pipeline

A modular **ETL (Extract, Transform, Load)** project for processing sales data from Excel files into a SQL Server database using Python.  
The project includes structured logging, modular design, and configurable database connectivity.

---

## Overview

This ETL pipeline automates the process of reading sales data from Excel, cleaning and transforming it, and loading it into a SQL Server table named **`Sales`**.

The process follows a simple 3-step design:

1. **Extractor** — Reads raw sales data from Excel files.  
2. **Transformer** — Cleans, validates, and formats data.  
3. **Loader** — Loads transformed data into SQL Server.  

Comprehensive logging ensures each stage of the ETL process is traceable and auditable.

---

## 📁 Project Structure

### Sales_python_project

- **config.py** — Configuration file (database connection, file paths)
- **extractor.py** — Extracts data from Excel
- **transformer.py** — Transforms/cleans the extracted data
- **loader.py** — Loads data into SQL Server
- **logger_config.py** — Logger setup for consistent logging
- **main.py** — Main ETL execution script
- **sales_transactions.xlsx** — Input data file
- **README.md** — Project documentation
