import logging 

def setup_logger() : 
    logger = logging.getLogger('sales_ETL')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    file_handler = logging.FileHandler('sales_etl.log')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)  
    
    return logger