from extractor import extractor
from transformer import transformer
from loader import loader
from logger_config import setup_logger

def main():
    print("Starting ETL process...")

    extractor_obj = extractor()
    transformer_obj = transformer()
    loader_obj = loader()

    # Step 1: Extract
    data = extractor_obj.read_excel()

    # Step 2: Transform
    transformed_data = transformer_obj.clean_data(data)

    # Step 3: Load
    conn = loader_obj.connect()
    if conn:
        loader_obj.delete_table(conn)
        loader_obj.logger.info("Prompting user for confirmation before data insertion.")
        proceed = input("Do you want to continue with data insertion? (yes/no): ")
        if proceed.lower() != 'yes':
            print("ETL Process stopped after the drop operation.")
            conn.close()
            return
        loader_obj.create_and_insert(conn, transformed_data)
        conn.close()
        print("ETL Process Completed Successfully!")

if __name__ == "__main__":
    main()